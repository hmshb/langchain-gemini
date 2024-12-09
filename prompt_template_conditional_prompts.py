# LangChain + Google Gemini AI Integration Example
# Author: Hassan Mehmood
# Demonstrates This is the example of prompt template with conditional prompts.

from gemini import GoogleGeminiModel

def main():
    # Define the prompt template for extracting key facts
    template = """You are a helpful assistant. When I ask you about {topic}, give me a {response_type} answer.
    For example, if the topic is 'math', give me a detailed explanation. If the topic is 'history', give me a brief summary."""

    # Initialize the GoogleGeminiModel instance
    gemini_model = GoogleGeminiModel()

    # topic = "math"
    # response_type = "detailed"

    topic = "history"
    response_type = "brief"

    # Execute the chain using the defined prompt and input text
    print(f"🌍 Executing the chain for the input: Topic: {topic}, Response Type: {response_type}")
    response = gemini_model.execute_chain(prompt_template=template, input_text={"topic": topic, "response_type": response_type}, input_variables=["topic", "response_type"])

    # Display the result
    print("============================================")
    print(f"🌟 Response Result: {response}")
    print("============================================")

if __name__ == "__main__":
    main()