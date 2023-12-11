import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline, logging
import sys

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

model_id = "nvjkkartik/llama2-qlora-hi-7b"
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb_config, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_id)

device = "cuda:0"


def run_inference(message):
    # Ignore warnings
    logging.set_verbosity(logging.CRITICAL)

    messages = [
    {"role": "user", "content": message}
    ]


    encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

    model_inputs = encodeds.to(device)


    generated_ids = model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
    decoded = tokenizer.batch_decode(generated_ids)
    print(decoded[0])
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python inference.py <message>")
        sys.exit(1)
        
    message = sys.argv[1]

    # Your inference logic here
    print(f"Inference result for message: {run_inference(message)}")
    
if __name__ == '__main__':
    main()