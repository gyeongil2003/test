import streamlit as st
import pandas as pd
import requests
import datetime
import pydeck as pdk

st.set_page_config(page_title="지진 발생 시각화", layout="wide")

st.title("🌍 지진 발생 시각화 웹앱")

# 1. 사용자로부터 날짜 범위 입력
today = datetime.date.today()
start_date = st.date_input("조회 시작일", today - datetime.timedelta(days=7))
end_date = st.date_input("조회 종료일", today)

# 2. 위도, 경도 범위 지정 (기본: 대한민국)
st.markdown("**🔍 위치 범위 설정 (위도 / 경도)**")
min_lat = st.number_input("최소 위도", value=33.0)
max_lat = st.number_input("최대 위도", value=39.5)
min_lon = st.number_input("최소 경도", value=124.0)
max_lon = st.number_input("최대 경도", value=132.0)

# 3. USGS API 호출
if st.button("지진 정보 불러오기"):
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_date}&endtime={end_date}&minlatitude={min_lat}&maxlatitude={max_lat}&minlongitude={min_lon}&maxlongitude={max_lon}"

    res = requests.get(url)
    data = res.json()

    if len(data["features"]) == 0:
        st.warning("선택한 범위 내 지진이 없습니다.")
    else:
        # 4. 데이터 정리
        df = pd.DataFrame([{
            "장소": f["properties"]["place"],
            "규모": f["properties"]["mag"],
            "시간": pd.to_datetime(f["properties"]["time"], unit="ms"),
            "경도": f["geometry"]["coordinates"][0],
            "위도": f["geometry"]["coordinates"][1],
        } for f in data["features"]])

        # 5. 결과 출력
        st.success(f"✅ 총 {len(df)}건의 지진 발생")
        st.metric("📊 평균 규모", round(df['규모'].mean(), 2))
        st.dataframe(df)

        # 6. 지도 시각화 (한국 중심 + 툴팁 포함)
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=36.5,   # 대한민국 중심
                longitude=127.5,
                zoom=5,
                pitch=0,
            ),
            layers=[
                pdk.Layer(
                    "ScatterplotLayer",
                    data=df,
                    get_position='[경도, 위도]',
                    get_color='[200, 30, 0, 160]',
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
