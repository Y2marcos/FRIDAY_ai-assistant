# Create a test file: test_imports.py
try:
    from dotenv import load_dotenv
    from livekit import agents
    from livekit.agents import function_tool
    import pyautogui
    import requests
    print("✅ All dependencies installed successfully!")
except ImportError as e:
    print(f"❌ Missing dependency: {e}")
