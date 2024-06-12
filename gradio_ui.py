import gradio as gr
import random
import time
from groq_AI import generate_response
from FAQLIST import generate_intro,generate_answer_faq
import pandas as pd

#Chat generation
def respond(message, chat_history):
        if message.isnumeric():
              bot_message=generate_answer_faq(int(message))
              chat_history.append((message,bot_message))
        elif message=='C' or message=='c':
            activate=True
            bot_message = 'Hi this is Tap smart smart robot speaking, how can I help you'
            chat_history.append((message, bot_message))
        else:
            bot_message = generate_response(message)
            chat_history.append((message, bot_message))
        
        time.sleep(2)
        return "", chat_history

#Welcoming Message
intro=generate_intro()
initial_message = [("Chatbot", "Welcome! Here are some frequently aksed questions"+'\n'+
                    intro
                    )]

#Front UI
with gr.Blocks() as demo:
    chatbot = gr.Chatbot(value=initial_message)
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])  
    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()
