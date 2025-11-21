import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Ensure we can import google.adk
# (Assuming it's installed in the environment we are running this in)

try:
    from google.adk import Agent
    from google.adk.models import Gemini
except ImportError:
    print("Error: google-adk not found. Please install it via 'pip install google-adk'.")
    sys.exit(1)

# Define the Anonymizer Agent
# We can inherit from Agent or just instantiate it.
# For a template, we'll define a function to create it.

def create_anonymizer_agent(model_name="gemini-1.5-flash"):
    """
    Creates the Anonymizer Agent (Agent 1).
    This agent is responsible for identifying and redacting PII from the input text.
    """
    
    # Initialize the model
    # Note: GOOGLE_API_KEY must be set in environment variables
    model = Gemini(model=model_name)

    # Define the prompt for the agent
    anonymizer_prompt = """
    You are an expert Data Privacy Officer.
    Your task is to anonymize the given text by replacing Personally Identifiable Information (PII)
    with unique placeholders (e.g., [NAME_1], [EMAIL_1], [PHONE_1]).
    
    Output a JSON object with two fields:
    1. 'anonymized_text': The text with PII redacted.
    2. 'mapping': A dictionary mapping the placeholders back to the original values.
    
    Example Input: "Contact John Doe at john@example.com"
    Example Output:
    {
        "anonymized_text": "Contact [NAME_1] at [EMAIL_1]",
        "mapping": {
            "[NAME_1]": "John Doe",
            "[EMAIL_1]": "john@example.com"
        }
    }
    """

    # Create the agent
    # Correct arguments based on inspection: name, model, instruction
    agent = Agent(name="Anonymizer", model=model, instruction=anonymizer_prompt)
    
    return agent

if __name__ == "__main__":
    print("Initializing Anonymizer Agent...")
    
    # Check for API Key
    if "GOOGLE_API_KEY" not in os.environ:
        print("WARNING: GOOGLE_API_KEY not set. Agent might fail.")
    
    try:
        agent1 = create_anonymizer_agent()
        print("Agent 1 (Anonymizer) created successfully.")
        
        # Test run (optional, commented out until we have a key)
        # input_text = "Hello, my name is Alice."
        # response = agent1.run(input_text)
        # print("Response:", response)
        
    except Exception as e:
        print(f"Failed to create agent: {e}")
