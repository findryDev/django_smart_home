"""class using in views
"""
from datetime import datetime
from .fontello_style import get_icon_name_CO


class DataToTemplate:
    """class aggregated information of temperature include in data base
    """
    def __init__(self, model_db):
        self.date_format = "%d-%m-%Y %H:%M:%S"
        self.db_query_last = model_db.objects.order_by("-id").first()
        self.dict_query_last = self.query_to_dict(self.db_query_last)
        self.db_query_tempearture_max = model_db.objects.order_by(
            "-current_temperature"
        ).first()
        self.db_query_tempearture_min = model_db.objects.order_by(
            "current_temperature"
        ).first()
        self.dict_query_max = self.query_to_dict(self.db_query_tempearture_max)
        self.dict_query_min = self.query_to_dict(self.db_query_tempearture_min)

        self.date_to_template = self.get_data_to_template(
            date_format=self.date_format,
            dict_query_last=self.dict_query_last,
            dict_query_max=self.dict_query_max,
            dict_query_min=self.dict_query_min,
        )

    def query_to_dict(self, q):
        """covert data model to dictionary

        Args:
            self,
            q[data model]

        Returns:
            [dictionary]: [dictionary to template]
        """
        if q is None:
            return None

        dictionary = {}
        dictionary["id"] = q.id
        dictionary["pub_date"] = q.pub_date
        dictionary["current_temperature"] = q.current_temperature

        return dictionary

    def float_to_string_two_decimal(self, val):
        """add zero if data is to short

        Args:
            val [float]: float to convert

        Returns:
            strings: strings to template
        """
        if val is None:
            return "0.00"
        unity_digit, decimal_digit = str(val).split(".")
        if len(decimal_digit) < 2:
            decimal_digit = decimal_digit + "0"
            return unity_digit + "." + decimal_digit

    def get_data_to_template(
        self, date_format, dict_query_last, dict_query_max, dict_query_min
    ):
        """match summary dictionary

        Args:
            date_format ([string]): date time format
            dict_query_last ([query object): dictionary current temperature[key:
                                                                    current temperature,
                                                                    date,
                                                                    icon]
            dict_query_max ([dictionary]): dictionary max temperature[key:
                                                                    max_temperature,
                                                                    date]

            dict_query_min ([dictionary]): dictionary min temperature[key:
                                                                    min_temperature,
                                                                    date]
        ['current_temperature', 'date', 'icon', 'max', 'min']
        ['max_temperature', 'date']
        ['min_temperature', 'date']

        Returns:
            [dictionary]: ['current_temperature', 'date', 'icon',
            'max'['max_temperature', 'date']
            'min'['min_temperature', 'date']]
        """
        dict_to_template = {}

        dict_to_template["current_temperature"] = self.float_to_string_two_decimal(
            dict_query_last["current_temperature"]
        )
        dict_to_template["date"] = dict_query_last["pub_date"].strftime(date_format)
        dict_to_template["icon"] = get_icon_name_CO(
            dict_query_last["current_temperature"]
        )

        dict_to_template["max"] = {}
        dict_to_template["max"]["max_temperature"] = self.float_to_string_two_decimal(
            dict_query_max["current_temperature"]
        )
        dict_to_template["max"]["date"] = dict_query_max["pub_date"].strftime(
            date_format
        )

        dict_to_template["min"] = {}
        dict_to_template["min"]["min_temperature"] = self.float_to_string_two_decimal(
            dict_query_min["current_temperature"]
        )
        dict_to_template["min"]["date"] = dict_query_min["pub_date"].strftime(
            date_format
        )
        return dict_to_template

    def sensor_queries_to_plot(self, model_db, how_many):
        """Plot data

        Args:
            model_db ([data base model]): [table]
            how_many ([int]): [how many records in plot]

        Returns:
            [dictionary]: [data used to created plot]
        """
        temperature_queries = model_db.object.order_by("-id")[:how_many]
        return temperature_queries

    def delete_old_data(self, days_limit, model_db):
        """cleaning data and delete old data

        Args:
            days_limit (int): [how long data exist in database]
            model_db ([data model object]]): [table]

        Returns:
            [int]: [how many records was delete]
        """
        try:
            old_period = datetime.datetime.now() - datetime.timedelta(days_limit)
            del_count = model_db.objects.filter(pub_date_lte=old_period).delete()
            return del_count
        except Exception as e:
            return e
