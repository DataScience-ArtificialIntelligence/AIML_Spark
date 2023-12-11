import json

def load_config(config_file="model_config.json"):
    with open(config_file, "r") as f:
        config = json.load(f)
    return config

# Load model parameters from the config file
config = load_config()

# Assign config values to variables
model_name = config["model_name"]
use_4bit = config["use_4bit"]
bnb_4bit_quant_type = config["bnb_4bit_quant_type"]
bnb_4bit_compute_dtype = config["bnb_4bit_compute_dtype"]
use_nested_quant = config["use_nested_quant"]
lora_r = config["lora_r"]
lora_alpha = config["lora_alpha"]
lora_dropout = config["lora_dropout"]
device_map = config["device_map"]
output_dir = config["output_dir"]
num_train_epochs = config["num_train_epochs"]
fp16 = config["fp16"]
bf16 = config["bf16"]
per_device_train_batch_size = config["per_device_train_batch_size"]
per_device_eval_batch_size = config["per_device_eval_batch_size"]
gradient_accumulation_steps = config["gradient_accumulation_steps"]
gradient_checkpointing = config["gradient_checkpointing"]
max_grad_norm = config["max_grad_norm"]
learning_rate = config["learning_rate"]
weight_decay = config["weight_decay"]
optim = config["optim"]
lr_scheduler_type = config["lr_scheduler_type"]
max_steps = config["max_steps"]
warmup_ratio = config["warmup_ratio"]
group_by_length = config["group_by_length"]
save_steps = config["save_steps"]
logging_steps = config["logging_steps"]
max_seq_length = config["max_seq_length"]
packing = config["packing"]