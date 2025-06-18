import streamlit as st
import joblib
import os
import time

# Inject CSS for background and styles
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://static.vecteezy.com/system/resources/thumbnails/013/087/516/small_2x/diagonal-golden-line-glass-cube-on-black-background-illustration-of-website-banner-poster-sign-corporate-business-social-media-post-billboard-agency-advertising-media-motion-video-animation-wave-vector.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .main-container {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 20px;
        color: white;
    }
    h1, h2, h3 {
        color: white !important;
    }
    .stTextInput>div>div>input {
        background-color: #fff0 !important;
        color: white !important;
    }
    .stTextArea textarea {
        background-color: #2c2c2c !important;
        color: white !important;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5em 1.5em;
    }
    .stAlert {
        background-color: #444 !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Container to group app content
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    st.title("AI Sentiment Analyzer ✨")
    st.write("Analyze the sentiment of any text using AI (ML + NLP)")

    # Load model and vectorizer
    model_file = "sentiment_model.pkl"
    vectorizer_file = "vectorizer.pkl"

    if os.path.exists(model_file) and os.path.exists(vectorizer_file):
        model = joblib.load(model_file)
        vectorizer = joblib.load(vectorizer_file)
        st.success("✅ Model loaded successfully!")
    else:
        st.error("❌ Model files not found. Please run `train_model.py`.")
        st.stop()

    # User input
    user_input = st.text_area("Enter your text below:", height=150)

    if st.button("🔍 Analyze Sentiment"):
        if not user_input.strip():
            st.warning("⚠️ Please enter text before analyzing.")
        else:
            with st.spinner("🔎 Predicting sentiment..."):
                time.sleep(1.5)
                input_vec = vectorizer.transform([user_input])
                prediction = model.predict(input_vec)[0].lower()

                if prediction == "positive":
                    st.success("😊 **Sentiment: Positive**")
                    st.balloons()
                elif prediction == "negative":
                    st.error("😠 **Sentiment: Negative**")
                else:
                    st.info("😐 **Sentiment: Neutral**")

    st.markdown('</div>', unsafe_allow_html=True)
