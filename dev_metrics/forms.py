from django import forms

class addMetrics(forms.Form):
    reporting_period  = forms.CharField(label='Reporting Period', max_length=100)