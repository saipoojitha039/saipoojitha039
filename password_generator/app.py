import streamlit as st
import string
import random

st.set_page_config(page_title="AI Password Generator", page_icon="🔐", layout="centered")

# Apply CSS for mosaic and background
st.markdown("""
<style>
    .stApp {
        background-image: url('https://static.vecteezy.com/system/resources/thumbnails/002/844/147/small/closed-padlock-on-digital-background-cyber-security-free-vector.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    .mosaic {
        background: rgba(0, 0, 0, 0.6);
        border-radius: 20px;
        padding: 40px 30px;
        max-width: 800px;
        margin: 60px auto;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        color: #ffffff;
    }
    .title {
        text-align: center;
        font-size: 38px;
        color: #ffffff;
        font-weight: bold;
        text-shadow: 2px 2px 6px #000000;
        margin-bottom: 30px;
    }
    .password-box {
        background-color: rgba(0, 0, 0, 0.75);
        padding: 12px;
        border-radius: 10px;
        font-size: 20px;
        text-align: center;
        margin-top: 20px;
        word-break: break-word;
        color: #00ffcc;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


# Title inside the box
st.markdown('<div class="title">AI Password Generator 🔐</div>', unsafe_allow_html=True)

# UI elements inside the mosaic
length = st.slider("Select password length", 6, 40, 12)
use_upper = st.checkbox("Include Uppercase Letters (A-Z)", True)
use_lower = st.checkbox("Include Lowercase Letters (a-z)", True)
use_digits = st.checkbox("Include Numbers (0-9)", True)
use_symbols = st.checkbox("Include Special Characters (!@#$%^&*)", True)

def generate_password():
    chars = ""
    if use_upper: chars += string.ascii_uppercase
    if use_lower: chars += string.ascii_lowercase
    if use_digits: chars += string.digits
    if use_symbols: chars += string.punctuation
    if not chars:
        return "Please select at least one option."
    return ''.join(random.choice(chars) for _ in range(length))

def password_strength(pw):
    score = 0
    if any(c.islower() for c in pw): score += 1
    if any(c.isupper() for c in pw): score += 1
    if any(c.isdigit() for c in pw): score += 1
    if any(c in string.punctuation for c in pw): score += 1
    if len(pw) >= 12: score += 1
    levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    colors = ["#ff4d4d", "#ff944d", "#ffd11a", "#66ff66", "#33cc33"]
    idx = min(score, 4)
    return levels[idx], colors[idx]

if st.button("🔁 Generate Password"):
    password = generate_password()
    if "Please select" in password:
        st.error(password)
    else:
        st.markdown(f"<div class='password-box' id='genPass'>{password}</div>", unsafe_allow_html=True)
        strength, color = password_strength(password)
        st.markdown(f"<h5 style='color:{color}; margin-top:10px;'>Password Strength: {strength}</h5>", unsafe_allow_html=True)

        # Copy to clipboard JS
        js = f"""
        <script>
        function copyToClipboard(text) {{
            navigator.clipboard.writeText(text).then(function() {{
                alert("✅ Password copied to clipboard!");
            }}, function(err) {{
                alert("❌ Failed to copy: ", err);
            }});
        }}
        </script>
        <button onclick="copyToClipboard('{password}')" 
            style="padding:10px 20px; background:#3399ff; color:white; border:none; border-radius:8px;
                   font-weight:bold; margin-top:10px; cursor:pointer;">
            📋 Copy to Clipboard
        </button>
        """
        st.components.v1.html(js, height=60)

# End mosaic container
st.markdown('</div>', unsafe_allow_html=True)