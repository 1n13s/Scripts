import random
import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
nums = string.digits
punt = "!@#$%^&"

def make_password(lenght: int):
    if lenght < 4: lenght = 4
    password = (
        random.choice(lower)
        +random.choice(upper)
        +random.choice(nums)
        +random.choice(punt)
    )
    chars = lower+upper+nums+punt
    for _ in range(lenght-4):
        password += random.choice(chars)
    return shuffle_password(password)

def shuffle_password(password: str):
    list_pwd = list(password)
    random.shuffle(list_pwd)
    return "".join(list_pwd)

"""def evaluate_password(password: str):
    evaluation = {
            "lower": False,
            "upper": False,
            "nums": False,
            "punt": False
        }
    for letter in password:
        if letter in string.ascii_lowercase:
            evaluation.update({"lower": True})
        if letter in string.ascii_uppercase:
            evaluation.update({"upper": True})
        if letter in string.digits:
            evaluation.update({"nums": True})
        if letter in string.punctuation:
            evaluation.update({"punt": True})
    return evaluation
"""