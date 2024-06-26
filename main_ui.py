import streamlit as st
import gradio as gr
import os
import mysql.connector
import subprocess
import time


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='lol123',
    database='user_files'
    )

cursor = mydb.cursor()

st.image("Logo.png")

def check_valid(SURNAME, GIVEN_NAME):
        query = """
            SELECT *
            FROM USER AS U
            WHERE U.SURNAME = %s AND U.GIVEN_NAME = %s
        """
        cursor.execute(query, (SURNAME, GIVEN_NAME))

        if cursor.fetchone():
            return True
        else:
            return False

def find_person():
    with st.form (key="Registration Form"):
        Surname=st.text_input('Enter your surname')
        Given_name=st.text_input('Enter your given name')
        submit=st.form_submit_button(label='Log in')

        if submit==True:
            if check_valid(Surname,Given_name)==True:
                st.success('Person found!')
                query = """
                SELECT CV_PATH,FAQ_PATH
                FROM USER AS U
                WHERE U.SURNAME = %s AND U.GIVEN_NAME = %s
                        """

                cursor.execute(query,(Surname,Given_name))
                results=cursor.fetchall()
                cv_path=results[0][0]
                faq_path=results[0][1]
                paths=cv_path+','+faq_path
                with open("paths.txt", "w") as file1:
                    # Writing data to a file
                    file1.write(paths)
                
                with open('count.txt','r+') as f:
                    a = f.read()
                    if a:
                        a = int(a)
                    else:
                        a = -1
                    a += 1
                    a = str(a)
                    f.seek(0)
                    f.write(a)
                    f.truncate()
                    
                 
                
                subprocess.Popen(['python','gradio_ui.py'])        
            else:
                st.error('Person is not registered', icon="🚨")
                time.sleep(2)
                st.rerun()
    
    
def chatbot():
    time.sleep(7)
    st.title("Chat with a bot")
    # Display Streamlit content
    # Replace the Gradio interface URL with your generated share link
    
    with open('count.txt','r') as f:
        count=f.read()
    
    gradio_interface_url = "http://127.0.0.1:786"+count  # Example URL

    # Load the Gradio interface using an iframe
    st.write(f'<iframe src="{gradio_interface_url}" width="720" height="1080"></iframe>',
            unsafe_allow_html=True) 


pages = {
    "Find Person": find_person,
    "Chatbot": chatbot,
    
}


st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(pages.keys()))

pages[selection]()


