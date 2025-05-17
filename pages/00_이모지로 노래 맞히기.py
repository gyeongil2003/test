import streamlit as st
import streamlit.components.v1 as components

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
st.info("정답을 맞히면 +5, 힌트 사용 후 맞히면 +3, 패스하면 정답이 공개되고 +0점입니다.")
st.warning("한글과 숫자는 띄어쓰지 않고, 영어 제목은 모두 소문자로 입력해주세요!")
st.markdown("---")

# 상태 저장용 세션
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.show_hint = False
    st.session_state.answered = False
    st.session_state.hint_used = False

questions = list(music.items())

if st.session_state.question_index < len(questions):
    emoji, answer = questions[st.session_state.question_index]
    # 진행도 계산
    current = st.session_state.question_index + 1
    total = len(questions)
    progress_ratio = current / total
    
    # 텍스트 + 진행바 함께 표시
    st.subheader(f"문제 {current} / {total}")
    st.progress(progress_ratio)

    st.markdown(f"### {emoji}")

    if not st.session_state.answered:
        user_input = st.text_input("정답을 입력하세요:", key=f"q_{st.session_state.question_index}")

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("제출"):
                if user_input.strip() == answer:
                    st.success("정답입니다! 😊 +5점")
                    st.session_state.score += 5
                    st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnpybTl6eWJ3N2tkNTdmejd4dTc5dHBlMXZlc3RwOXk4eHh0eDBrYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pYkD8W72qnO97rOEh8/giphy.gif", use_container_width=True)
                    st.session_state.answered = True
                else:
                    st.error("틀렸습니다! 😢")
        with col2:
            if not st.session_state.show_hint:
                if st.button("힌트 보기"):
                    st.session_state.show_hint = True
                    st.session_state.hint_used = True


    if st.session_state.show_hint and not st.session_state.answered:
        st.info("힌트: " + hint.get(emoji, "힌트 없음"))
        hint_input = st.text_input("힌트를 보고 다시 정답을 입력하세요:", key=f"hint_{st.session_state.question_index}")
    
        hint_col1, hint_col2 = st.columns([1, 1])
        with hint_col1:
            if st.button("정답 제출"):
                if hint_input.strip() == answer:
                    st.success("정답입니다! 🎉 +3점")
                    st.session_state.score += 3
                    play_correct_sound()
                else:
                    st.error("아쉽습니다. 다음 문제로 넘어가요!")
                st.session_state.answered = True
        with hint_col2:
            if st.button("패스!"):
                st.warning(f"정답은 '{answer}'였습니다! 다음 문제로 넘어갑니다.")
                st.session_state.answered = True


else:
    st.subheader(f"🎉 게임 종료! 총 점수: {st.session_state.score}점")
    if st.session_state.score >= 60:
        st.success("kpop 고인물이군요!")
        st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGp6dXc3N2FtdG9kcmVuOHd1MDZraGsyczRncGF5NjdybzM1MHY3ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fxsqOYnIMEefC/giphy.gif", use_container_width=True)
    elif 50 <= st.session_state.score <= 59:
        st.info("아쉽군요! 조금만 있으면 당신은 kpop 고수!")
    elif 40 <= st.session_state.score <= 49:
        st.warning("좀 더 분발하세요!")
    elif 30 <= st.session_state.score <= 39:
        st.warning("문화생활을 즐기세요^^")
    else:
        st.error("당신의 국적을 의심해봐야겠어요.")
