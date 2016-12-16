#!/usr/bin/python3
from sys import argv
from shutil import rmtree
from os import path
import UinfoFunc
import re

def deldirs( dirlist ):
    for x in dirlist:
        if path.exists( x ):
            rmtree( x )



introduction = """
######################
SetupServer.py
Setup the FTP server.
######################

OPTIONS:
--------

-delall 
    Delete all users.

-del <username1> <username2> ...
    Delete users by username.

-add <username1>:<password1> <username2>:<password2> ...
    Add users.
"""
if len(argv) == 1:
    print( introduction )
    exit()



if argv[1] == "-delall":
    uinfo = UinfoFunc.getUsers()
    deldirs( [ user.get('username') for user in uinfo ] )
    open("Uinfo.txt", "w").close()
elif argv[1] == "-del":
    to_be_deleted = argv[2:]
    uinfo = UinfoFunc.getUsers()
    deldirs( [ x for x in argv[2:] ] )
    new_uinfo = [ user for user in uinfo if user.get('username') not in to_be_deleted ]
    UinfoFunc.writeUsers( new_uinfo )
elif argv[1] == "-add":
    newusers = argv[2:]
    newusers = [ { 'username':x.split(':',1)[0], 'password':x.split(':',1)[1] } for x in newusers ]
    UinfoFunc.writeUsers( UinfoFunc.getUsers() + newusers )
else:
    print("Error in arguments")
