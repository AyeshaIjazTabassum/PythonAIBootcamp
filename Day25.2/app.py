import torch
from PIL import Image
import gradio as gr
from transformers import BlipProcessor, BlipForQuestionAnswering

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-vqa-base"
)
model = BlipForQuestionAnswering.from_pretrained(
    "Salesforce/blip-vqa-base"
)

def vqa(image, question):
    if image is None or question == "":
        return "Please upload an image and ask a question."

    inputs = processor(image, question, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(**inputs)

    answer = processor.decode(output[0], skip_special_tokens=True)
    return answer

demo = gr.Interface(
    fn=vqa,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Textbox(label="Your Question")
    ],
    outputs=gr.Textbox(label="Answer"),
    title="Visual Question Answering using BLIP",
    description="Ask questions about an image using BLIP (Salesforce)"
)

demo.launch()
