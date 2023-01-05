def calculate(amount, interest_rate, time):
    # your code here
    interest = amount * time * interest_rate / 100
    total_amount = amount + interest
    return interest, total_amount


def print_result(interest, total_amount):
    print('The interest is:', interest)
    print('The total amount is:', total_amount)
