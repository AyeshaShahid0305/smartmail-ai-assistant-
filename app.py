import os
import re

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

st.set_page_config(page_title="AI Email Assistant", page_icon="✉️", layout="wide")

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #f7f9fc 0%, #eef4ff 100%);
        }
        .hero {
            padding: 2rem 2rem 1.2rem 2rem;
            border-radius: 24px;
            background: rgba(255, 255, 255, 0.82);
            border: 1px solid rgba(120, 140, 180, 0.18);
            box-shadow: 0 18px 40px rgba(30, 50, 90, 0.08);
            margin-bottom: 1.2rem;
        }
        .hero h1 {
            margin: 0;
            font-size: 2.4rem;
            color: #14213d;
        }
        .hero p {
            margin-top: 0.4rem;
            color: #4f5d75;
            font-size: 1.02rem;
        }
        .metric-card {
            padding: 1rem 1.1rem;
            border-radius: 18px;
            background: white;
            border: 1px solid rgba(120, 140, 180, 0.18);
            box-shadow: 0 10px 26px rgba(30, 50, 90, 0.06);
        }
        .section-title {
            margin-top: 1.2rem;
            margin-bottom: 0.4rem;
            color: #14213d;
            font-weight: 700;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <h1>AI Email Assistant</h1>
        <p>Turn short notes into polished emails with a subject line, short version, and improved version.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

api_key = os.getenv("OPENAI_API_KEY", "").strip()
model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip()


def build_prompt(purpose_text: str, receiver_text: str, tone_text: str, points_text: str) -> str:
    bullet_points = [line.strip("- ").strip() for line in points_text.splitlines() if line.strip()]
    bullets = "\n".join(f"- {item}" for item in bullet_points) if bullet_points else "- No additional details provided."

    return f"""Write a {tone_text.lower()} email.

Recipient: {receiver_text}
Purpose: {purpose_text}

Requirements:
- Generate a subject line
- Write a complete email
- Include a short version
- Include an improved version
- Fix grammar and improve clarity
- Keep the response professional and well structured

Key points:
{bullets}

Return the answer in this exact format:
Subject: <subject line>

Professional Email:
<email body>

Short Version:
<short version>

Improved Version:
<improved version>
"""


def parse_sections(output_text: str) -> dict[str, str]:
    labels = ["Subject", "Professional Email", "Short Version", "Improved Version"]
    parts: dict[str, str] = {}
    for index, label in enumerate(labels):
        tail = labels[index + 1 :]
        if tail:
            lookahead = "|".join(re.escape(next_label) for next_label in tail)
            pattern = rf"{re.escape(label)}:\s*(.*?)(?=\n(?:{lookahead}):|\Z)"
        else:
            pattern = rf"{re.escape(label)}:\s*(.*)\Z"

        match = re.search(pattern, output_text, flags=re.S)
        parts[label] = match.group(1).strip() if match else ""
    return parts


def build_download_text(sections: dict[str, str]) -> str:
    return (
        f"Subject: {sections.get('Subject', '')}\n\n"
        f"Professional Email:\n{sections.get('Professional Email', '')}\n\n"
        f"Short Version:\n{sections.get('Short Version', '')}\n\n"
        f"Improved Version:\n{sections.get('Improved Version', '')}\n"
    )


left, right = st.columns([1.1, 0.9], gap="large")

with left:
    st.markdown('<div class="section-title">Input Details</div>', unsafe_allow_html=True)
    with st.form("email_form"):
        purpose = st.text_input("Purpose of email", placeholder="Need one day leave")
        receiver = st.text_input("Receiver", placeholder="Manager")
        tone = st.selectbox("Tone", ["Formal", "Friendly", "Professional", "Apologetic"])
        points = st.text_area(
            "Key points",
            placeholder="- I need leave for one day\n- I will complete my pending work before leaving",
            height=220,
        )
        submitted = st.form_submit_button("Generate Email", use_container_width=True)

with right:
    st.markdown('<div class="section-title">What You Get</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            '<div class="metric-card"><strong>Professional</strong><br>Clean full email</div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            '<div class="metric-card"><strong>Structured</strong><br>Subject, short, improved</div>',
            unsafe_allow_html=True,
        )

    st.write("")
    st.markdown(
        '<div class="metric-card"><strong>Supported tones</strong><br>Formal, Friendly, Professional, Apologetic</div>',
        unsafe_allow_html=True,
    )


if submitted:
    if not api_key:
        st.error("OPENAI_API_KEY is missing. Add it to your .env file first.")
    elif not purpose.strip() or not receiver.strip() or not points.strip():
        st.error("Please fill in purpose, receiver, and key points.")
    else:
        prompt = build_prompt(purpose, receiver, tone, points)
        client = OpenAI(api_key=api_key)

        with st.spinner("Generating email..."):
            try:
                response = client.chat.completions.create(
                    model=model_name,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an expert writing assistant that creates clear, polished emails.",
                        },
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0.7,
                )
                output = response.choices[0].message.content.strip()
                sections = parse_sections(output)
                download_text = build_download_text(sections)
                st.session_state["generated_output"] = download_text

                st.markdown('<div class="section-title">Generated Output</div>', unsafe_allow_html=True)
                out1, out2 = st.columns([1, 1], gap="large")

                with out1:
                    st.markdown("**Subject Line**")
                    st.code(sections["Subject"] or "No subject returned", language="text")
                    st.markdown("**Short Version**")
                    st.text_area(
                        "Short Version",
                        value=sections["Short Version"] or "No short version returned",
                        height=160,
                        label_visibility="collapsed",
                    )

                with out2:
                    st.markdown("**Professional Email**")
                    st.text_area(
                        "Professional Email",
                        value=sections["Professional Email"] or "No email returned",
                        height=220,
                        label_visibility="collapsed",
                    )
                    st.markdown("**Improved Version**")
                    st.text_area(
                        "Improved Version",
                        value=sections["Improved Version"] or "No improved version returned",
                        height=180,
                        label_visibility="collapsed",
                    )

                with st.expander("Raw model output"):
                    st.text(output)

                st.download_button(
                    label="Download Result",
                    data=download_text,
                    file_name="ai_email_assistant_output.txt",
                    mime="text/plain",
                    use_container_width=True,
                )
            except Exception as exc:
                st.error(f"Generation failed: {exc}")

st.caption("Built with Python, Streamlit, and the OpenAI API.")
