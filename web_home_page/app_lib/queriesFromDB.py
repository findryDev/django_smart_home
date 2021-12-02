from .fontelloStyle import get_icon_name_CO
from .fontelloStyle import get_icon_name_home
from datetime import datetime
from django.forms.models import model_to_dict

# TODO: sensorQueries improve

def queryToDict(q):
    if q == None:
        return None

    dictionery = {}
    dictionery['id'] = q.id
    dictionery['pub_date'] = q.pub_date
    dictionery['current_temperature'] = q.current_temperature

    return dictionery


def float_to_string_two_decimal(val):
    if val is None:
        return "0.00"
    unity_digit, decimal_digit = str(val).split(".")
    if len(decimal_digit) < 2:
        decimal_digit = decimal_digit + "0"
        return unity_digit + "." + decimal_digit




def get_data_to_template(modelDB):
    dateFormat = '%d-%m-%Y %H:%M:%S'
    dbQuery_last = modelDB.objects.order_by('-id').first()
    dict_query_last = queryToDict(dbQuery_last)
    dbQuery_tempearture_max = modelDB.objects.order_by('-current_temperature').first()
    dbQuery_tempearture_min = modelDB.objects.order_by('current_temperature').first()
    dict_query_max = queryToDict(dbQuery_tempearture_max)
    dict_query_min = queryToDict(dbQuery_tempearture_min)

    dict_to_template ={}

    dict_to_template['current_temperature'] = float_to_string_two_decimal(dict_query_last['current_temperature'])
    dict_to_template['date'] = dict_query_last['pub_date'].strftime(dateFormat)
    dict_to_template['icon'] = get_icon_name_CO(dict_query_last['current_temperature'])

    dict_to_template['max'] = {}
    dict_to_template['max']['max_temperature'] = float_to_string_two_decimal(dict_query_max['current_temperature'])
    dict_to_template['max']['date'] = dict_query_max['pub_date'].strftime(dateFormat)

    dict_to_template['min'] = {}
    dict_to_template['min']['min_temperature'] = float_to_string_two_decimal(dict_query_min['current_temperature'])
    dict_to_template['min']['date'] = dict_query_min['pub_date'].strftime(dateFormat)

    return dict_to_template


def sensor_queries_to_plot(modelDB, howMany):
    temperatureQueries = (modelDB.object.order_by('-id')[:howMany])
    return temperatureQueries


def delete_old_data(daysLimit, modelDB):
    try:
        oldPeriod = datetime.datetime.now() - datetime.timedelta(daysLimit)
        delCount = modelDB.objects.filter(pub_date_lte=oldPeriod).delete()
        return delCount
    except Exception as e:
        return e

# TODO: add max and min function



