from flask import render_template, request, redirect, url_for
from models import Person

def register_routes(app, db):
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            people = Person.query.all()
            return render_template('index.html', people=people)
        elif request.method == 'POST':
            name = request.form.get('name')
            age = int(request.form.get('age'))
            job = request.form.get('job')
            
            person = Person(name=name, age=age, job=job)
            db.session.add(person)
            db.session.commit()
            
            return redirect(url_for('index'))
    
    @app.route('/delete/<int:pid>', methods=['DELETE'])
    def delete(pid):
        Person.query.filter_by(pid=pid).delete()
        db.session.commit()
        return '', 204  

    @app.route('/details/<int:pid>')
    def details(pid):
        person = Person.query.filter_by(pid=pid).first()
        return render_template('detail.html', person=person)
