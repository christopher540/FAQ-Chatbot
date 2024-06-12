import pandas as pd

df=pd.read_excel('FAQ list.xlsx')


def generate_intro():
    intro=''
    questions=[]
    for i in range(df.shape[0]):
        questions.append(df.iloc[i,0])
    
    for num,question in enumerate(questions):
        intro+=str(num+1)+'. '+question+'\n'

    
    intro+='C. To talk to the Smart ChatBot'
    return intro

def generate_answer_faq(n):
    return df.iloc[n-1,1]
