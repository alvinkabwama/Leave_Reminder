from django import forms


class LeaveForm(forms.Form):
    leave_file = forms.FileField()   
    
