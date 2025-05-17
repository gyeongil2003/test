import streamlit as st

# 문제 데이터 정의
music = {
    '🔒486': '비밀번호486',
    '🎨': '팔레트',
    '💃🌇💨': 'dance the night away',
    '⌚🏃': '시간을 달려서',
    '🔥😝': '불장난',
    '👌🤷‍♀️👌': 'yes or yes',
    '💨️️⏩➡️': 'fast forward',
    '👩👸🔵🧔‍♀️💍 / 🧝‍♀️👩‍🦰💙🧔‍♀️💍': '이브,프시케, 그리고 푸른 수염의 아내',
    '❤️📖': 'love story',
    '❤️🤒👧👧👧': 'love sick girls',
    '🌸📆': '봄날',
    '🍳💭💤': '후라이의 꿈'
}

hint = {
    '🔒486': '하루에 네 번',
    '🎨': '이제 조금 알 것 같아 날',
    '💃🌇💨': '바다야 우리와 같이 놀아',
    '⌚🏃': '🌎🤝',
    '🔥😝': '👩‍👧🗣️👨⚠️',
    '👌🤷‍♀️👌': '❌=❌',
    '💨️️⏩➡️': '🤔❤🏃‍♀️🧐👁️‍🗨️',
    '👩👸🔵🧔‍♀️💍 / 🧝‍♀️👩‍🦰💙🧔‍♀️💍': '💥💥💥👉❤️‍🔥⬆️⬆️',
    '❤️📖': '👶👉👁️🍻',
    '❤️🤒👧👧👧': '네 멋대로 내 사랑을 바꿀 순 없어',
    '🌸📆': '눈꽃이 떨어져요 또 조금씩 멀어져요',
    '🍳💭💤': '난 차라리 흘러갈래'
}

# 페이지 구성
st.title("🎵 이모지로 노래 제목 맞추기 게임")
st.markdown("한글과 숫자는 띄어쓰지 않고, 영어 제목은 모두 소문자로 입력해주세요!")
st.markdown("---")

score = 0

for emoji, answer in music.items():
    with st.expander(f"문제: {emoji}"):
        user_input = st.text_input(f"정답을 입력하세요 ({emoji})", key=emoji)

        if user_input:
            if user_input.strip() == answer:
                st.success("정답입니다! 😊 +5점")
                score += 5
            else:
                st.error("틀렸습니다! 😢")
                if st.toggle("힌트 보기", key="hint_" + emoji):
                    st.info(hint.get(emoji, "힌트 없음"))
                    hint_input = st.text_input("힌트를 보고 다시 맞혀보세요", key="re_" + emoji)
                    if hint_input and hint_input.strip() == answer:
                        st.success("정답입니다! 🎉 +2점")
                        score += 2
                    elif hint_input:
                        st.error("아쉽습니다. 다음 문제로 넘어가요!")

st.markdown("---")
st.subheader(f"총 점수: {score}점")

if score == 60:
    st.success("kpop 고인물이군요!")
elif 50 <= score <= 59:
    st.info("아쉽군요! 조금만 있으면 당신은 kpop 고수!")
elif 40 <= score <= 49:
    st.warning("좀 더 분발하세요!")
elif 30 <= score <= 39:
    st.warning("문화생활을 즐기세요^^")
else:
    st.error("당신의 국적을 의심해봐야겠어요.")
