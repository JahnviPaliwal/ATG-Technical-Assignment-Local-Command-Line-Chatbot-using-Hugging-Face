# ATG-Technical-Assignment-Local-Command-Line-Chatbot-using-Hugging-Face
ATG Technical Assignment:  Local Command-Line Chatbot using Hugging  Face =>Machine Learning Intern Deliverables


## Overview
This project is a simple command-line chatbot built using Hugging Face's DialoGPT-medium model. It was developed as part of my first task for the ATG internship, where I applied as a Machine Learning intern.

The chatbot uses a continual CLI loop and maintains conversational context through chat history tokens, while also integrating a FAQ knowledge base for instant factual replies.

## Project Structure
The project consists of three main Python files:

- **model_loader.py**  
  Loads the pre-trained DialoGPT model and tokenizer for text generation.

- **chat_memory.py**  
  Maintains a FAQ knowledge base with common questions and handles chat memory logic by storing tokenized conversation history.

- **interface.py**  
  Implements the CLI loop that takes user input, checks FAQs, generates responses using the model, and manages chat history.

## Video file link
[![Chatbot Demo](https://drive.google.com/file/d/13wv_E-Pw4LrBHDyRccPM6oQRz_qp0dzd/view?usp=sharing)

## Setup Instructions

1. Clone the repository:

   ```
   git clone <repository_url>
   cd <repository_folder>
   ```

2. (Optional) Create and activate a Python virtual environment:

   ```
   python -m venv env
   source env/bin/activate      # On Windows: env\Scripts\activate
   ```

3. Install required packages:

   ```
   pip install torch transformers
   ```

4. Run the chatbot interface:

   ```
   python interface.py
   ```

## How to Use

- Type messages into the terminal.
- The bot answers questions from the FAQ instantly or generates replies otherwise.
- To exit the chatbot, type `/exit`.

### Sample Interaction

```
User: Hello
Bot: Hi! How can I help you today?

User: What is the capital of France?
Bot: The capital of France is Paris.

User: And Italy?
Bot: The capital of Italy is Rome.

User: /exit
Exiting chatbot. Goodbye!
```

## Features

- FAQ knowledge base for fast answers on common questions.
- Maintains short-term chat history by concatenating tokenized conversation turns.
- Uses DialoGPT-medium with sampling techniques for varied and natural responses.
- Modular code for easy maintenance and scalability.

## Future Work

- Improve understanding of complex or grammatical questions.
- Optimize memory window size for better contextual awareness.
- Enhance tone consistency and error handling.

