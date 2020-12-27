from flask import Flask, flash, redirect, render_template, request, url_for
from flask_wtf import Form
from wtforms.fields.html5 import DateField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"


####################################################################################################################
# This is the database model we used 
#
#
#
####################################################################################################################


#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)



#Database for the User
class residents(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    phoneProvider = db.Column(db.String(100))
    RoomNumber = db.Column(db.String(100))
    DepositAmt = db.Column(db.String(100))
    
    MoveInDate = db.Column(db.String(100))    
    MoveOutDate = db.Column(db.String(100))



    def __init__(self, name, email, phone, phoneProvider, RoomNumber, DepositAmt, MoveInDate, MoveOutDate):

        self.name = name
        self.email = email
        self.phone = phone
        self.phoneProvider = phoneProvider
        self.RoomNumber = RoomNumber
        self.DepositAmt = DepositAmt
        
        self.MoveInDate = MoveInDate
        self.MoveOutDate = MoveOutDate


    
    #Database for the charges
class charges(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    billdatestart  = db.Column(db.String(100))
    billdateend  = db.Column(db.String(100))
    user = db.Column(db.String(100))
    item = db.Column(db.String(100))
    discription = db.Column(db.String(100))
    charge = db.Column(db.String(100))



    def __init__(self, billdatestart, billdateend, user, item, discription, charge ):

        self.billdatestart = billdatestart
        self.billdateend = billdateend
        self.user = user
        self.item = item
        self.discription = discription
        self.charge = charge

####################################################################################################################
#This is the index route where we are going to
#
#
#
####################################################################################################################

@app.route('/')
def Index():
    all_data = residents.query.all()

    return render_template("index.html", residents = all_data)


####################################################################################################################
# This is the resident portal for the Users: Manage users in the system for 5558
#
#
#
####################################################################################################################


@app.route('/h5558/residents')
def h5558Residents():
    all_data = residents.query.all()

    return render_template("h5558residents.html", residents = all_data)
    #return redirect(url_for('/h5558/resident/'))


#this route is for inserting data to mysql database via html forms
@app.route('/h5558/resident/insertH5558Resident', methods = ['POST'])
def insertH5558Resident():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        phoneProvider = request.form['phoneProvider']
        RoomNumber = request.form['RoomNumber']
        DepositAmt = request.form['DepositAmt']
    
        MoveInDate = request.form['MoveInDate']   
        MoveOutDate = request.form['MoveOutDate']
 


        my_data = residents( name, email, phone, phoneProvider, RoomNumber, DepositAmt, MoveInDate, MoveOutDate)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for('/h5558/resident/'))


#this is our update route where we are going to update our employee
@app.route('/h5558/resident/update', methods = ['GET', 'POST'])
def updateH5558Resident():

    if request.method == 'POST':
        my_data = residents.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']

        my_data.phoneProvider = request.form['phoneProvider']
        my_data.RoomNumber = request.form['RoomNumber']
        my_data.DepositAmt = request.form['DepositAmt']
    
        my_data.MoveInDate = request.form['MoveInDate']

    
        my_data.MoveOutDate = request.form['MoveOutDate']

        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('Index'))




#This route is for deleting our employee
@app.route('/h5558/resident/delete/<id>/', methods = ['GET', 'POST'])
def deleteH5558Resident(id):
    my_data = residents.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('Index'))


####################################################################################################################
# This is the charges portal for 5558
#
#
#
####################################################################################################################


@app.route('/h5558/charges')
def h5558charges():
    all_data = charges.query.all()

    return render_template("h5558charges.html", charges = all_data)

#this route is for inserting data to mysql database via html forms
@app.route('/h5558/charges/insertH5558charges', methods = ['POST'])
def insertH5558charges():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        phoneProvider = request.form['phoneProvider']
        RoomNumber = request.form['RoomNumber']
        DepositAmt = request.form['DepositAmt']
    
        MoveInDate = request.form['MoveInDate']
        MoveOutDate = request.form['MoveOutDay']



        my_data = residents( name, email, phone, phoneProvider, RoomNumber, DepositAmt, MoveInDate, MoveOutDate)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for('/h5558/charges/'))


#this is our update route where we are going to update our employee
@app.route('/h5558/charges/update', methods = ['GET', 'POST'])
def updateH5558charges():

    if request.method == 'POST':
        my_data = residents.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
        my_data.phoneProvider = request.form['phoneProvider']
        my_data.RoomNumber = request.form['RoomNumber']
        my_data.DepositAmt = request.form['DepositAmt']
        my_data.MoveInDate = request.form['MoveInDate']
        my_data.MoveOutDate = request.form['MoveOutDate']


        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('Index'))




#This route is for deleting our employee
@app.route('/h5558/charges/delete/<id>/', methods = ['GET', 'POST'])
def deleteH5558charges(id):
    my_data = charges.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('Index'))




if __name__ == "__main__":
    app.run(debug=True)