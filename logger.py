def is_logged(username_client, password_client):
    file_user = open("data_username.txt", "r")
    file_pass = open("data_password.txt", "r")
    while True:
        check_user = file_user.readline().replace("\n","")
        check_pass = file_pass.readline().replace("\n","")
        if check_user == username_client and check_pass == password_client:
            file_user.close()
            file_pass.close()
            return True
        if len(check_user) == 0 or len(check_pass) == 0:
            file_user.close()
            file_pass.close()
            return False

def regis(username_client, password_client):
    file_user = open("data_username.txt", "a")
    file_pass = open("data_password.txt", "a")
    file_user.write(username_client + "\n")
    file_pass.write(password_client + "\n")
    file_user.close()
    file_pass.close()