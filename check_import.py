try:
    import adk
    print("adk imported")
except ImportError as e:
    print(f"adk failed: {e}")

try:
    import google.adk
    print("google.adk imported")
except ImportError as e:
    print(f"google.adk failed: {e}")

try:
    import google_adk
    print("google_adk imported")
except ImportError as e:
    print(f"google_adk failed: {e}")
