import torch
from model_loader import load_model_and_tokenizer
from chat_memory import query_faq_kb

model_name = "microsoft/DialoGPT-medium"
tokenizer, model = load_model_and_tokenizer(model_name)

chat_history_ids = None

print("Chatbot ready! Type '/exit' to quit.\n")

while True:
    user_input = input("User: ").strip()
    if user_input.lower() == "/exit":
        print("Exiting chatbot. Goodbye!")
        break

    # Check FAQ knowledge base first
    answer = query_faq_kb(user_input)
    if answer:
        print(f"Bot: {answer}")
        faq_turn = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
        ans_turn = tokenizer.encode(answer + tokenizer.eos_token, return_tensors='pt')
        if chat_history_ids is not None:
            chat_history_ids = torch.cat([chat_history_ids, faq_turn, ans_turn], dim=-1)
        else:
            chat_history_ids = torch.cat([faq_turn, ans_turn], dim=-1)
        continue

    # Encode user input with EOS token
    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # Append tokens to chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if chat_history_ids is not None else new_user_input_ids

    # Generate response with attention mask explicitly
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.9,
        attention_mask=torch.ones(bot_input_ids.shape, dtype=torch.long)
    )

    # Decode bot reply (tokens generated after user input)
    bot_reply = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    print(f"Bot: {bot_reply}")
