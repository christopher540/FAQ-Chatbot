import gradio as gr
from groq_AI import generate_response
from FAQLIST import generate_intro,generate_answer_faq
import pandas as pd
import time
import mysql.connector
import os

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='lol123',
    database='user_files'
    )

cursor = mydb.cursor()

#Chat generation
def respond(message, chat_history,config):
        cv = config['cv']
        faq = config['faq']
        if message.isnumeric():
              bot_message=generate_answer_faq(int(message),faq)
              chat_history.append((message,bot_message))
        elif message=='C' or message=='c':
            bot_message = 'Hi this is Tap smart smart robot speaking, how can I help you'
            chat_history.append((message, bot_message))
        else:
            bot_message = generate_response(message,cv)
            chat_history.append((message, bot_message))
        
        time.sleep(2)
        return "", chat_history

#Welcoming Message
def initial_msg(faq):
    intro=generate_intro(faq)
    initial_message = [("Chatbot", "Welcome! Here are some frequently aksed questions"+'\n'+
                        intro
                        )]
    return initial_message

#Front UI
cv_path=''
faq_path=''
with gr.Blocks() as demo:
    with open("paths.txt", "r+") as file1:
        paths=file1.read().split(',')
        cv_path=paths[0]
        faq_path=paths[1]
    data_json={'cv': cv_path, 'faq': faq_path}
    config = gr.State(data_json)

    chatbot = gr.Chatbot(value=initial_msg('FAQ list.xlsx'))
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])  
    msg.submit(respond, [msg, chatbot,config], [msg, chatbot])

demo.launch()
