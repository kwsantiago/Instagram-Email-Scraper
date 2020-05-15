from igramscraper.instagram import Instagram
from time import sleep

def getUser(username):
    account = instagram.get_account(username)
    sleep(1)
    name = account.full_name

def main():
    instagram = Instagram()
    username = 'golive_entertainment'
    getUser(username)

main()
