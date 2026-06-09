from django import forms
from .models import UserProfile


class CustomSignupForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        label='First Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
        )
    last_name = forms.CharField(
        max_length=30,
        label='Last Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
        )
    address = forms.CharField(
        max_length=250,
        label='Mailing Address',
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Mailing Address',
            'rows': 7}
            )
        )
    contact_number = forms.CharField(
        max_length=20,
        label='Contact Number',
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'tel',
            'placeholder': 'Contact Number'}
            )
        )

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profile = user.userprofile
        profile.default_address = self.cleaned_data['address']
        profile.default_contact_number = self.cleaned_data['contact_number']
        profile.save()


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=False, label="Username")
    first_name = forms.CharField(
        max_length=30,
        required=False,
        label="First Name"
        )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        label="Last Name"
        )
    email = forms.EmailField(
        max_length=254,
        required=False,
        label="Email Address"
        )

    class Meta:
        model = UserProfile
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'default_phone_number', 
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_county',
            'default_postcode'
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user:
            self.fields['username'].initial = self.user.username
            self.fields['first_name'].initial = self.user.first_name
            self.fields['last_name'].initial = self.user.last_name
            self.fields['email'].initial = self.user.email

        friendly_names = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County, State or Region',
            'default_postcode': 'Postal Code',
        }

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control \
                border-secondary-subtle shadow-sm mb-2'
            if field_name in ['default_street_address1',
                              'default_town_or_city', 'default_postcode']:
                field.required = True
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['rows'] = 4

            if field_name in friendly_names:
                placeholder = friendly_names[field_name]
                field.widget.attrs['placeholder'] = placeholder
                field.label = placeholder
