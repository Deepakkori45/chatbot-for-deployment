import openai
import logging

# Set your OpenAI API key
openai.api_key = "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"

# Set up logging to store responses
logging.basicConfig(filename='chatbot_logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def chat_with_gpt(prompt):
    try:
        # Use GPT-4 (GPT-4 mini model) for chat
        response = openai.Completion.create(
            model="gpt-4",  # You can specify "gpt-4" for GPT-4
            prompt=prompt,
            max_tokens=150
        )

        message = response.choices[0].text.strip()
        logging.info(f"User: {prompt}")
        logging.info(f"Bot: {message}")
        
        return message

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return "Sorry, there was an error processing your request."

if __name__ == "__main__":
    print("Chatbot is ready! Type 'exit' to end.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = chat_with_gpt(user_input)
        print(f"Bot: {response}")
