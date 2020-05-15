from igramscraper.instagram import Instagram
from time import sleep
import sys

def getUser(username):
    instagram = Instagram()
    symbol = '@'
    account = instagram.get_account(username)
    sleep(1)
    try:
        name = account.full_name
        if(symbol in name):
            return name
        else:
            bio = account.biography
            if(symbol in bio):
                return bio
    except:
        return

def main():
    username = sys.argv[1]
    print(getUser(username))

main()
