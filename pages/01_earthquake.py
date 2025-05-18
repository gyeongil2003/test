import streamlit as st
import pandas as pd
import requests
import datetime
import pydeck as pdk

st.set_page_config(page_title="지진 발생 시각화", layout="wide")

st.title("🇰🇷 대한민국 지진 시각화 앱")

# 1. 사용자로부터 날짜 범위 입력
today = datetime.date.today()
start_date = st.date_input("조회 시작일", today - datetime.timedelta(days=7))
end_date = st.date_input("조회 종료일", today)

# 2. 고정된 대한민국 범위 (위치 입력 제거)
min_lat, max_lat = 33.0, 39.5
min_lon, max_lon = 124.0, 132.0

# 3. USGS API 호출
if st.button("지진 정보 불러오기"):
    url = (
        f"https://earthquake.usgs.gov/fdsnws/event/1/query"
        f"?format=geojson&starttime={start_date}&endtime={end_date}"
        f"&minlatitude={min_lat}&maxlatitude={max_lat}"
        f"&minlongitude={min_lon}&maxlongitude={max_lon}"
    )

    res = requests.get(url)
    data = res.json()

    if "features" not in data or len(data["features"]) == 0:
        st.warning("최근 기간 동안 대한민국 주변에서 발생한 지진이 없습니다.")
    else:
        df = pd.DataFrame([{
            "장소": f["properties"]["place"],
            "규모": f["properties"]["mag"],
            "시간": pd.to_datetime(f["properties"]["time"], unit="ms"),
            "경도": f["geometry"]["coordinates"][0],
            "위도": f["geometry"]["coordinates"][1],
        } for f in data["features"]])

        st.success(f"✅ 총 {len(df)}건의 지진 발생")
        st.metric("📊 평균 규모", round(df['규모'].mean(), 2))
        st.dataframe(df)

        # 지도 시각화
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=36.5,
                longitude=127.5,
                zoom=5,
                pitch=0,
            ),
            layers=[
                pdk.Layer(
                    "ScatterplotLayer",
                    data=df,
                    get_position='[경도, 위도]',
                    get_color='[255, 0, 0, 160]',
                    get_radius='규모 * 10000',
                    pickable=True,
                ),
            ],
            tooltip={
                "html": "<b>📍 장소:</b> {장소}<br><b>📈 규모:</b> {규모}<br><b>🕒 시간:</b> {시간}",
                "style": {
                    "backgroundColor": "white",
                    "color": "black",
                    "fontSize": "14px"
                }
            }
        ))
