from flask import render_template, request

from models import Person

def register_routes(app, db):

    @app.route('/', methods = ['GET', "POST"])
    def index():
        if request.method == "GET":
            people = Person.query.all()
            return render_template('index.html', people= people)
        elif request.method == "POST":
            name = request.form.get('name')
            age = int(request.form.get('age'))
            job = request.form.get('job')

            person = Person(name=name, age=age, job=job)

            db.session.add(person)
            db.session.commit()

            people = Person.query.all()
            return render_template('index.html', people=people)
    
    @app.route('/delete/<paid>', methods= ['DELETE'])
    def delete(paid):
        Person.query.filter(Person.paid == paid).delete()
        db.session.commit()

        people = Person.query.all()
        return render_template('index.html', people =people)
    
    @app.route("/details/<paid>", methods = ['GET'])
    def details(paid):
        person  = Person.query.filter(Person.paid == paid ).first()
        return render_template("details.html", person= person)