from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat
app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html',
                               billform=bill_form)
    def post(self):
        billform = BillForm(request.form)
        amount = int(billform.amount.data)
        period = billform.period.data

        name1 = billform.name1.data
        days1 = float(billform.days1.data)

        name2 = billform.name2.data
        days2 = float(billform.days2.data)

        the_bill = flat.Bill(amount, period)
        flatmate1 = flat.Flatmate(name1, days1)
        flatmate2 = flat.Flatmate(name2, days2)

        return render_template('bill_form_page.html', billform=billform, result = True,
                                                                 name1= flatmate1.name,
                                                                 name2 = flatmate2.name,
                                                                 amount1 = flatmate1.pays(the_bill,flatmate2),
                                                                 amount2 = flatmate2.pays(the_bill,flatmate1))


# class ResultPage(MethodView):
#     def post(self):
#         billform = BillForm(request.form)
#         amount = int(billform.amount.data)
#         period = billform.period.data
#
#         name1 = billform.name1.data
#         days1 = float(billform.days1.data)
#
#         name2 = billform.name2.data
#         days2 = float(billform.days2.data)
#
#         the_bill = flat.Bill(amount, period)
#         flatmate1 = flat.Flatmate(name1, days1)
#         flatmate2 = flat.Flatmate(name2, days2)
#
#         return render_template('bill_form_page.html',
#                                                                  name1= flatmate1.name,
#                                                                  name2 = flatmate2.name,
#                                                                  amount1 = flatmate1.pays(the_bill,flatmate2),
#                                                                  amount2 = flatmate2.pays(the_bill,flatmate1))

class BillForm(Form):
    amount = StringField('Bill Amount:', default = "100")
    period = StringField('Bill Period:', default = "december")
    name1 = StringField('Name:', default = 'divyansh')
    days1 = StringField('Days in the house:', default= '20')
    name2 = StringField('Name:', default = "rohan")
    days2 = StringField('Days in the house:', default= '20')
    button = SubmitField('Calculate')



app.add_url_rule('/', view_func= HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func = BillFormPage.as_view('bill_form_page'))

# app.add_url_rule('/results',
#                  view_func = ResultPage.as_view('results_page'))

app.run(debug=True)