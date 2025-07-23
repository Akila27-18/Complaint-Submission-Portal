
from flask import Flask, render_template, redirect, url_for, request
from config import Config
from models import db, Complaint
from forms import ComplaintForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ComplaintForm()
    if form.validate_on_submit():
        complaint = Complaint(name=form.name.data, message=form.message.data)
        db.session.add(complaint)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.route('/admin')
def admin():
    complaints = Complaint.query.all()
    total = Complaint.query.count()
    resolved = Complaint.query.filter_by(resolved=True).count()
    return render_template('admin.html', complaints=complaints, total=total, resolved=resolved)

@app.route('/resolve/<int:id>')
def resolve(id):
    complaint = Complaint.query.get_or_404(id)
    complaint.resolved = True
    db.session.commit()
    return redirect(url_for('admin'))

@app.route('/delete/<int:id>')
def delete(id):
    complaint = Complaint.query.get_or_404(id)
    db.session.delete(complaint)
    db.session.commit()
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
