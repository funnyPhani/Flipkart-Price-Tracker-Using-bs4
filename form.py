from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired,DataRequired,Email,ValidationError,URL
from wtforms.fields.html5 import EmailField,URLField
import email_validator
import linkvalidator as lv
import save as s
import Scrapper as sc
from short import shortit
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY']= "thisissecret"


class Front_End_Form(FlaskForm):
    def flipkart_url(form,url):
        if "flipkart" in url.data and lv.check(url.data):
            return True
        else:
            raise ValidationError('Enter the correct url')
    #raise validation errors
    
   
    Product_name = URLField("Enter Flipkart's product link:", validators=[DataRequired(message="Enter URL Please"), URL(message="Enter Valid URl Please."), flipkart_url])
    Displayed_price = StringField("Current Price of the product is:",render_kw={'readonly':True})  
    Your_Price = IntegerField("Enter the Price, at which you want:", validators=[InputRequired("Please enter the price.")])
    Emailsection = EmailField("Enter your email for reminders:", validators=[InputRequired("Please enter your email address."), Email("This field requires a valid email address")])
    submit=SubmitField("Submit")
  

@app.route('/', methods=['GET','POST'])
def form():
    form= Front_End_Form()
    if form.validate_on_submit():
        s.insertdata(s.records.count(),str(form.Emailsection.data),str(shortit(form.Product_name.data)),int(form.Your_Price.data))
        return render_template('main2.html', form=form)
    return render_template('main.html', form=form)


if __name__=='__main__':    
    app.run(debug=True)
