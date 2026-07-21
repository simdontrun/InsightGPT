"""
Shared Gemini client factory.

Works in two environments:
  - Local dev: reads GEMINI_API_KEY from .env via python-dotenv
  - Streamlit Cloud: reads GEMINI_API_KEY from st.secrets

Call get_gemini_client() anywhere you need a google.genai.Client instance.
"""

import os
from dotenv import load_dotenv

load_dotenv()  # no-op on Streamlit Cloud, safe to call


def _get_api_key() -> str:
    # 1. Try Streamlit secrets (Streamlit Cloud deployment)
    try:
        import streamlit as st
        if "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

    # 2. Fall back to environment variable (local .env)
    key = os.getenv("GEMINI_API_KEY")
    if key:
        return key

    raise RuntimeError(
        "GEMINI_API_KEY not found. "
        "Add it to .env for local dev, or to Streamlit secrets for cloud deployment."
    )


def get_gemini_client():
    from google import genai
    return genai.Client(api_key=_get_api_key())
