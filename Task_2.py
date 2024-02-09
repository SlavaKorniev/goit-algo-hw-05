def generator_numbers (text: str): # Генератор. Шукає числа між пробілами у тексті і виводить їх як float
    import re
    numbers = []
    numbers = re.findall(r" \d+\.\d+ ", text) # Шукає числа між пробілами у тексті
    for number in numbers:
        number = float(re.sub(" ","",number)) # Чистить числа від пробілів, виводить їх як float
        yield number

def sum_profit(text, generator_numbers): # Х-з чому, але ця функція спрацювала :)
    # має використовувати генератор generator_numbers для обчислення загальної суми чисел у рядку text
    sum__profit = 0
    for number in generator_numbers (text): # витягує числа з генератора і сумує їх
        sum__profit += number
    return sum__profit

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
