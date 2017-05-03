from django import forms


class FormOne(forms.Form):
    decimal_field = forms.DecimalField(decimal_places=2, max_digits=10)
    ip_address_field = forms.GenericIPAddressField()
    boolean_field = forms.BooleanField()
    char_field = forms.CharField(max_length=255)
    slug_field = forms.SlugField()
    date_field = forms.DateField()
    datetime_field = forms.DateTimeField()
    integer_field = forms.IntegerField()
    email_field = forms.EmailField()
    url_field = forms.URLField()
    time_field = forms.TimeField()
    float_field = forms.FloatField()
