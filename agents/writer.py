import os
from langchain_google_genai import ChatGoogleGenerativeAI
from agents.utils import extract_text

llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7
)

def write_content(topic:str , platform:str , strategy:str) -> str:
    prompt=f"""Based on this content strategy:
{strategy}

Write a {platform} post about: "{topic}"

Rules:
- Match {platform}'s typical style and length
- Include a strong hook in the first line
- Add relevant hashtags at the end (3-5 max)
- Make it engaging and natural, not robotic"""
    response=llm.invoke(prompt)
    return extract_text(response)