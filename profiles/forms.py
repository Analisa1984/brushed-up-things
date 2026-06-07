from django import forms


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
