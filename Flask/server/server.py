from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_company_names', methods=['GET'])
def get_company_names():
    response = jsonify({
        'companies': util.get_company_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/salary', methods=['POST'])
def predict_salary_price():
    company= request.form['company']
    title = request.form['title']
    experience = int(request.form['experience'])

    response = jsonify({
        'salary': util.get_estimated_salary(company,title,experience)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Salary Prediction...")
    #util.load_saved_artifacts()
    app.run()
