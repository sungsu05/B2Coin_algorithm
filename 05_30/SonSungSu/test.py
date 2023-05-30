import re
def solution(email,password,username):
    password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    password_match = re.match(password_pattern, password)
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    email_match = re.match(email_pattern, email)
    if not all([bool(password_match), bool(email_match)]):
        return False
    check =[
        lambda element: len(element) == len(element.replace(" ", "")),
        # 공백이 포함 되어 있을 경우 False
        lambda element: True if (len(element) > 1 and len(element) < 21) else False,
        # 전달된 값의 개수가 1~20 사이일 경우 True
    ]

    for i in check:
        if not i(username):
            return False
    return True

print(solution("thstjdtn05@gmail.com","Asdfsdaf315602!!","하이"))
