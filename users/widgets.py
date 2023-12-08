from django.forms import RadioSelect
from django.shortcuts import get_object_or_404

from locations.models import Country

class CountryRadio(RadioSelect):
    option_template_name = 'users/widgets/option_country_radio.html'
    use_fieldset = False

    def create_option(self, *args, **kwargs):
        option = super(CountryRadio, self).create_option(*args, **kwargs)
        option['flag'] = get_object_or_404(Country, pk=str(option['value'])).flag
        return option