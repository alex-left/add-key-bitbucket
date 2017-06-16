#!/usr/bin/env python3

import requests, json, argparse

## HELP & ARGS
parser = argparse.ArgumentParser(description="""add a public ssh deploy key in a bitbucket repo.
                                    For your convenience maybe you want set hardcoded user/pass""")
parser.add_argument("-u", "--user", help="owner of the repo", type=str, default="mrmilu")
parser.add_argument("-r", "--repo", help="name of the repo", type=str, required=True)
parser.add_argument("-n", "--name", help="name of the key", type=str, required=True)
parser.add_argument("-k", "--key", help="public ssh-key", type=str, required=True)
parser.add_argument("-l", "--login", help="user for login in BB", type=str, required=False)
parser.add_argument("-p", "--passwd", help="password for login in BB", type=str, required=False)
args = parser.parse_args()

## DATA
urlbase="https://api.bitbucket.org/1.0/repositories/"
action="deploy-keys"
login_user=args.login
login_pass=args.passwd
user=args.user
repo=args.repo
keyname=args.name
key=args.key


## CODE
payload = {"accountname": user,
           "repo_slug": repo,
           "label": keyname,
           "key": key }

post = requests.post(urlbase + "/".join([user, repo, action]),
                   auth=(login_user, login_pass),
                   data=json.dumps(payload),
                   headers = {'content-type': 'application/json'})

if post.ok:
    print("Parece que ha ido OK:")
    print(post.text)
else:
    print("ERROR:")
    print(post.text)
