email = "zeeshan@email.com"
name = "Zeeshan"

def greetings(name):
    print(f"Helle {name}")


def fina_max(numbers):
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num