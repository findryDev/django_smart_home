from django.http import HttpResponse
from django.template import loader
from piec_CO.models import TemperatureIn, TemperatureOut, TemperatureReturn
from .app_lib.queries_from_db import DataToTemplate


'''
def utility_processor():
    def to_two_decimal(float_number):
        unity_digit, decimal_digit = str(float_number).split(".")
        if len(decimal_digit) < 2:
            decimal_digit = decimal_digit + "0"
        return unity_digit + "." + decimal_digit
    return dict(to_two_decimal=to_two_decimal)
'''


# Create your views here.
def index(request):
    template = loader.get_template('web_home_page/index.html')
    return(HttpResponse(template.render(request=request)))

def temperature_in(request):
    pass

def temperature_out(request):
    pass

def temperature_return(request):
    pass

def temperature_all(request):
    pass

def temperature_all_without_plot(request):
    template = loader.get_template('web_home_page/temperature_all_without_plot.html')


    context = {'temperature_in': DataToTemplate(TemperatureIn).          date_to_template,
              'temperature_out': DataToTemplate(TemperatureOut).date_to_template,
              'temperature_return': DataToTemplate(TemperatureReturn).date_to_template}

    return(HttpResponse(template.render(context, request)))