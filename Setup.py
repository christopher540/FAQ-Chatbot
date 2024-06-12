import streamlit as st
import tempfile
import os
import sqlite3
    
conn=sqlite3.connect('User_Files.db',timeout=10)
cursor=conn.cursor()

def addInfo(a,b,c,d):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS REGISTRATIONS (
        SURNAME TEXT(50),
        GIVEN_NAME TEXT(50),
        CV_PATH TEXT(50),
        FNQ_PATH TEXT(50)
        )
        """
    )
    cursor.execute("INSERT INTO REGISTRATION VALUES (?,?,?,?)",(a,b,c,d))
    conn.commit()
    conn.close()
    st.success("User has been added to the database")

st.title('Smart FAQ Setup')
st.subheader('Please Upload your CV and Excel File (List of QnA)', divider='gray')


with st.form (key="Registration Form"):
    Surname=st.text_input('Enter your surname')
    Given_name=st.text_input('Enter your given name')
    uploaded_files = st.file_uploader("Drag and Drop your files here", accept_multiple_files=True)

    for uploaded_file in uploaded_files:
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, uploaded_file.name)
        file_extension = os.path.splitext(path)[1]
        
        if str(file_extension)=='.pdf':
            CV_path=path
        elif str(file_extension)=='.xlsx':
            FAQ_list=path
    submit=st.form_submit_button(label='Register')

    if submit==True:
        st.success('Your registration is successful')
        addInfo(Surname,Given_name,CV_path,FAQ_list)










