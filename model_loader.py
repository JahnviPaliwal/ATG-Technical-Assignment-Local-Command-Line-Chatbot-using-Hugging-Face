# --- Load model and tokenizer ---
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model_and_tokenizer(model_name="microsoft/DialoGPT-medium"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model
