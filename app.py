import streamlit as st

# 강아지 몸무게를 입력받아 체급, 하루 권장 급여량(g), 주의 문구를 반환하는 함수
def calculate_food(weight):
    notice = ""

    # 몸무게 구간에 따라 체급을 나누고 하루 급여량 계산
    if weight < 5.0:
        dog_size = "소형견"
        daily_amount = weight * 30
    elif weight < 15.0:
        dog_size = "중형견"
        daily_amount = weight * 25
    elif weight < 50.0:
        dog_size = "대형견"
        daily_amount = weight * 20
    else:
        dog_size = "초대형견"
        daily_amount = weight * 20
        notice = "⚠️ 50kg 이상입니다. 건강 관리를 위해 먹이 조절이 필요합니다!"

    return dog_size, daily_amount, notice


# 웹앱 제목 및 안내 문구
st.title("🐶 강아지 무게별 먹이 급여량 계산기")
st.write("강아지의 몸무게를 입력하면 하루 적정 사료량과 끼니별 급여량을 알려줍니다.")
st.caption("※ 일반적인 성견 기준 참고용 계산기이며, 실제 급여량은 사료 칼로리와 활동량에 따라 달라질 수 있습니다.")

# 강아지 몸무게 입력창 (0.5kg ~ 100.0kg, 기본값 4.0kg)
weight = st.number_input(
    "강아지 몸무게를 입력하세요 (kg)",
    min_value=0.5,
    max_value=100.0,
    value=4.0,
    step=0.5
)

# 버튼을 누르면 계산 결과 출력
if st.button("급여량 계산하기 🦴"):
    dog_size, daily_amount, notice = calculate_food(weight)

    st.success(f"우리 강아지는 **{dog_size}**이며, 하루 권장 급여량은 **{daily_amount:.1f}g** 입니다!")

    # 50kg 이상일 때만 먹이 조절 경고 문구 표시
    if notice != "":
        st.warning(notice)

    # 아침, 저녁 리스트를 반복문으로 순회하며 한 끼 급여량 출력
    meals = ["아침", "저녁"]
    per_meal = daily_amount / len(meals)

    st.subheader("🍽️ 끼니별 급여 가이드")
    for meal in meals:
        st.write(f"- **{meal}**: {per_meal:.1f}g")
