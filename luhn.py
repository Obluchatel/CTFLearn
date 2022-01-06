"""
 I used code from lunh module that can be fouud here:
 https://pypi.org/project/luhn/0.1.1/
 Thanks for its  Author: Michael McLoughlin
"""


def checksum(string):
    """
    Compute the Luhn checksum for the provided string of digits. Note this
    assumes the check digit is in place.
    """
    digits = list(map(int, string))
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return (odd_sum + even_sum) % 10


def verify(string):
    return (checksum(string) == 0)


card_number = "543210******1234"

for number in range(111111, 999999):
    if verify((card_number.replace("******", str(number)))) == True and int(
            card_number.replace("******", str(number))) % 123457 == 0:
        print(card_number.replace("******", str(number)))
    else:
        pass
