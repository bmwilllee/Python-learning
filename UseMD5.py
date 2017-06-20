#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Willlee

import hashlib

db = {}

def get_md5(password):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()

def register(username, password):
	if username in db or username == '' or password == '':
		print('bad input')
	else:
		db[username] = get_md5(password + username + 'the-Salt')

def login(username, password):
	if username not in db or username == '' or password == '':
		exit('bad input')
	else:
		if db[username] == get_md5(username, password):
			print('welcome %s' % username)
		else:
			print('Please check your password')

if __name__=='__main__':
    while True:
        choose = input('1. regist;\n2. login;\n3. exit.\n')
        if choose == '1':
            register(input('input username:'), input('input password:'))
        elif choose == '2':
            login(input('input username:'), input('input password:'))
        elif choose == '3':
            print(db)
            print('Bye.')
            break
        else:
            print('Input error.')