class rentalUnit(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    propCode  = db.Column(db.String(100))
    rentalCode  = db.Column(db.String(100))
    rent = db.Column(db.String(100))


    def __init__(self, propCode, address, availDate):
        self.propCode = propCode
        self.rentalCode = rentalCode
        self.rent = rent
        


####################################################################################################################
# This is the resident portal for Rental Unit
#
#
#
####################################################################################################################

@app.route('/rentalUnit')
def rentalUnit():
    all_data = rentalUnit.query.all()

    return render_template("rentalUnit.html", rentalUnit = all_data)

#this route is for inserting data to mysql database via html forms
@app.route('/rentalUnit/insertrentalUnit', methods = ['POST'])
def insertrentalUnit():

    if request.method == 'POST' and request.form:
    
        id = request.form['id']
        propCode = request.form['propCode']
        rentalCode = request.form['rentalCode']
        rent = request.form['rent']


        my_data = rentalUnit(id,propCode,rentalCode,rent,)
        db.session.add(my_data)
        db.session.commit()

        flash("Rental Property Inserted Successfully")

        #return redirect(url_for('/residents'))
        # return redirect(url_for('Index'))
        return(request.form)
    else:
        flash("Rental Property Can Not Be Inserted")
        return("Failed: request form is null")

#this is our update route where we are going to update our employee
@app.route('/rentalUnit/update', methods = ['GET', 'POST'])
def updaterentalUnit():

    if request.method == 'POST':
        my_data = rentalUnit.query.get(request.form.get('propCode'))
        my_data.Address = request.form['Address']
        my_data.AvailabilityDate = request.form['AvailabilityDate']


        db.session.commit()
        flash("rentalUnit Updated Successfully")

        return redirect(url_for('Index'))
    
#This route is for deleting our employee
@app.route('/rentalUnit/delete/<propCode>/', methods = ['GET', 'POST'])
def deleterentalProperty(propCode):
    my_data = rentalProperty.query.get(propCode)
    db.session.delete(my_data)
    db.session.commit()
    flash("propCode Deleted Successfully")

    return redirect(url_for('Index'))