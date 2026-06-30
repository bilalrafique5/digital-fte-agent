import os
from langchain_google_genai import ChatGoogleGenerativeAI
from agents.utils import extract_text

llm=ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.4
)

def plan_content(topic:str, platform:str) -> str:
    prompt=f"""You are a content strategist. Create a brief content strategy 
for a {platform} post about: "{topic}"

Include:
- Target audience
- Tone (professional/casual/etc)
- Key message
- Call to action

Keep it concise, 3-4 lines."""

    response=llm.invoke(prompt)
    return extract_text(response)
