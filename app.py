import streamlit as st
from datetime import date, timedelta

# Page config
st.set_page_config(page_title="🎂 Age Calculator", layout="centered")

# Custom CSS for gradient background & styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #89f7fe, #66a6ff);
        color: #fff;
    }
    .stApp {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    }
    h1 {
        text-align: center;
        color: #333;
    }
    .stSuccess, .stInfo {
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🎉 Age Calculator 🎂")

# Input: Date of Birth
dob = st.date_input("📅 Select your Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())

# Today's Date
today = date.today()

if dob:
    # Calculate age
    age_years = today.year - dob.year
    age_months = today.month - dob.month
    age_days = today.day - dob.day

    # Adjust if birthday hasn't come yet this year
    if age_days < 0:
        age_months -= 1
        prev_month = (today.month - 1) if today.month > 1 else 12
        prev_year = today.year if today.month > 1 else today.year - 1
        last_day_prev_month = (date(prev_year, prev_month + 1, 1) - timedelta(days=1)).day
        age_days += last_day_prev_month

    if age_months < 0:
        age_years -= 1
        age_months += 12

    # Display result
    st.success(f"🎂 You are *{age_years} years, {age_months} months, {age_days} days* old!")

    # Extra info: total days lived
    total_days = (today - dob).days
    st.info(f"🌍 You have lived for *{total_days:,} days* ")

    # 🎉 Next Birthday Countdown
    this_year_birthday = date(today.year, dob.month, dob.day)

    if this_year_birthday < today:
        next_birthday = date(today.year + 1, dob.month, dob.day)
    else:
        next_birthday = this_year_birthday

    days_left = (next_birthday - today).days

    if days_left == 0:
        st.balloons()
        st.success("🎉 Happy Birthday! 🥳 🎂 🎁")
    else:
        st.warning(f"⏳ Your next birthday is in *{days_left} days* 🎊")