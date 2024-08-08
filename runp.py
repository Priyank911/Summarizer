import gradio as gr
import requests

def summarize(text):
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": "Bearer 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"}

    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    if response.status_code != 200:
        return f"API request failed with status code {response.status_code}: {response.text}"
    
    result = response.json()
    if isinstance(result, list) and len(result) > 0:
        return result[0].get("summary_text", "No summary available.")
    
    return "Unexpected API response structure."

demo = gr.Interface(
    fn=summarize,
    inputs=gr.Textbox(lines=5, label="Input Text"),
    outputs="text",
    title="Text Summarization"
)

if __name__ == "__main__":
    demo.launch(share=True)
