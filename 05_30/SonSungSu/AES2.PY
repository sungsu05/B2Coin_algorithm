# pip install pycryptodome
import string,random,base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


"""
대칭키 생성 , 암호화 복호화 알고리즘
"""

random_value = string.ascii_letters + string.digits
random_value = list(random_value)
random.shuffle(random_value)
result = "".join(random_value[:16])
result = result.encode()
_KEY = result

class AESAlgorithm():
    key = _KEY
    # 대칭키
    # 장고에서는 환경변수로 관리해줄것

    @classmethod
    def encrypt(self,**kwargs):
        """ 암호화 """
        cipher = AES.new(self.key, AES.MODE_ECB)
        # AES 객체 생성
        data_dict = {}
        for key,value in kwargs.items():
            # 딕셔너리 순회
            cipher_data = cipher.encrypt(pad(value.encode(), AES.block_size))
            # 16BYTE 블록 사이즈에 맞게 패딩
            encrypt_value = base64.b64encode(cipher_data).decode()
            # 바이트 문자열을 문자열로 변환
            data_dict[key] = encrypt_value
            # 딕셔너리 KEY VALUE에 맞게 추가
        return data_dict

    @classmethod
    def decrypt(self,**kwargs):
        """ 복호화 """
        cipher = AES.new(self.key, AES.MODE_ECB)
        # AES 객체 생성
        data_dict = {}
        for key, value in kwargs.items():
            cipher_data = base64.b64decode(value)
            # 암호화 문자열을 바이트 문자열로 변환
            data = unpad(cipher.decrypt(cipher_data), AES.block_size)
            # 원본 데이터의 사이즈로 변환(블록 사이즈 제거)
            cipher_value = data.decode()
            # 바이트 문자열을 문자열로 변환
            data_dict[key] = cipher_value
            # 딕셔너리 KEY VALUE에 맞게 추가
        return data_dict

email = 'helloEmail@gmail.com'
username = 'helloUserName'
password = 'helloPassword!1'
birth_date = "030516"
gender = "2"
user_data = {
    "email":email,
    "username":username,
    "password":password,
    "birth_date" : birth_date,
    "gender" : gender,
}

encrypt_list = AESAlgorithm.encrypt(**user_data)
# 암호화 데이터 출력
print(encrypt_list)
decrypt_list = AESAlgorithm.decrypt(**dict(encrypt_list))
print(decrypt_list)
