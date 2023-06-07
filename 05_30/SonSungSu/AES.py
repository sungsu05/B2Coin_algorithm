# pip install pycryptodome
import string,random,base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
"""
패딩 
 - 암호화, 복호화 알고리즘의 경우 INPUT 데이터는 블록 사이즈의 배수가 되어야 한다.
 - 이때 INPUT 데이터가 블록 사이즈의 배수가 아닌경우  마지막 블록에 값을 추가하여 블록 사이즈의 배수로 맞춘다.
apd : 데이터를 블록 크기의 배수로 패딩
unpad : 패딩이 추가된 데이터를 원래의 크기로 복원
"""

def encrypt(data, key):
    """ 암호화 """
    cipher = AES.new(key, AES.MODE_ECB)
    # 암호화 객체 생성
    # ECB 원본 데이터를 16Byte로 쪼개어 생성
    cipher_data = cipher.encrypt(pad(data.encode(), AES.block_size))
    # 16byte 블록 사이즈에 맞게 데이터를 패딩
    return base64.b64encode(cipher_data).decode()
    # base64 : 암호화 데이터를 인코딩
    # decode : 바이트 문자열을 문자열로 변환

def decrypt(cipher_data, key):
    """ 복호화 """
    cipher = AES.new(key, AES.MODE_ECB)
    # 복호화 객체 생성
    cipher_data = base64.b64decode(cipher_data)
    # 암호화 문자열 데이터를 바이트 문자열로 변환
    data = unpad(cipher.decrypt(cipher_data), AES.block_size)
    # 블록 사이즈를 기존의 값으로 복원 (패딩 이전)
    return data.decode()
    # 복호화한 바이트 문자열을 문자열로 변환

random_value = string.ascii_letters + string.digits
random_value = list(random_value)
random.shuffle(random_value)
result = "".join(random_value[:16])
# 영 대소문자, 숫자로 이루어진 16byte의 랜덤값 생성
print("문자열: ",result,type(result))

result = result.encode()
# 문자열 데이터를 바이트 문자열 데이터로 변환
print("바이트 문자열",result,type(result))

key = result
# 새로 생성한 결과값을 key로 사용
# 대칭 키 : 암호화, 복호화에 사용되는 키
# 데이터 베이스에 사용될시 항상 key값은 환경 변수를 사용하여 관리하여야 한다.
# 또한 key값은 1개월을 기준으로 주기적으로 바꾸는것이 좋다고 한다.
print(key,type(key))
msg = '안녕하세요'

encrypted = encrypt(msg, key)
print('암호화된 결과:', encrypted)

decrypted = decrypt(encrypted, key)
print('복호화된 결과:', decrypted)
