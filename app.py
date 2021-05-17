from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///cruddatabse.db'
db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
   

    def __repr__(self):
        return '<task %r>' % self.id    

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=="POST":
        emp = request.form['content']
        new_employee = Employee(firstname=emp)
 
        try:
            db.session.add(new_employee)
            db.session.commit()
            return redirect('/')
        except:
            return "somethig went wrong......"    
    else:
        employees=Employee.query.all()        
        return render_template("index.html",employees=employees)


@app.route('/delete/<int:id>')
def delete(id):
    emp_delete = Employee.query.get(id)
        
    try:
        db.session.delete(emp_delete)
        db.session.commit()
        return redirect('/')
    except: 
        return 'something went wrong'


@app.route('/update/<int:id>',methods=["POST","GET"])
def update(id):
    emp = Employee.query.get(id)
    if request.method=="POST":
        emp.firstname = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'something went wrong..........'    
    else:
        return render_template("update.html",emp=emp)


if __name__ =="__main__":
    app.run(debug=True)