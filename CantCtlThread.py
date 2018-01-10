#!/usr/bin/python
# -*- coding: utf-8 -*-

import time,threading
import os

	


def loop(self):
	print ('%s get' % self)
	time.sleep(2)

def test1(self):
	print('test1 runing...')
	time.sleep(3)
	print('test1 ended')
def test2(self):
	time.sleep(3)

def start_thread():
	
	start = time.time()		
	
        
        ips = []

	with open('./ip.txt', 'r') as fp:
		for line in fp.readlines():
			ip = line.strip()
			ips.append(ip)
	threads = []
		
	for ip in ips:
		t = threading.Thread(target=loop, args=(ip,))
		threads.append(t)
	
	for thr in threads:
		thr.start()
	for thr in threads:
		thr.join()
	
	end = time.time()
	print ('run %s seconds' % (end-start))

if __name__=='__main__':
    start_thread()
