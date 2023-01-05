def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 2)


def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


def main():
    """Entry point of the program."""
    user_input = input().split()
    temperature, unit = float(user_input[0]), user_input[1]  # read the input
    print(fahrenheit_to_celsius(temperature) if unit == 'F' else celsius_to_fahrenheit(temperature),
          'F' if unit == 'C' else 'C')
