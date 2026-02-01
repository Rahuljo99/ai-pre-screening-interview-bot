from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

from openai import api_key 
from backend.app.schemas import ResumeSchema

async def resume_extractor(resume_text: str) -> ResumeSchema:
    load_dotenv()
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        print(f"DEBUG: GOOGLE_API_KEY found? {bool(api_key)}")
    except KeyError:
        raise KeyError("GOOGLE_API_KEY not found in environment variables.")

    llm = ChatGoogleGenerativeAI(
        model = "gemini-2.5-flash",
        temperature=0,
        api_key=os.getenv("GOOGLE_API_KEY")
    )

    structured_llm = llm.with_structured_output(ResumeSchema)
    prompt = f"""
        You are an expert HR professional skilled in extracting structured information from resumes.
        Given the following resume text, extract the relevant details and format them according to the ResumeSchema.
        Resume Text:
        {resume_text}
    """
    response = structured_llm.invoke(prompt)
    return response
