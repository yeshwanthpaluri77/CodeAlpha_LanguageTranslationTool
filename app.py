import streamlit as st
from deep_translator import GoogleTranslator

#Page config
st.set_page_config(
    page_title="AI Translator",
    layout="centered"
)

#Customized CSS
st.markdown("""
<style>

/*Main background*/
.stApp {
    background: linear-gradient(to bottom right, #0f172a, #020617);
    color: white;
}

/*Title*/
.main-title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #38bdf8;
    margin-bottom: 10px;
}

/*Subtitle*/
.sub-text {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 40px;
}

/*Input boxes*/
textarea, .stSelectbox div[data-baseweb="select"] {
    border-radius: 15px !important;
}

/*Button*/
.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #38bdf8, #6366f1);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: none;
    border-radius: 15px;
    padding: 12px;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
    background: linear-gradient(to right, #0ea5e9, #4f46e5);
}

/*Output card*/
.output-box {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 20px;
    margin-top: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
}

/*Footer*/
.footer {
    text-align: center;
    margin-top: 50px;
    color: gray;
}

</style>
""", unsafe_allow_html=True)

#TITLE
st.markdown('<div class="main-title">AI Language Translator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-text">Translate text instantly across multiple languages using AI</div>',
    unsafe_allow_html=True
)

#Text input
text = st.text_area(
    "Enter your text",
    height=150,
    placeholder="Type something here..."
)

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        list(languages.keys())
    )

#button
if st.button("Translate Now"):

    if text:

        with st.spinner("Translating..."):

            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

        st.success("Translation Completed!!!")

        st.markdown(f"""
        <div class="output-box">
            <h3>Translated Text</h3>
            <p style="font-size:20px;">{translated}</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("Please enter some text.")
