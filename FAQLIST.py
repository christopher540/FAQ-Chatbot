import pandas as pd



def generate_intro(faq):
    df=pd.read_excel(faq)
    intro=''
    questions=[]
    for i in range(df.shape[0]):
        questions.append(df.iloc[i,0])
    
    for num,question in enumerate(questions):
        intro+=str(num+1)+'. '+question+'\n'

    
    intro+='\n'+'You could also ask any question and our Chatbot will be happy to answer it!'
    return intro

def generate_answer_faq(n,faq):
    df=pd.read_excel(faq)
    return df.iloc[n-1,1]
