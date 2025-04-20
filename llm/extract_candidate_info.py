import requests
import os
from dotenv import load_dotenv

load_dotenv()

def extract_candidate_info(resume_text):
    api_key = os.getenv("OPENROUTER_API_KEY")

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    messages = [
        {"role": "system", "content": "You are an HR assistant."},
        {"role": "user", "content": f"""\
From this resume, extract the following:

- **Candidate Name**: 
- **Work Experience Summary**: 
- **Education Summary**: 
- **Key Skills Identified**: 
- **Relevant Keywords Matched**:

Resume:
{resume_text}
"""}]

    response = requests.post(url, headers=headers, json={"model": "openai/gpt-3.5-turbo", "messages": messages})
    response.raise_for_status()

    data = response.json()
    reply = data['choices'][0]['message']['content']
    return reply.strip()
