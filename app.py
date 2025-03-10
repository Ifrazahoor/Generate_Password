import streamlit as st
import re
import random

# List of common weak passwords
COMMON_PASSWORDS = {"password", "123456", "qwerty", "abc123", "password123", "admin", "letmein", "welcome"}

# Function to check password strength
def check_password_strength(password):
    score = 0
    suggestions = []

    # Blacklist Check
    if password.lower() in COMMON_PASSWORDS:
        return '<span style="color: red; font-weight: bold;">❌ This password is too common. Choose a more unique password.</span>', "Weak"

    # Length Check
    if len(password) >= 12:
        score += 1
    else:
        suggestions.append('<span style="color: orange;">🔸 Password should be at least 12 characters long.</span>')

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append('<span style="color: orange;">🔸 Include both uppercase and lowercase letters.</span>')

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append('<span style="color: orange;">🔸 Add at least one number (0-9).</span>')

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append('<span style="color: orange;">🔸 Include at least one special character (!@#$%^&*).</span>')

    # Strength Rating
    if score == 4:
        return '<span style="color: green; font-weight: bold;">✅ Strong Password! Your password is secure.</span>', "Strong"
    elif score == 3:
        return '<span style="color: #f1c40f; font-weight: bold;">⚠️ Moderate Password - Consider adding more security features.</span>', "Moderate"
    else:
        return "<br>".join(suggestions), "Weak"

# Function to generate a strong password
def generate_strong_password():
    while True:
        password = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*", k=14))
        if (re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and 
            re.search(r"\d", password) and re.search(r"[!@#$%^&*]", password)):
            return password

# Apply Background Image
bg_image_url = "https://img.freepik.com/free-vector/dark-hexagonal-background-with-gradient-color_79603-1409.jpg?t=st=1741610985~exp=1741614585~hmac=651712ebe446179bd278b10cb15a379a3fd4397d05e7088b63b61f0421cddbbb&w=1380"  # <-- Replace with actual image URL
st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url("{bg_image_url}");
            background-size: cover;
            background-position: center;
        }}
        .password-box {{
            background: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI - Welcome Section
st.markdown("""
    <div class="password-box">
        <h2 style="color: #2c3e50;">🎉 Welcome to the Ultimate Password Generator!</h2>
        <p style="color: #7f8c8d; font-size: 16px;">
            Use this tool to generate a <strong>strong password</strong> for your accounts and stay secure online.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Password Input Section
st.markdown("<h3 style='color: #3498db;'>Enter your password:</h3>", unsafe_allow_html=True)
password = st.text_input("", type="password")

# Password Strength Feedback
if password:
    feedback, strength = check_password_strength(password)
    
    if strength == "Strong":
        st.markdown(f'<div style="background-color: #d4edda; color: #155724; padding: 10px; border-radius: 5px;">{feedback}</div>', unsafe_allow_html=True)
    elif strength == "Moderate":
        st.markdown(f'<div style="background-color: #fff3cd; color: #856404; padding: 10px; border-radius: 5px;">{feedback}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="background-color: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px;">{feedback}</div>', unsafe_allow_html=True)

# Password Generator Button with Styling
if st.button("🔹 Generate a Strong Password"):
    generated_password = generate_strong_password()
    st.markdown(f'<div style="background-color: #d1ecf1; color: #0c5460; padding: 10px; border-radius: 5px;">'
                f'<b>Suggested Strong Password:</b> <span style="font-weight:bold;">{generated_password}</span></div>', 
                unsafe_allow_html=True)
