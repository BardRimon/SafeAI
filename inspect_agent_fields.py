from google.adk import Agent
try:
    print(Agent.model_fields.keys())
except Exception as e:
    print(f"Could not print model_fields: {e}")
