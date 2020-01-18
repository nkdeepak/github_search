
from github import Github
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

user_name = config['LOGIN']['username']
password = config['LOGIN']['passwrd']
# Authenticating using username and password

g = Github(user_name, password)

users = g.search_users(query="Natural language processing language:python location:India location:Netherlands repos:>5")
counter = 9
for user in users:
    if counter < 11:
        print(user.login + ' | ' + user.url + ' | ' + user.html_url)
        counter +=1

#for repo in g.get_user().get_repos():
#    print(repo.name)