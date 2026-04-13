from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
import os
import sqlite3
import joblib
import numpy as np
from fpdf import FPDF
import io

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a random secret key

base_dir = os.path.dirname(os.path.abspath(__file__))

# Load the model
model_path = os.path.join(base_dir, 'Cardiovascular-Disease Prediction', 'HEART_DISEASE_MODEL.joblib')
model = joblib.load(model_path)

def init_db():
    db_path = os.path.join(base_dir, 'evaluation.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS registration
                 (Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT, Gender TEXT, age TEXT, password TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db_path = os.path.join(base_dir, 'evaluation.db')
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('SELECT * FROM registration WHERE username = ? AND password = ?', (username, password))
        result = c.fetchone()
        conn.close()
        
        if result:
            session['username'] = username
            return redirect(url_for('predict'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        address = request.form['address']
        username = request.form['username']
        email = request.form['email']
        phoneno = request.form['phoneno']
        gender = request.form['gender']
        age = request.form['age']
        password = request.form['password']
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Password and Confirm Password do not match')
            return redirect(url_for('register'))

        db_path = os.path.join(base_dir, 'evaluation.db')
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('INSERT INTO registration VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                  (fullname, address, username, email, phoneno, gender, age, password))
        conn.commit()
        conn.close()
        
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Get form data
        username = session['username']
        age = float(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])
        
        # Prepare input for model
        inputs = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        
        try:
            # Predict
            prediction = model.predict([inputs])[0]
            
            # Generate report text
            if prediction == 1:
                result_text = "Abnormality Detected! Report is Generated"
                report_text = "\n As per input data Heart Abnormality Detected."
                text_color = 'red'
            else:
                result_text = "No Abnormality Detected. Report is Generated"
                report_text = "\n As per input data No Heart Disease Detected\n\nRelax and Follow below mentioned Lifestyle Changes:\n\n1. Eat a healthy diet\n2. Regular exercise\n3. Maintain a healthy weight\n4. Quit smoking\n5. Limit alcohol consumption\n6. Manage stress\n7. Get enough sleep\n8. Regular health check-ups"
                text_color = 'green'
            
            # Generate PDF
            try:
                pdf_filename = generate_pdf_report(report_text, username, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, text_color)
            except Exception as e:
                pdf_filename = None
                flash(f'PDF generation failed: {str(e)}')
            
            return render_template('result.html', result=result_text, pdf_path=pdf_filename, color=text_color)
        except Exception as e:
            flash(f'Error in prediction: {str(e)}')
            return redirect(url_for('predict'))
    
    return render_template('predict.html', username=session['username'])

def generate_pdf_report(report_text, username, age, sex, chest_pain, trestbps, chol, fbs, rest_ecg, thalach, ex_ang, old_peak, slope, ca, thal, text_color):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.rect(5.0, 5.0, 200.0, 278.0)
    
    col_width = 60
    col_height = 8
    
    pdf.set_font("Arial", style='B', size=18)
    pdf.cell(0, 10, txt=f"Patient Report for {username}", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.set_draw_color(0, 0, 0)
    pdf.line(10, pdf.get_y(), 200 - 10, pdf.get_y())
    pdf.cell(0, 10, txt="", ln=True)
    
    pdf.cell(col_width, col_height, txt="Age:", ln=False)
    pdf.cell(col_width, col_height, txt=str(int(age)), ln=True)
    pdf.cell(col_width, col_height, txt="Sex:", ln=False)
    pdf.cell(col_width, col_height, txt='Female' if sex == 0 else 'Male', ln=True)
    pdf.cell(col_width, col_height, txt="Chest Pain:", ln=False)
    pdf.cell(col_width, col_height, txt='Typical' if chest_pain == 1 else 'Asymptomatic' if chest_pain == 2 else 'Non-typical', ln=True)
    pdf.cell(col_width, col_height, txt="Trestbps:", ln=False)
    pdf.cell(col_width, col_height, txt=f"{str(int(trestbps))} mm Hg", ln=True)
    pdf.cell(col_width, col_height, txt="Chol:", ln=False)
    pdf.cell(col_width, col_height, txt=f"{str(int(chol))} mg/dl", ln=True)
    pdf.cell(col_width, col_height, txt="FBS:", ln=False)
    pdf.cell(col_width, col_height, txt='True' if fbs == 1 else 'False', ln=True)
    pdf.cell(col_width, col_height, txt="RestECG:", ln=False)
    pdf.cell(col_width, col_height, txt='Normal' if rest_ecg == 0 else 'Having ST-T wave abnormality' if rest_ecg == 1 else 'Showing probable or definite left ventricular hypertrophy', ln=True)
    pdf.cell(col_width, col_height, txt="Thalach:", ln=False)
    pdf.cell(col_width, col_height, txt=str(int(thalach)), ln=True)
    pdf.cell(col_width, col_height, txt="ExANG:", ln=False)
    pdf.cell(col_width, col_height, txt='Yes' if ex_ang == 1 else 'No', ln=True)
    pdf.cell(col_width, col_height, txt="Old Peak:", ln=False)
    pdf.cell(col_width, col_height, txt=str(float(old_peak)), ln=True)
    pdf.cell(col_width, col_height, txt="Slope:", ln=False)
    pdf.cell(col_width, col_height, txt='Fixed' if slope == 1 else 'Normal' if slope == 2 else 'Reversible', ln=True)
    pdf.cell(col_width, col_height, txt="Ca:", ln=False)
    pdf.cell(col_width, col_height, txt=str(int(ca)), ln=True)
    pdf.cell(col_width, col_height, txt="Thal:", ln=False)
    pdf.cell(col_width, col_height, txt='Fixed' if thal == 1 else 'Normal' if thal == 2 else 'Reversible' if thal == 3 else 'Asymptomatic', ln=True)
    
    pdf.cell(0, 10, txt="", ln=True)
    pdf.set_font("Arial", size=14, style='B')
    pdf.cell(col_width * 3, col_height, txt="Conclusions:", ln=True)
    pdf.set_font("Arial", size=12)
    
    conclusions = []
    if int(age) > 50:
        conclusions.append("Your age is above 50, which may increase the risk of heart disease. Ensure regular check-ups and maintain a healthy lifestyle to mitigate risks.")
    if float(chol) > 200:
        conclusions.append("Your cholesterol level is higher than the normal range (200 mg/dl). To reduce cholesterol, consider a low-cholesterol diet, regular exercise, and medication if prescribed by your doctor.")
    if fbs == 1:
        conclusions.append("Your fasting blood sugar level is higher than normal. Control sugar intake, exercise regularly, and consult your doctor for further evaluation.")
    
    for conclusion in conclusions:
        pdf.multi_cell(col_width * 3, col_height, txt=conclusion)
    
    if text_color == 'red':
        pdf.set_text_color(255, 0, 0)
    elif text_color == 'green':
        pdf.set_text_color(0, 128, 0)
    
    pdf.multi_cell(col_width * 3, col_height, txt=report_text, align='C')
    
    folder_path = os.path.join(base_dir, 'patient-report')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    pdf_filename = os.path.join(folder_path, f"{username}_Report.pdf")
    pdf.output(pdf_filename)
    return pdf_filename

@app.route('/download/<path:filename>')
def download_file(filename):
    try:
        folder_path = os.path.join(base_dir, 'patient-report')
        safe_path = os.path.join(folder_path, os.path.basename(filename))
        return send_file(safe_path, as_attachment=True)
    except Exception as e:
        return f"Error downloading file: {str(e)}"

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=10000)