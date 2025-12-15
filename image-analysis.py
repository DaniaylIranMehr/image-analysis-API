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

def encode_image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def analyze_image(image):
    try:
        image_base64 = encode_image_to_base64(image)
        image_ext = "png"

        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What is in this image?"
                    },
                    {
                        "type": "image_url",
                        "image_url":{
                            "url": f"data:image/{image_ext};base64,{image_base64}",
                            "detail": "auto"
                        }
                    }
                ]
            }
        ]

        ai_message = llm.invoke(messages)

        return ai_message.content


    except Exception as e:
        return f"Error: {str(e)}"
    


iface = gr.Interface(
    fn=analyze_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(label="Explanation", lines=15),
    title="Image Analysis",
    description="Upload an image and let AI describe it"
)

iface.launch()