from django import forms

class TickerForm(forms.Form):
    ticker = forms.CharField(label="Ticker", max_length=5)
    print("forms.py has made a form")