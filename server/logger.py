def is_logged(user):
    file_user = open("data_username.txt", "r")
    file_pass = open("data_password.txt", "r")
    while True:
        check_user = file_user.readline().replace("\n", "")
        check_pass = file_pass.readline().replace("\n", "")
        if check_user == user["name"] and check_pass == user["password"]:
            file_user.close()
            file_pass.close()
            return True
        if len(check_user) == 0 or len(check_pass) == 0:
            file_user.close()
            file_pass.close()
            return False


def is_sign_up(user):
    file_user = open("data_username.txt", "r")
    file_pass = open("data_password.txt", "r")
    while True:
        check_user = file_user.readline().replace("\n", "")
        check_pass = file_pass.readline().replace("\n", "")
        if check_user == user["name"] and check_pass == user["password"]:
            file_user.close()
            file_pass.close()
            return False
        if len(check_user) == 0 or len(check_pass) == 0:
            break
    file_user.close()
    file_pass.close()
    file_user = open("data_username.txt", "a")
    file_pass = open("data_password.txt", "a")
    file_user.write(user["name"] + "\n")
    file_pass.write(user["password"] + "\n")
    file_user.close()
    file_pass.close()
    return True
