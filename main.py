import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(page_title="MBTI 직업 추천 💼", page_icon="🧭", layout="centered")

# --- 헤더 ---
st.markdown("<h1 style='text-align: center; color: #ff69b4;'>🔮 MBTI로 보는 진로 탐색 💼</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>당신의 MBTI는 무엇인가요? 😊<br>당신에게 어울리는 직업을 추천해드릴게요! 🚀</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- MBTI 목록 ---
mbti_types = [
    "INTJ 🧠", "INTP 🔬", "ENTJ 👑", "ENTP 🗣️",
    "INFJ 🌈", "INFP 🎨", "ENFJ 🎤", "ENFP 🌟",
    "ISTJ 📚", "ISFJ 🧸", "ESTJ 💼", "ESFJ 💝",
    "ISTP 🛠️", "ISFP 🎶", "ESTP 🏎️", "ESFP 🎭"
]

mbti_input = st.selectbox("📌 당신의 MBTI를 선택하세요:", mbti_types)

# --- 추천 직업 DB ---
career_dict = {
    "INTJ": ["데이터 사이언티스트 📊", "전략 컨설턴트 🧩", "AI 엔지니어 🤖"],
    "INTP": ["연구원 🧪", "개발자 👨‍💻", "이론 물리학자 🌌"],
    "ENTJ": ["CEO 👔", "프로덕트 매니저 📱", "경영 컨설턴트 💼"],
    "ENTP": ["스타트업 창업자 🚀", "광고 기획자 🎯", "기술 분석가 📡"],
    "INFJ": ["상담사 🧘‍♂️", "작가 ✍️", "심리학자 🧠"],
    "INFP": ["시인 📝", "디자이너 🎨", "사회운동가 ✊"],
    "ENFJ": ["교사 📚", "인사담당자 🤝", "사회복지사 💖"],
    "ENFP": ["마케터 📢", "방송인 🎤", "브랜드 디렉터 💡"],
    "ISTJ": ["회계사 📑", "공무원 🏛️", "데이터 분석가 📉"],
    "ISFJ": ["간호사 🏥", "초등교사 🧸", "보육교사 👶"],
    "ESTJ": ["관리자 📋", "프로젝트 매니저 🏗️", "경찰관 🚓"],
    "ESFJ": ["이벤트 플래너 🎉", "간호 관리자 🩺", "호텔 매니저 🏨"],
    "ISTP": ["기계공 🛠️", "파일럿 ✈️", "보안 전문가 🔐"],
    "ISFP": ["패션 디자이너 👗", "사진작가 📸", "음악가 🎵"],
    "ESTP": ["영업사원 💬", "트레이더 💹", "스턴트 배우 🎬"],
    "ESFP": ["배우 🎭", "MC 🎙️", "무대 연출가 💃"]
}

# --- MBTI 추출 ---
selected_mbti = mbti_input.split()[0]  # 이모지 제거

if st.button("🔍 직업 추천 받기!"):
    st.markdown("## 🎯 추천 직업")
    recommendations = career_dict.get(selected_mbti, [])
    for job in recommendations:
        st.success(f"✨ {job}")
    st.balloons()

# --- 푸터 ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ by 당신의 진로 친구 AI</p>", unsafe_allow_html=True)
