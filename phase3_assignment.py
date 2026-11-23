from google import genai
import streamlit as st

client = genai.Client(api_key="(API_KEY)")

st.set_page_config(page_title="AI Topic Simplifier", layout="wide")
st.header("AI Topic Simplifier")

topic = st.text_area(
    "Enter your topic here",
    height=100,
    placeholder="e.g. Python programming, World War II, etc."
)
st.markdown(topic)
if st.button("Simplify This"):
    if topic.strip():
        try:
            with st.spinner("Generating content for you..."):
                prompt = f"""
                Analyse {topic} carefully.
                Then give me a brief summary of {topic}
                in three short paragraphs.
                """
                response = client.models.generate_content(model="gemini-3.8-flash",contents=prompt)
                st.subheader("Generated Text:")
                st.markdown(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a topic to simplify.")
