from pyicloud import PyiCloudService
import sys


# Takes a username and password to login to iCloud account
def login(username, pword):
    api = PyiCloudService(username, pword)
    return api


if __name__ == "__main__":
    user = str(sys.argv[1])
    password = str(sys.argv[2])
    if login(user, password):
        print('Successfully logged in!')
    else:
        print('Login Failure')
