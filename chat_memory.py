import torch

# --- FAQ Knowledge Base ---
faq_knowledge_base = {
    "what is the capital of afghanistan": "The capital of Afghanistan is Kabul.",
    "what is the capital of australia": "The capital of Australia is Canberra.",
    "what is the capital of brazil": "The capital of Brazil is Brasília.",
    "what is the capital of canada": "The capital of Canada is Ottawa.",
    "what is the capital of china": "The capital of China is Beijing.",
    "what is the capital of france": "The capital of France is Paris.",
    "what is the capital of germany": "The capital of Germany is Berlin.",
    "what is the capital of india": "The capital of India is New Delhi.",
    "what is the capital of indonesia": "The capital of Indonesia is Jakarta.",
    "what is the capital of italy": "The capital of Italy is Rome.",
    "what is the capital of japan": "The capital of Japan is Tokyo.",
    "what is the capital of mexico": "The capital of Mexico is Mexico City.",
    "what is the capital of nepal": "The capital of Nepal is Kathmandu.",
    "what is the capital of netherlands": "The capital of the Netherlands is Amsterdam.",
    "what is the capital of pakistan": "The capital of Pakistan is Islamabad.",
    "what is the capital of russia": "The capital of Russia is Moscow.",
    "what is the capital of saudi arabia": "The capital of Saudi Arabia is Riyadh.",
    "what is the capital of south africa": "South Africa has three capitals: Pretoria, Bloemfontein, and Cape Town.",
    "what is the capital of south korea": "The capital of South Korea is Seoul.",
    "what is the capital of spain": "The capital of Spain is Madrid.",
    "what is the capital of sri lanka": "The capital of Sri Lanka is Sri Jayawardenepura Kotte.",
    "what is the capital of thailand": "The capital of Thailand is Bangkok.",
    "what is the capital of turkey": "The capital of Turkey is Ankara.",
    "what is the capital of ukraine": "The capital of Ukraine is Kyiv.",
    "what is the capital of united arab emirates": "The capital of UAE is Abu Dhabi.",
    "what is the capital of united kingdom": "The capital of the United Kingdom is London.",
    "what is the capital of united states": "The capital of the United States is Washington, D.C.",
    "what is the capital of vietnam": "The capital of Vietnam is Hanoi.",
    "what is the capital of zimbabwe": "The capital of Zimbabwe is Harare.",

    "which countries are in the north of india": "To the north of India are China, Nepal and Bhutan.",
    "which countries are in the northwest of india": "To the northwest of India are Pakistan and Afghanistan.",
    "which countries are in the east of india": "To the east of India are Bangladesh and Myanmar.",
    "which countries are in the south east of india": "The southeastern neighbours of India include Myanmar and Indonesia.",
    "which countries are in the west of india": "To the west of India are Pakistan and Afghanistan.",
    "which countries share land borders with india": "India shares land borders with Afghanistan, Bangladesh, Bhutan, China, Myanmar, Nepal, Pakistan, and Sri Lanka.",
    "which countries share maritime borders with india": "India shares maritime borders with Sri Lanka and the Maldives.",
    "what is the capital of nepal": "The capital of Nepal is Kathmandu.",
    "what is the capital of bhutan": "The capital of Bhutan is Thimphu.",
    "what is the capital of bangladesh": "The capital of Bangladesh is Dhaka.",
    "what is the capital of myanmar": "The capital of Myanmar is Naypyidaw.",
    "what is the capital of pakistan": "The capital of Pakistan is Islamabad.",
    "what is the capital of sri lanka": "The capital of Sri Lanka is Sri Jayawardenepura Kotte.",

    "what ocean is south of india": "The Indian Ocean lies to the south of India.",
    "which seas surround india": "The Arabian Sea is to the west and the Bay of Bengal is to the east of India.",
    "how many neighbours does india have": "India has 7 land neighbours and 2 maritime neighbours making 9 in total.",
}

def query_faq_kb(user_input):
    normalized = user_input.lower().strip().rstrip('?.!')
    return faq_knowledge_base.get(normalized, None)
