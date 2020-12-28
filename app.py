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
    profession = db.Column(db.String(100))
    professionCode = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    phoneProvider = db.Column(db.String(100))
    propCode = db.Column(db.String(100))
    RentCode = db.Column(db.String(100))
    DepositAmt = db.Column(db.String(100))
    leaseStartDate = db.Column(db.String(100))
    leaseEndDate = db.Column(db.String(100))
    MoveInDate = db.Column(db.String(100))    
    MoveOutDate = db.Column(db.String(100))
    LiveWith = db.Column(db.String(100))
    LiveWithRelationship = db.Column(db.String(100))
    emergency1Name = db.Column(db.String(100))
    emergency1Phone = db.Column(db.String(100))
    emergency1Address = db.Column(db.String(100))
    emergency1Relationship = db.Column(db.String(100))
    emergency2Name = db.Column(db.String(100))
    emergency2Phone = db.Column(db.String(100))
    emergency2Address = db.Column(db.String(100))
    emergency2Relationship = db.Column(db.String(100))

    def __init__(self, name, email,profession,professionCode ,phone, phoneProvider,propCode, RoomNumber, DepositAmt, MoveInDate, MoveOutDate, LiveWith,LiveWithRelationshi,emergency1Name,emergency1Phone,emergency1Address,emergency1Relationship,emergency2Name,emergency2Phone,emergency2Address,emergency2Relationship):
        self.name = name
        self.email = email
        self.profession = profession
        self.professionCode = professionCode
        self.phone = phone
        self.phoneProvider = phoneProvider
        self.propCode = propCode
        self.RoomNumber = RoomNumber
        self.DepositAmt = DepositAmt
        self.MoveInDate = MoveInDate
        self.MoveOutDate = MoveOutDate
        self.LiveWith = LiveWith 
        self.LiveWithRelationship = LiveWithRelationship
        self.emergency1Name = emergency1Name
        self.emergency1Phone = emergency1Phone
        self.emergency1Address = emergency1Address
        self.emergency1Relationship = emergency1Relationship
        self.emergency2Name = emergency2Name
        self.emergency2Phone = emergency2Phone
        self.emergency2Address = emergency2Address
        self.emergency2Relationship = emergency2Relationship

    
class rentalProperty(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    propCode  = db.Column(db.String(100))
    address  = db.Column(db.String(100))
    availDate = db.Column(db.String(100))

    def __init__(self, propCode, address, availDate):
        self.propCode = propCode
        self.address = address
        self.availDate = availDate

class rentalPropertyAssets(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    propCode  = db.Column(db.String(100))
    buyDate = db.Column(db.String(100))
    item  = db.Column(db.String(100))
    assetdesc  = db.Column(db.String(100))
    cost = db.Column(db.String(100))


    def __init__(self, propCode, buyDate, item, assetdesc, cost):
        self.propCode = propCode
        self.buyDate = buyDate
        self.item = item
        self.assetdesc = assetdesc
        self.cost = cost

class rentalUnit(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    propCode  = db.Column(db.String(100))
    rentalCode  = db.Column(db.String(100))
    rent = db.Column(db.String(100))


    def __init__(self, propCode, address, availDate):
        self.propCode = propCode
        self.address = address
        self.availDate = availDate
        
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


@app.route('/residents')
def Residents():
    all_data = residents.query.all()

    return render_template("residents.html", residents = all_data)


#this route is for inserting data to mysql database via html forms
@app.route('/residents/insertResident', methods = ['POST'])
def insertResident():

    if request.method == 'POST' and request.form:
    
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

        flash("Resident Inserted Successfully")

        #return redirect(url_for('/residents'))
        # return redirect(url_for('Index'))
        return(request.form)
    else:
        flash("Resident Can Not Be Inserted")
        return("Failed: request form is null")



#this is our update route where we are going to update our employee
@app.route('/resident/update', methods = ['GET', 'POST'])
def updateResident():

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
@app.route('/resident/delete/<id>/', methods = ['GET', 'POST'])
def deleteResident(id):
    my_data = residents.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('Index'))


####################################################################################################################
# This is the charges portal
#
#
#
####################################################################################################################


@app.route('/charges')
def charges():
    all_data = charges.query.all()

    return render_template("charges.html", charges = all_data)

#this route is for inserting data to mysql database via html forms
@app.route('/charges/insertCharges', methods = ['POST'])
def insertCharges():

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

        flash("Resident Inserted Successfully")

        return redirect(url_for('/charges/'))


#this is our update route where we are going to update our residents
@app.route('/charges/update', methods = ['GET', 'POST'])
def updatecharges():

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
        flash("Resident Updated Successfully")

        return redirect(url_for('Index'))




#This route is for deleting our employee
@app.route('/charges/delete/<id>/', methods = ['GET', 'POST'])
def deleteH5558charges(id):
    my_data = charges.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Resident Deleted Successfully")

    return redirect(url_for('Index'))




if __name__ == "__main__":
    app.run(debug=True)