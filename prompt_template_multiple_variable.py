# LangChain + Google Gemini AI Integration Example
# Author: Hassan Mehmood
# Demonstrates This is the example of prompt template with multiple variables.

from gemini import GoogleGeminiModel

def main():
    # Define the text to process (could be any input for translation or extraction)
    word_to_translate = """LangChain provides a modular framework for developing applications with large language models. It allows developers to chain together tools, handle memory, and use different models to create more powerful solutions. LangChain has been used for building chatbots, document analysis tools, and other AI-powered applications."""

    # Define the prompt template for extracting key facts
    template = "Extract {action} from the following text: {text}. Provide a list of the most important points."

    # Initialize the GoogleGeminiModel instance
    gemini_model = GoogleGeminiModel()

    # Execute the chain using the defined prompt and input text
    print(f"🌍 Executing the chain for the input: {word_to_translate}")
    response = gemini_model.execute_chain(prompt_template=template, input_text={"action": "3 facts", "text": word_to_translate}, input_variables=["action", "text"])

    # Display the result
    print("============================================")
    print(f"🌟 Response Result: {response}")
    print("============================================")

if __name__ == "__main__":
    main()