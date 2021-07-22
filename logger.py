def is_logged(user):
    file_user = open("data_username.txt", "r")
    file_pass = open("data_password.txt", "r")
    while True:
        check_user = file_user.readline().replace("\n","")
        check_pass = file_pass.readline().replace("\n","")
        if check_user == user["name"] and check_pass == user["password"]:
            file_user.close()
            file_pass.close()
            return True
        if len(check_user) == 0 or len(check_pass) == 0:
            file_user.close()
            file_pass.close()
            return False

def regis(user):
    file_user = open("data_username.txt", "a")
    file_pass = open("data_password.txt", "a")
    file_mail = open("data_email.txt", "a")
    file_first_name = open("data_firstname.txt", "a")
    file_last_name = open("data_lastname.txt", "a")
    file_user.write(user["name"] + "\n")
    file_pass.write(user["password"] + "\n")
    file_mail.write(user["mail"] + "\n")
    file_first_name.write(user["first_name"] + "\n")
    file_last_name.write(user["last_name"] + "\n")
    file_user.close()
    file_pass.close()
    file_mail.close()
    file_first_name.close()
    file_last_name.close()