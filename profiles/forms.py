from django import forms
from .models import UserProfile
from artwork.models import Artist, Artwork


class CustomSignupForm(forms.Form):
    field_order = [
        'first_name',
        'last_name',
        'username',
        'email',
        'phone_number',
        'street_address1',
        'street_address2',
        'town_or_city',
        'county',
        'postcode',
        'password1',
        'password2',
    ]
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
    email = forms.EmailField(
        max_length=254,
        label='Email Address',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'})
    )
    phone_number = forms.CharField(
        max_length=20,
        label='Contact Number',
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'tel',
            'placeholder': 'Phone Number'}
            )
        )
    street_address1 = forms.CharField(
        max_length=80,
        label='Street Address 1',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Street Address 1'})
    )
    street_address2 = forms.CharField(
        max_length=80,
        label='Street Address 2',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Street Address 2 (Optional)'}
            )
    )
    town_or_city = forms.CharField(
        max_length=40,
        label='Town or City',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Town or City'})
    )
    county = forms.CharField(
        max_length=80,
        label='County',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'County, State or Region (Optional)'}
            )
    )
    postcode = forms.CharField(
        max_length=20,
        label='Postal Code',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Postal Code'})
    )

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profile = user.userprofile
        profile.default_street_address1 = self.cleaned_data['street_address1']
        profile.default_street_address2 = self.cleaned_data['street_address2']
        profile.default_town_or_city = self.cleaned_data['town_or_city']
        profile.default_county = self.cleaned_data['county']
        profile.default_postcode = self.cleaned_data['postcode']
        profile.default_phone_number = self.cleaned_data['phone_number']
        profile.save()


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150, required=False, label="Username"
        )
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

    def save(self, commit=True):
        """ Custom save method to update both the Profile and User tables """
        profile = super().save(commit=False)
        if self.user:
            self.user.username = self.cleaned_data['username']
            self.user.first_name = self.cleaned_data['first_name']
            self.user.last_name = self.cleaned_data['last_name']
            self.user.email = self.cleaned_data['email']
            self.user.save()

        if commit:
            profile.save()
        return profile


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'bio', 'image']


class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = [
            'artist',
            'title',
            'description',
            'medium',
            'price',
            'image',
            'is_sold',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['rows'] = 4
