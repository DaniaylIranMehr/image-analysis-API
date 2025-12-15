import gradio as gr
import base64
import os
from io import BytesIO
from langchain_openai import ChatOpenAI


base_url="https://openrouter.ai/api/v1"
api_key="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"
model_name="google/gemma-3-4b-it:free"

llm = ChatOpenAI(
    base_url=base_url,
    model=model_name,
    api_key=api_key
)