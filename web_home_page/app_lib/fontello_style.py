"""maching value to symbols
"""
def get_icon_name_co(temperature):
    """check value in temperature and match fontello termometer icon

    Args:
        temperature ([float]): [temperature]

    Returns:
        [string]: [name of symbol]
    """
    icon = ""
    if temperature <= 10:
        icon = "icon-thermometer-0"
    elif temperature > 10 and temperature <= 20:
        icon = "icon-thermometer-quarter"
    elif temperature > 20 and temperature <= 40:
        icon = "icon-thermometer-2"
    elif temperature > 40 and temperature < 50:
        icon = "icon-thermometer-3"
    elif temperature >= 50:
        icon = "icon-thermometer"
    return icon


def get_icon_name_home(temperature):
    """check value in temperatureerature and match fontello termometer icon

    Args:
        temperature ([float]): [temperature]

    Returns:
        [string]: [name of symbol]
    """
    icon = ""
    if temperature <= 10:
        icon = "icon-thermometer-0"
    elif temperature > 10 and temperature <= 15:
        icon = "icon-thermometer-quarter"
    elif temperature > 15 and temperature <= 20:
        icon = "icon-thermometer-2"
    elif temperature > 20 and temperature < 25:
        icon = "icon-thermometer-3"
    elif temperature >= 25:
        icon = "icon-thermometer"
    return icon
