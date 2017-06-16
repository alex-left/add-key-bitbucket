# README #

Simple script to add a Read only ssh public key (deploy key) in a Bitbucket repo. 

## USAGE
usage: add-key.py [-h] [-u USER] -r REPO -n NAME -k KEY [-l LOGIN] [-p PASSWD]

add a public ssh deploy key in a bitbucket repo 
Maybe you want set hardcoded user/pass

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  owner of the repo
  -r REPO, --repo REPO  name of the repo
  -n NAME, --name NAME  name of the key
  -k KEY, --key KEY     public ssh-key
  -l LOGIN, --login LOGIN
                        user for login in BB
  -p PASSWD, --passwd PASSWD
                        password for login in BB
