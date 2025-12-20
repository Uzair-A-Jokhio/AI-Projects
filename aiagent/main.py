import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import sys
from functions.get_files_info import get_files_info

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        print("I need prompt!")
        sys.exit(1)

    verbose_flag = False

    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True
        
    prompt = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=messages,
    )

    print(response.text)
    if response is None or response.usage_metadata is None:
        print("Response is malformed")
    if verbose_flag:
        print(f"User Prompt: {prompt}")
        print(f"Prompts tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens:{response.usage_metadata.candidates_token_count}")

main()