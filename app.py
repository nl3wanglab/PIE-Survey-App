from flask import Flask, render_template, request, jsonify, url_for
import questions
import os
import xlsxwriter

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def home():
    options = [
        {
            'label': "Children's Behavior Questionnaire",
            'url': 'Childrens_Behavior_Questionnaire'
        },
    ]

    return render_template('home.html', options=options)

@app.route('/<quiz_type>')
def quiz_type(quiz_type):
    questions_dict = questions.get_questions_Childrens_Behavior_Questionnaire()
    #questions_dict = questions.get_questions(f'Quizzes/{quiz_type}.xlsx', 'questions')
    return render_template(f'{quiz_type}/home.html', questions=questions_dict, quiz_type=quiz_type)

@app.route('/submit/Childrens_Behavior_Questionnaire', methods=['POST'])
def submit_cbq():
    data = request.get_json()

    subjectNo = data['subjectNo']
    patientName = data['patientName']
    patientGender = data['patientGender']
    dob = data['dob']
    dateTime = data['dateTime']
    childAgeOutput = data['childAgeOutput']
    quizData = {int(k): int(v) for k, v in data['quizData'].items()}

    questions_dict = questions.get_questions_Childrens_Behavior_Questionnaire()

    filename = 'static/saves/' + dateTime + '.xlsx'
    workbook = xlsxwriter.Workbook(filename, {'nan_inf_to_errors': True})
    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold': True})

    worksheet.write('A1', 'subjectNo', bold)
    worksheet.write('A2', subjectNo)

    worksheet.write('B1', 'patientName', bold)
    worksheet.write('B2', patientName)

    worksheet.write('C1', 'patientGender', bold)
    worksheet.write('C2', patientGender)

    worksheet.write('D1', 'dob', bold)
    worksheet.write('D2', dob)

    worksheet.write('E1', 'dateTime', bold)
    worksheet.write('E2', dateTime)

    worksheet.write('F1', 'Child Age', bold)
    worksheet.write('F2', childAgeOutput)

    worksheet.write('A5', 'QUESTION', bold)
    worksheet.write('B5', 'QUESTION #', bold)
    worksheet.write('C5', 'QUESTION ANSWER', bold)
    worksheet.write('D5', 'REVERSE', bold)
    worksheet.write('E5', 'CBQ_SCALE_CAT', bold)

    for i, (question_number, answer) in enumerate(quizData.items(), start=6):
        question_number_int = int(question_number)
        question_data = questions_dict.get(question_number_int, {'question_prompt': 'Question Not Found', 'reverse': 'N/A', 'cbq_scale_cat': 'N/A'})
        question = question_data['question_prompt']
        worksheet.write(f'A{i}', question)
        worksheet.write(f'B{i}', question_number)
        worksheet.write(f'C{i}', answer)
        worksheet.write(f'D{i}', question_data['reverse'])
        worksheet.write(f'E{i}', question_data['cbq_scale_cat'])

    types = ['AL', 'AN', 'AP', 'AF', 'AS', 'DS', 'SO', 'FE', 'HP', 'IM', 'IC', 'LP', 'SE', 'SD', 'SH', 'SL', '---old---']

    results = {}
    for type in types:
        results[type] = {
            'sum': 0,
            'scale': 0,
            'numerical_responses': 0,
        }

    for question_num, question_data in questions_dict.items():
        question_type = question_data['cbq_scale_cat']
        question_reverse_bool = question_data['reverse'] == 'R'
        results[question_type]['scale'] += 1
        if question_num in quizData and quizData[question_num] != -1:
            question_response = quizData[question_num]
            if question_reverse_bool:
                question_response = 8 - question_response
            results[question_type]['sum'] += question_response
            results[question_type]['numerical_responses'] += 1

    worksheet.write(f'H5', "CBQ_SCALE_CATEGORY", bold)
    worksheet.write(f'I5', "SUM", bold)
    worksheet.write(f'J5', "SCALE", bold)
    worksheet.write(f'K5', "NUMERICAL RESPONSES", bold)
    worksheet.write(f'L5', "SUM / NUMERICAL RESPONSES", bold)
    row = 6  # starting row
    for type in types:
        if type in results:
            sum_divided_by_numerical_responses = results[type]['sum'] / results[type]['numerical_responses'] if results[type]['numerical_responses'] > 0 else 'DIV/0!'
            worksheet.write(f'H{row}', type)
            worksheet.write(f'I{row}', results[type]['sum'])
            worksheet.write(f'J{row}', results[type]['scale'])
            worksheet.write(f'K{row}', results[type]['numerical_responses'])
            worksheet.write(f'L{row}', sum_divided_by_numerical_responses)
            row += 1

    workbook.close()

    url_to_go = url_for('results_cbq')

    return jsonify({'success': True, 'excel': url_for('static', filename=filename), 'redirect': url_to_go})

@app.route('/result/Childrens_Behavior_Questionnaire')
def results_cbq():
    return render_template(f'Childrens_Behavior_Questionnaire/result.html')

if __name__ == '__main__':
    app.run(debug=True)
