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
# @classmethod : 인스턴스를 생성하지 않고 메서드를 사용할 수 있는 데코레이터

class ValidatedData():
    """ 데이터 검증 클래스 """
    @classmethod
    def validated_password(self,password):
        """ 비밀번호 검증 """
        if password == None:
            return False
        password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        password_match = re.match(password_pattern, password)
        return bool(password_match)

    @classmethod
    def validated_username(self,username):
        """ 유저네임 검증 """
        check = [
            lambda element: element != None,
            # None값이 아니라면 True
            lambda element: len(element) == len(element.replace(" ", "")),
            # 공백이 포함 되어 있을 경우 False
            lambda element: True if (len(element) > 1 and len(element) < 21) else False,
            # 전달된 값의 개수가 1~20 사이일 경우 True
        ]
        for i in check:
            if not i(username):
                return False
        return True

    @classmethod
    def validated_email(self,email):
        """ 이메일 검증"""
        if email == None:
            return False
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        email_match = re.match(email_pattern, email)
        return bool(email_match)

    @classmethod
    def validated_birth_date(self,birth_date):
        """ 생년월일 검증 """
        check = [
            lambda element: len(element) == len(element.replace(" ", "")),
            # 공백이 포함 되어 있을 경우 False
            lambda element: True if (len(element) == 6) else False,
            # 길이가 6과 맞지 않다면 False
            lambda element: element.isdigit(),
            # 숫자를 제외한 값이 있다면 False
            lambda element: True if int(element[2:4])>0 and int(element[2:4]) < 13 else False,
            # 출생 월이 0보다 크거나 13보다 작다면 True
            lambda element: True if int(element[4:]) > 0 and int(element[4:]) < 32 else False,
            # 출생 일이 0보다 크거나 32보다 작다면 True
        ]
        for i in check:
            if not i(birth_date):
                return False
        return True

    @classmethod
    def validated_gender(self,gender):
        """ 성별 데이터 검증 """
        check = [
            lambda element: element != None,
            # None값이 아니라면 True
            lambda element: len(element) == len(element.replace(" ", "")),
            # 공백이 포함 되어 있을 경우 False
            lambda element: True if (len(element) == 1) else False,
            # 길이가 6과 맞지 않다면 False
            lambda element: element.isdigit(),
            # 숫자를 제외한 값이 있다면 False
            lambda element: int(element) in [1,2,3,4],
            # 값이 1,2,3,4
        ]
        for i in check:
            if not i(gender):
                return False
        return True

    @classmethod
    def validated_user_data(self,**kwargs):
        """ 이메일,유저네임,비밀번호,생년월일,성별 검증 """
        if not self.validated_email(kwargs.get('email')):
            return [False,"이메일 정보가 올바르지 않습니다."]
        elif not self.validated_username(kwargs.get('username')):
            return [False,"닉네임이 올바르지 않습니다."]
        elif not self.validated_password(kwargs.get('password')):
            return [False,"비밀번호가 올바르지 않습니다."]
        elif kwargs.get('birth_date') != None:
            # 생년월일 및 성별은 필수 입력 사항이 아니기 때문에 None값이라면 검사하지 않는다.
            if not self.validated_birth_date(kwargs.get('birth_date')):
                return [False, "생년월일 정보가 올바르지 않습니다."]
            elif not self.validated_gender(kwargs.get('gender')):
                return [False, "성별 정보가 올바르지 않습니다."]
        elif kwargs.get('birth_date') == None or kwargs.get('gender') != None:
            # 성별 데이터는 입력했지만, 생년월일 데이터를 입력하지 않았을 경우
            return [False, "생년월일 데이터를 입력하지 않았습니다."]
        return [True,"유효성 검사에 통과했습니다."]

email = 'helloEmail@gmail.com'
username = 'helloUserName'
password = 'helloPassword!1'
# birth_date = None
# gender = None
birth_date = "030516"
gender = "2"


user_data = {
    "email":email,
    "username":username,
    "password":password,
    "birth_date" : birth_date,
    "gender" : gender,
}

result = ValidatedData.validated_user_data(**user_data)
print(result[0],result[1])




