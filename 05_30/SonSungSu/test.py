def test(**kwargs):
    data_list = []
    for value in kwargs:
        print(value)

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

test(**user_data)