import torch
import gradio as gr
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import os

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

image_folder = "images"
image_paths = [os.path.join(image_folder, img) for img in os.listdir(image_folder)]
images = [Image.open(p).convert("RGB") for p in image_paths]

image_inputs = processor(images=images, return_tensors="pt")

with torch.no_grad():
    image_embeddings = model.get_image_features(**image_inputs)

def search(query):
    text_inputs = processor(text=[query], return_tensors="pt")
    with torch.no_grad():
        text_embedding = model.get_text_features(**text_inputs)

    similarity = torch.matmul(text_embedding, image_embeddings.T)
    best_idx = similarity.argmax().item()

    return images[best_idx]

demo = gr.Interface(
    fn=search,
    inputs=gr.Textbox(label="Search with text"),
    outputs=gr.Image(label="Best Matching Image"),
    title="CLIP Image Search",
    description="Visualizing how CLIP matches text with images"
)

demo.launch()
