
# #import google.generativeai as genai
# import google.genai as genai


# def extract_data(opportunity):
#     prompt = f"""
#     Extract structured info from this opportunity:
#     Title: {opportunity['title']}
#     Link: {opportunity['link']}
#     Return JSON with fields: program_name, organization, country, deadline, eligibility, funding, category, description, tags
#     """
#     model = genai.GenerativeModel("gemini-1.5-pro")
#     response = model.generate_content(prompt)
#     return response.text

# from google import genai


# def extract_data(opportunity):
#     prompt = f"""
#     Extract structured info from this opportunity:
#     Title: {opportunity['title']}
#     Link: {opportunity['link']}
#     Return JSON with fields: program_name, organization, country, deadline, eligibility, funding, category, description, tags
#     """

#     # Model call
#     response = client.models.generate_content(
#         model="gemini-1.5-pro",
#         contents=prompt
#     )

#     return response.text


from google import genai
import os
from dotenv import load_dotenv

# load .env file
load_dotenv()

# API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

# Client initialization
client = genai.Client(api_key=API_KEY)

def extract_data(opportunity):
    prompt = f"""
    Extract structured info from this opportunity:
    Title: {opportunity['title']}
    Link: {opportunity['link']}

    Return JSON with fields:
    program_name, organization, country, deadline, eligibility,
    funding, category, description, tags
    """

    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=prompt
    )

    return response.text