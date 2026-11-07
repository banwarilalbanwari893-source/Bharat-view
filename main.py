
import streamlit as st

st.set_page_config(
    page_title="Bharat View AI",
    page_icon="🐍"
)

st.title("🐍 Bharat View AI")
st.subheader("Your Personal AI Team")

st.success("Welcome to Bharat View AI!")

st.write("ChatGPT + Grok = Your AI Team")

st.divider()

st.header("🤖 अपना AI काम चुनें")

task = st.text_area(
    "आप AI से क्या काम करवाना चाहते हैं?",
    placeholder="यहाँ अपना काम लिखें..."
)

if st.button("🚀 काम शुरू करो"):
    if task.strip():
        st.info("आपका काम दर्ज हो गया है।")
        st.write("आपका काम:", task)
        st.warning(
            "AI कनेक्शन अगले चरण में जोड़ा जाएगा।"
        )
    else:
        st.error("पहले अपना काम लिखें।")

st.divider()

st.write("🛡️ Upload करने से पहले आपकी अनुमति जरूरी होगी।")
st.caption("Bharat View AI - Version 1.0")
