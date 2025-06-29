def convert_temperature(temp, unit):
    """
    Converts temperature between Fahrenheit and Celsius.
    
    Parameters:
    - temp (float or int): The temperature value to convert.
    - unit (str): 'F' if input is Fahrenheit, 'C' if input is Celsius.
    
    Returns:
    - float: Converted temperature rounded to 2 decimal places.
    """
    if unit == 'F':
        celsius = (temp - 32) * 5/9
        return round(celsius, 2)
    elif unit == 'C':
        fahrenheit = (temp * 9/5) + 32
        return round(fahrenheit, 2)
    else:
        return "Invalid unit. Please use 'F' or 'C'."
