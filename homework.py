from flask import Blueprint, request, render_template, redirect, url_for, current_app
from flask_login import login_required
from werkzeug.utils import secure_filename
import os

homework = Blueprint('homework', __name__)

@homework.route('/dashboard')
@login_required
def dashboard():
    files = os.listdir(current_app.config['UPLOAD_FOLDER'])
    return render_template('dashboard.html', files=files)

@homework.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files.get('pdf')
        if file and file.filename.endswith('.pdf'):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('homework.dashboard'))
    return render_template('upload.html')
