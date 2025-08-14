from google.generativeai import configure, GenerativeModel

# Configure with your API key
configure(api_key=" ")

# Initialize the model
model = GenerativeModel('gemini-1.5-flash')

# Ask the user for input
user_question = input("Ask a question: ")

# Get response from Gemini
response = model.generate_content(user_question)

# Print the AI's answer
print("\nGemini says:", response.text)
