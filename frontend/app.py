import streamlit as st
import requests

st.set_page_config(
    page_title="AI App Generator",
    layout="wide"
)

st.title("AI Platform Engineer Prototype")

st.markdown(
    "Generate Structured App Configurations Using AI Pipelines"
)

prompt = st.text_area(
    "Enter your app idea"
)

if st.button("Generate"):

    response = requests.post(
        "http://127.0.0.1:8000/generate",
        json={"prompt": prompt}
    )

    data = response.json()

    st.success("Generation Completed")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Intent")
        st.json(data["intent"])

        st.subheader("Pages")
        st.json(data["pages"])

        st.subheader("Database")
        st.json(data["database"])

        st.subheader("Validation")
        st.json(data["validation"])

    with col2:

        st.subheader("API Schema")
        st.json(data["api_schema"])

        st.subheader("Auth System")
        st.json(data["auth"])

        st.subheader("Assumptions")
        st.json(data["assumptions"])

        st.subheader("Metrics")
        st.json(data["metrics"])