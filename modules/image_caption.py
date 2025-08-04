from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

import os
os.system("uv pip install transformers")

# Load processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
model.eval()
model.to("cuda" if torch.cuda.is_available() else "cpu")

def caption_from_image(uploaded_file):
    try:
        image = Image.open(uploaded_file).convert("RGB")
        inputs = processor(images=image, return_tensors="pt").to(model.device)

        with torch.no_grad():
            output = model.generate(**inputs, max_new_tokens=60)

        caption = processor.decode(output[0], skip_special_tokens=True)
        return caption.strip()

    except Exception as e:
        return f"❌ Error generating caption: {str(e)}"
