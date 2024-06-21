import string
from Tools.my_tools import make_password



def test_password_len():
    password = make_password(10)
    assert len(password) == 10

def test_password_chars():
    password = make_password(10)
    assert evaluate_dict(evaluation=make_evaluate_dict(password)) == True

def evaluate_dict(evaluation: dict):
    for value in evaluation.values():
        if not value: return value
    return True


def make_evaluate_dict(password: str):
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