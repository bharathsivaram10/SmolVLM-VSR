import gradio as gr
import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq, BitsAndBytesConfig
from peft import PeftModel
import time

# Load your VLM model and processor
# DEVICE = 'cpu'
DEVICE = 'cuda'
bitsnbytes = False
model_id = "HuggingFaceTB/SmolVLM-Instruct"

# Configure 8-bit quantization
bnb_config = BitsAndBytesConfig(
        load_in_8bit=True,
    )

# Load the model in 8-bit for CPU
model = AutoModelForVision2Seq.from_pretrained(
    model_id,
    # quantization_config=bnb_config if bitsnbytes else None,
    _attn_implementation="eager",
    device_map=DEVICE,
    torch_dtype=torch.float32
)

model = PeftModel.from_pretrained(model, "checkpoint-480")
model = model.merge_and_unload()
model.eval()

processor = AutoProcessor.from_pretrained(model_id)

def eval(input):

    input = input.to(DEVICE)
    t1 = time.perf_counter()
    generated_ids = model.generate(**input, max_new_tokens=500)
    generated_texts = processor.batch_decode(generated_ids, skip_special_tokens=True)
    t2 = time.perf_counter()

    print(t2-t1)
    print(generated_texts[0])

# Define the function to process the image and query
def generate_response(image, query):

    # Create input messages
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image"},
                {"type": "text", "text": query}
            ]
        },
    ]

    prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
    input = processor(text=prompt, images=[image], return_tensors="pt")
    input = input.to(DEVICE)

    t1 = time.perf_counter()
    generated_ids = model.generate(**input, max_new_tokens=500)
    generated_texts = processor.batch_decode(generated_ids, skip_special_tokens=True)
    t2 = time.perf_counter()

    comptime = t2 - t1

    # print(f"Inference time: {comptime:.2f}s")
    response = generated_texts[0]

    # **Ensure only assistant's response is returned**
    if "Assistant:" in response:
        response = response.split("Assistant:")[-1].strip()

    return response

# Create Gradio interface
iface = gr.Interface(
    fn=generate_response,
    inputs=[gr.Image(type="pil"), gr.Textbox()],
    outputs="text",
    live=False
)

# Launch the interface
iface.launch()

