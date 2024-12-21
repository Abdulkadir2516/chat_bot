import ollama

def chat_with_ollama(prompt):
    # Ollama ile sohbet et
    response = ollama.chat(model='llama3.2:1b', messages=[
        {"role": "system","content": "Introduce yourself as a storyteller for children."},
        {"role": "user", "content": prompt}
    ])

    # Yanıtı kontrol et
    #print("API Yanıtı:", response)

    # Yanıtın içeriğini döndür
    if hasattr(response, "message") and hasattr(response.message, "content"):
        return response.message.content
    else:
        return "Beklenmeyen bir yanıt alındı."


def main():
    print("Ollama Chatbot'a hoş geldiniz! (Çıkmak için 'exit' yazın)")
    while True:
        user_input = input("Sen: ")
        if user_input.lower() == 'exit':
            print("Görüşmek üzere!")
            break
        response = chat_with_ollama(user_input)
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
