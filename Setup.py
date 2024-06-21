import streamlit as st
import tempfile
import os
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='lol123',
    database='user_files'
)

cursor=mydb.cursor()

def addInfo(a,b,c,d):

    cursor.execute("INSERT INTO USER VALUES (%s,%s,%s,%s)",(a,b,c,d))
    
    
    
    mydb.commit()
    st.success("User has been added to the database")

def save_file(file):
    folder="C:/Users/chris/OneDrive/Documents/Python Projects/FAQ BOT/store"
    with open(os.path.join(folder,file.name),'wb') as f:
        f.write(file.getbuffer())
    
    return os.path.join(folder,file.name)


st.title('Smart FAQ Setup')
st.subheader('Please Upload your CV and Excel File (List of QnA)', divider='gray')


with st.form (key="Registration Form"):
    Surname=st.text_input('Enter your surname')
    Given_name=st.text_input('Enter your given name')
    uploaded_files = st.file_uploader("Drag and Drop your files here", accept_multiple_files=True)

    for uploaded_file in uploaded_files:
        path=save_file(uploaded_file)
        file_extension = os.path.splitext(path)[1]
        
        if str(file_extension)=='.pdf':
            CV_path=path
        elif str(file_extension)=='.xlsx':
            FAQ_list=path
    submit=st.form_submit_button(label='Register')

    if submit==True:
        st.success('Your registration is successful')
        addInfo(Surname,Given_name,CV_path,FAQ_list)

mydb.close()









