import streamlit as st
import pandas as pd
import requests
import datetime
import pydeck as pdk
import altair as alt

st.set_page_config(page_title="지진 발생 시각화", layout="wide")

st.title("🌍 전 세계 지진 시각화 웹앱")

# 날짜 입력
today = datetime.date.today()
start_date = st.date_input("조회 시작일", today - datetime.timedelta(days=7))
end_date = st.date_input("조회 종료일", today)

# 데이터 요청
if st.button("지진 정보 불러오기"):
       with st.spinner("🌐 데이터를 불러오는 중입니다..."):
        url = (
    f"https://earthquake.usgs.gov/fdsnws/event/1/query"
    f"?format=geojson&starttime={start_date}&endtime={end_date}"
)
    
        res = requests.get(url)
    
        if res.status_code != 200:
            st.error(f"요청 실패 (상태 코드 {res.status_code})")
            st.stop()
    
        try:
            data = res.json()
        except ValueError:
            st.error("⚠️ 응답이 JSON 형식이 아닙니다.")
            st.text(res.text)
            st.stop()
        
        if "features" not in data or len(data["features"]) == 0:
            st.warning("선택한 기간 동안 지진 데이터가 없습니다.")
        else:
            df = pd.DataFrame([{
                "장소": f["properties"]["place"],
                "규모": f["properties"]["mag"],
                "시간": pd.to_datetime(f["properties"]["time"], unit="ms", errors="coerce"),
                "경도": f["geometry"]["coordinates"][0],
                "위도": f["geometry"]["coordinates"][1],
            } for f in data["features"]])
    
            st.success(f"✅ 총 {len(df)}건의 지진 발생")
            st.metric("📊 평균 규모", round(df['규모'].mean(), 2))
    
            # 표: 가운데 정렬
            st.markdown("""
            <style>
            .centered-table td, .centered-table th {
                text-align: center !important;
            }
            </style>
            """, unsafe_allow_html=True)
            st.markdown('<div class="centered-table">', unsafe_allow_html=True)
            st.dataframe(df.style.set_properties(**{'text-align': 'center'}), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
        # 지도 시각화
            st.pydeck_chart(pdk.Deck(
                map_style='mapbox://styles/mapbox/light-v9',
                initial_view_state=pdk.ViewState(
                    latitude=0,
                    longitude=0,
                    zoom=1.2,
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

        # 대륙 구분 (간단한 위경도 기준)
        def estimate_continent(lat, lon):
            if -90 <= lat <= 85:
                if -170 <= lon <= -30:
                    if lat < 15:
                        return "남아메리카"
                    else:
                        return "북아메리카"
                elif -30 < lon <= 50:
                    return "유럽"
                elif -30 < lon <= 60 and lat < 15:
                    return "아프리카"
                elif 60 < lon <= 150 and lat > 0:
                    return "아시아"
                elif 110 < lon <= 180 and lat < 0:
                    return "오세아니아"
            return "기타"


        df['대륙'] = df.apply(lambda row: estimate_continent(row['위도'], row['경도']), axis=1)

        # 대륙별 빈도 그래프
        st.markdown("---")
        st.markdown("### 🌎 대륙별 지진 발생 건수")
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('대륙:N', title="대륙"),
            y=alt.Y('count():Q', title="지진 건수"),
            color='대륙:N'
        ).properties(
            width=600,
            height=400
        )
        st.altair_chart(chart, use_container_width=True)
