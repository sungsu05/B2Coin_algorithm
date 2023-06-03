import re
"""
비밀번호 정규식 
최소 8자 이상의 길이
최소 하나의 영문 대소문자를 하나씩 포함
최소 하나의 숫자 포함
최소 하나의 특수 문자 (@, $, !, %, *, ?, &)

이메일 정규식
example@naver.com 형태를 요구
"""

def validated_password(password):
    """ 비밀번호 검증 """
    password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    password_match = re.match(password_pattern, password)
    return bool(password_match)

def validated_username(username):
    """ 유저네임 검증 """
    check = [
        lambda element: len(element) == len(element.replace(" ", "")),
        # 공백이 포함 되어 있을 경우 False
        lambda element: True if (len(element) > 1 and len(element) < 21) else False,
        # 전달된 값의 개수가 1~20 사이일 경우 True
    ]
    for i in check:
        if not i(username):
            return False
    return True

def validated_email(email):
    """ 이메일 검증"""
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    email_match = re.match(email_pattern, email)
    return bool(email_match)

def return_validated_result(**kwargs):
    """ 이메일,유저네임,비밀번호 검증 """
    if not validated_email(kwargs.get('email')):
        return [False,"이메일 정보가 올바르지 않습니다."]
    elif not validated_username(kwargs.get('username')):
        return [False,"닉네임이 올바르지 않습니다."]
    elif not validated_password(kwargs.get('password')):
        return [False,"비밀번호가 올바르지 않습니다."]
    return [True,"유효성 검사에 통과했습니다."]


user_data = {
    "email":"helloEmail@gmail.com",
    "username":"helloUserName",
    "password":"helloPassword!1"
}

result = return_validated_result(**user_data)
print(result[0],result[1])