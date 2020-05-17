from igramscraper.instagram import Instagram
from time import sleep
import sys
import re

def getUser(username):
    instagram = Instagram()
    symbol = '@'
    account = instagram.get_account(username)
    sleep(1)
    try:
        name = account.full_name
        if(symbol in name):
            name = re.findall('\S+@\S+', name)
            return name
        else:
            bio = account.biography
            if(symbol in bio):
                bio = re.findall('\S+@\S+', bio)
                return bio
    except:
        return

def main():
    username = sys.argv[1]
    print(getUser(username))

main()
