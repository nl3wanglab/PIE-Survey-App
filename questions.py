import pandas as pd

def get_questions_Childrens_Behavior_Questionnaire():
    df_questions = pd.read_excel('Quizzes/Childrens_Behavior_Questionnaire.xlsx', sheet_name='questions')
    questions_dict = {}
    
    for i, j in df_questions[['cbq_num', 'cbq_q', 'reverse', 'cbq_scale_cat']].iterrows():
        questions_dict[j['cbq_num']] = {
            "question_num": j['cbq_num'],
            "question_prompt": j['cbq_q'],
            "reverse": j['reverse'],
            "cbq_scale_cat": j['cbq_scale_cat']
            }
    
    return questions_dict

def get_questions_The_Child_Autism_Spectrum_Quotient_Questionnaire():
    df_questions = pd.read_excel('Quizzes/The_Child_Autism_Spectrum_Quotient_Questionnaire.xlsx', sheet_name='questions')
    questions_dict = {}
    
    for i, j in df_questions[['q_num', 'q_text', 'reverse']].iterrows():
        questions_dict[j['q_num']] = {
            "question_num": j['q_num'],
            "question_prompt": j['q_text'],
            "reverse": j['reverse'],
            }
        
    return questions_dict
