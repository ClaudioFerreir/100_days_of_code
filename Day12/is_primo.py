n = 73

def is_primo(number):
    if number == 2:
        return True
    if number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(is_primo(n))