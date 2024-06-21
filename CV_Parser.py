# importing required modules 
from pypdf import PdfReader 
from groq import Groq

# creating a pdf reader object

def profile_summary(cv):
    reader = PdfReader(cv) 

    # getting a specific page from the pdf file 
    page = reader.pages[0] 

    # extracting text from page 
    text = page.extract_text() 

    client = Groq(
        api_key='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'
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Summarize this person's cv and highlight the key informations: "+text,
            }
        ],
        model="llama3-8b-8192",
    )

    summary=chat_completion.choices[0].message.content
    return summary

