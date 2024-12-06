# LangChain + Google Gemini AI Integration Example
# Author: Hassan Mehmood
# Demonstrates how to integrate LangChain with Google Gemini AI for multilingual translation.

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# ============================================
# Load Environment Variables
# ============================================
load_dotenv()

print("🔑 Loading API Key...")

# Access Google Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ Missing Google Gemini API key. Please set it in the .env file.")

print("✅ API Key Loaded Successfully.")

# ============================================
# Prepare the LLM Model
# ============================================
print("🤖 Initializing the Google Gemini Model...")

# Initialize the Gemini Pro model
llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=api_key)

print("✅ Model Initialized Successfully.")

# ============================================
# Define Prompt and Chain
# ============================================
print("📝 Setting up the Prompt Template...")

# Define a prompt for translating text from English to Italian
prompt = PromptTemplate.from_template("You are an AI assistant. Translate {word} from English into Italian.")

print("🔗 Creating the LLM Chain...")

# Create a chain that combines the LLM and the prompt template
chain = prompt | llm

print("✅ Chain Setup Complete.")

# ============================================
# Execute the Chain
# ============================================
word_to_translate = "Hello, This is Hassan!"
print(f"🌍 Translating the word: {word_to_translate}")

print("📤 Sending the request to the Gemini AI Model...")
response = chain.invoke(input=word_to_translate)

print("✅ Response Received.")
print("============================================")
print(f"🌟 Translation Result: {response.content}")
print("============================================")
