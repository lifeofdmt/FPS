from django import forms


school = ["Malik","Taiwo", "DMT", "Delana"]
class register1_form(forms.Form):
    firstname = forms.CharField(label="FirstName", strip=True)
    middlename = forms.CharField(label="SecondName", strip=True)
    lastname = forms.CharField(label="Lastname", strip=False)
    email = forms.EmailField(label="Email-Address")
    image = forms.ImageField(label="Your Picture", required=False)
    schools = forms.ChoiceField(label="School", choices=enumerate(school))
    school_key = forms.IntegerField(label="School's Key")

    check = forms.BooleanField(label="Do you aree to the the terms and conditions", required=False)
