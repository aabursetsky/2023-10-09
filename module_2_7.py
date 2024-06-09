def get_multiplied_digits(number):
    str_number = str(number)
    str_number = str_number.replace('0', '') # Удаление всех 0, в т.ч. замыкающих
    first = int(str_number[0])               # Первая или оставшаяся цифра
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:])) # без первой цифры
    return first


result = get_multiplied_digits(40203)
print(result)

# 24 
