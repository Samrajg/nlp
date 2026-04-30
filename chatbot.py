def get_response(user_input):
    responses = {
        "hi": "Hello!",
        "hello": "Hi there!",
        "how are you": "I am fine!",
        "what is your name": "I am a simple chatbot.",
        "bye": "Goodbye!"
    }  
    return responses.get(user_input.lower(), "Sorry, I don't understand.")
def chatbot():
    print("Chatbot: Type 'bye' to exit") 
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)       
        if user_input.lower() == "bye":
            break
chatbot()
