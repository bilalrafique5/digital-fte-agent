import os
from langchain_google_genai import ChatGoogleGenerativeAI
from agents.utils import extract_text

llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.2
)

def critique_and_refine(draft:str, platform:str) -> str:
    prompt=f"""Review this {platform} post:

{draft}

1. Give brief feedback (2-3 lines) on clarity, engagement, and tone.
2. Then provide an IMPROVED final version of the post.


Format your response EXACTLY like this:
FEEDBACK: <your feedback here>
FINAL_POST: <improved post here>"""
    response=extract_text(llm.invoke(prompt))

    feedback=""
    final_post=draft  #fallback

    if "FEEDBACK:" in response and "FINAL_POST:" in response:
        parts=response.split("FINAL_POST")
        feedback=parts[0].replace("FEEDBACK:","").strip()
        final_post=parts[1].lstrip(":").strip()
    return {"feedback": feedback, "final_post": final_post
    }