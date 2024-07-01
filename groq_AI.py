from groq import Groq
from CV_Parser import profile_summary

client = Groq(
    api_key='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'
)

def generate_response(question,cv):
    summary=profile_summary(cv) #change later
    # Set the system prompt
    system_prompt = {
        "role": "system",
        "content":
        "You are a smart chatbot who will answer everything about this person, here is the summary: "+summary
    }

    # Initialize the chat history
    chat_history = [system_prompt]
  
    # Get user input from the console
    user_input = question

    # Append the user input to the chat history
    chat_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(model="llama3-70b-8192",
                                            messages=chat_history,
                                            max_tokens=100,
                                            temperature=1.2)
    # Append the response to the chat history
    chat_history.append({
        "role": "assistant",
        "content": response.choices[0].message.content
    })

    # Print the response
    return response.choices[0].message.content
