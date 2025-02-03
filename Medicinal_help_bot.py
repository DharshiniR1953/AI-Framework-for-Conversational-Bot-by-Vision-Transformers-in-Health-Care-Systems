from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "Replace with your openAI API key here"

client = OpenAI()

def get_openai_response(plant_name, user_query):
    prompt = f"You are an expert in medicinal plants. Provide detailed answers based on the identified plant.\n\nPlant Name: {plant_name}\nUser Query: {user_query}\n\nAnswer:"
    
    response = client.chat.completions.create(
        model="gpt-4",  # Use "gpt-3.5-turbo" if you want a cheaper option
        messages=[
            {"role": "system", "content": "You are a helpful assistant with expertise in medicinal plants."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    
    return response.choices[0].message.content.strip()

def main():
    print("Welcome to the Medicinal Plant Chatbot!")
    plant_name = input("Enter the identified plant name: ")
    
    while True:
        user_query = input("Ask a question about the plant (or type 'exit' to quit): ")
        if user_query.lower() == "exit":
            print("Goodbye!")
            break
        
        response = get_openai_response(plant_name, user_query)
        print("\nChatbot:", response, "\n")

if __name__ == "__main__":
    main()
