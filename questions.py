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
