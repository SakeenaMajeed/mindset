import streamlit as st
import random
import time
from datetime import datetime, timedelta

# 🎨 Page Styling
st.set_page_config(
    page_title="Growth Mindset Challenge",
    page_icon="🚀",
    layout="centered"
)

# ✅ Custom CSS for Creative UI
st.markdown("""
    <style>
        /* Global Styles */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2);  /* Soft gradient background */
            font-family: 'Arial', sans-serif;
            padding: 20px;
        }
        h1, h2, h3, h4, h5, h6, p, span {
            color: #333333 !important;
            text-align: left;
        }
        h1 {
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #4a148c !important;  /* Purple for main heading */
            text-align: center;
            animation: fadeIn 2s ease-in-out;
        }
        h2 {
            font-size: 28px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 10px;
            color: #6a1b9a !important;  /* Dark purple for subheadings */
        }
        h3 {
            font-size: 22px;
            font-weight: bold;
            margin-top: 15px;
            margin-bottom: 10px;
            color: #6a1b9a !important;
        }
        /* Button Styles */
        .stButton>button {
            background-color: #6a1b9a !important;  /* Dark purple button */
            color: white !important;
            font-size: 16px;
            font-weight: bold;
            border-radius: 25px;
            padding: 12px 24px;
            transition: 0.3s;
            width: 100%;
            max-width: 200px;
            display: block;
            margin: auto;
            border: none;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stButton>button:hover {
            background-color: #4a148c !important;  /* Darker purple on hover */
            transform: scale(1.05);
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
        }
        /* Input Field Styles */
        .stTextInput>div>div>input {
            border-radius: 12px;
            padding: 10px;
            border: 2px solid #6a1b9a;
            transition: 0.3s;
            width: 100%;
            max-width: 400px;
        }
        .stTextInput>div>div>input:focus {
            border-color: #4a148c;
            box-shadow: 0 0 8px rgba(74, 20, 140, 0.5);
        }
        /* Card Styles for Sections */
        .card {
            background: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: 0.3s;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        /* Calendar Table Styles */
        .calendar-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        .calendar-table th, .calendar-table td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
        }
        .calendar-table th {
            background-color: #6a1b9a;
            color: white;
            font-weight: bold;
        }
        .calendar-table td {
            background-color: white;
            transition: 0.3s;
        }
        .calendar-table td:hover {
            background-color: #6a1b9a;
            color: white;
            transform: scale(1.1);
        }
        .calendar-table .today {
            background-color: #4a148c;
            color: white;
            font-weight: bold;
        }
        /* Progress Bar Styles */
        .stProgress>div>div>div {
            background-color: #6a1b9a !important;  /* Purple progress bar */
            border-radius: 10px;
        }
        /* Footer Styles */
        .footer {
            text-align: center;
            margin-top: 40px;
            padding: 10px;
            font-size: 14px;
            color: #777777;
        }
        /* Animation for headings */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        /* Remove extra spacing after Set Goal */
        .stSuccess {
            margin-bottom: 0 !important;
        }
        .stProgress {
            margin-bottom: 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# 🔥 Main Heading with Animation
st.markdown("<h1>🚀 Growth Mindset Challenge 🌱</h1>", unsafe_allow_html=True)

# 🎯 User Name Input
st.markdown("<h2>👩🏻‍💻 Your Name</h2>", unsafe_allow_html=True)
user_name = st.text_input("Enter your name:", key="username", placeholder="Sakeena")

# Display the user's name if entered
if user_name:
    st.markdown(f"<h2>👋 Welcome, {user_name}!</h2>", unsafe_allow_html=True)

# 🚀 Daily Growth Tip
st.markdown("<h2>💡 Today's Growth Tip</h2>", unsafe_allow_html=True)
daily_tips = [
    "Make it a habit to learn something new every day!", 
    "Challenges are the stepping stones to growth!", 
    "Consistency is the secret to success—never stop trying!"
]
today_tip = random.choice(daily_tips)
st.markdown(f'<div class="card"><p>{today_tip}</p></div>', unsafe_allow_html=True)

# 📅 Calendar for Tracking Growth Tips
st.markdown("<h2>📅 Growth Calendar</h2>", unsafe_allow_html=True)

# Generate a calendar for the current month
now = datetime.now()
current_month = now.month
current_year = now.year
days_in_month = (datetime(current_year, current_month + 1, 1) - timedelta(days=1)).day
first_day_of_month = datetime(current_year, current_month, 1).weekday()  # Monday is 0, Sunday is 6

# Display the calendar
st.write(f"### {now.strftime('%B %Y')}")

# Create the calendar table
calendar_html = """
<table class="calendar-table">
    <thead>
        <tr>
            <th>Mon</th>
            <th>Tue</th>
            <th>Wed</th>
            <th>Thu</th>
            <th>Fri</th>
            <th>Sat</th>
            <th>Sun</th>
        </tr>
    </thead>
    <tbody>
"""

# Fill the calendar with days
day_counter = 1
for week in range(6):  # Max 6 weeks in a month
    calendar_html += "<tr>"
    for day in range(7):  # 7 days in a week
        if week == 0 and day < first_day_of_month:  # Skip days before the first day of the month
            calendar_html += "<td></td>"
        elif day_counter > days_in_month:  # Stop if all days are filled
            calendar_html += "<td></td>"
        else:
            if day_counter == now.day:  # Highlight today's date
                calendar_html += f'<td class="today">{day_counter}</td>'
            else:
                calendar_html += f"<td>{day_counter}</td>"
            day_counter += 1
    calendar_html += "</tr>"
calendar_html += """
    </tbody>
</table>
"""

# Display the calendar table
st.markdown(calendar_html, unsafe_allow_html=True)

# Add a tip for today's date
st.markdown(f"<h3>📌 Tip for Today ({now.strftime('%d %B')})</h3>", unsafe_allow_html=True)
st.markdown(f'<div class="card"><p>{today_tip}</p></div>', unsafe_allow_html=True)

# 📅 7-Day Growth Challenge
st.markdown("<h2>🌟 7-Day Growth Challenge</h2>", unsafe_allow_html=True)
challenges = [
    "Plan how to improve a weak skill!",
    "Read one chapter of a motivational book!",
    "Research a new skill you’re interested in!",
    "Try completing a challenging task!",
    "Read about a mentor or role model!",
    "Step out of your comfort zone and try something new!",
    "Analyze your progress and set your next goal!"
]
st.markdown(f'<div class="card"><p>{random.choice(challenges)}</p></div>', unsafe_allow_html=True)

# 🧠 Memory Boost Mini-Game
st.markdown("<h2>🧠 Memory Boost Game</h2>", unsafe_allow_html=True)
memory_words = ["Success", "Effort", "Mindset", "Challenge", "Persistence", "Learning"]
word_to_remember = random.choice(memory_words)
st.markdown(f'<div class="card"><p>Remember this word for 5 seconds: <strong>{word_to_remember}</strong></p></div>', unsafe_allow_html=True)
time.sleep(5)
st.write("Now type the word you remember!")
user_memory_input = st.text_input("Type Here:", key="memory_game", placeholder="Type the word here...")
if user_memory_input:
    if user_memory_input.strip().lower() == word_to_remember.lower():
        st.success("🚀 Great Job! Your memory is strong!")
    else:
        st.error("🚫 Oops! Try again and improve your focus!")

# 💡 Inspiring Stories Section
st.markdown("<h2>📚 Inspiring Stories</h2>", unsafe_allow_html=True)
story = "Albert Einstein was a slow learner, but his continuous effort made him a genius!"
st.markdown(f'<div class="card"><p>{story}</p></div>', unsafe_allow_html=True)

# 🌍 Footer
st.markdown("---")  # Horizontal line for separation
st.markdown('<div class="footer">🚀 Developed with ❤️ by Growth Mindset Team | Keep Growing! 🌱</div>', unsafe_allow_html=True)