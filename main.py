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

# --- 직업 설명 DB 추가 ---
career_descriptions = {
    "데이터 사이언티스트 📊": "데이터를 분석해 인사이트를 도출하고, 머신러닝 모델을 개발하는 역할을 합니다.",
    "전략 컨설턴트 🧩": "기업의 문제를 분석하고 전략적인 해결 방안을 제시합니다.",
    "AI 엔지니어 🤖": "인공지능 시스템을 설계하고 구현하는 기술 전문가입니다.",
    "연구원 🧪": "과학적인 방법으로 새로운 사실을 탐구하고 연구합니다.",
    "개발자 👨‍💻": "소프트웨어를 설계하고 개발하여 디지털 세상을 구축합니다.",
    "이론 물리학자 🌌": "자연의 법칙을 수학과 이론으로 탐구하는 과학자입니다.",
    "CEO 👔": "회사의 최고경영자로서 전략적 결정을 내리는 리더입니다.",
    "프로덕트 매니저 📱": "제품의 기획부터 출시까지 전 과정을 총괄하는 역할입니다.",
    "경영 컨설턴트 💼": "기업의 운영과 전략을 효율적으로 개선하기 위한 조언을 제공합니다.",
    # 생략된 항목은 실제 사용 시 계속 추가해 주세요.
}

# --- 추천 결과 출력 ---
if st.button("🔍 직업 추천 받기!"):
    st.markdown("## 🎯 추천 직업")
    recommendations = career_dict.get(selected_mbti, [])
    for job in recommendations:
        with st.expander(f"✨ {job}"):
            st.write(career_descriptions.get(job, "설명이 아직 준비되지 않았어요. 😢"))
    st.balloons()

# --- 푸터 ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ by 당신의 진로 친구 AI</p>", unsafe_allow_html=True)
