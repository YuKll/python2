#!/usr/bin/python
# -*- coding: utf-8 -*-

import time,threading
#from multiprocessing import Pool
from multiprocessing import Process, Queue
import os

class test(object):
	

	def __init__(self):
		self.src = Queue()
		self.ips = []
	
	def loop(self):
		ip = self.src.get(True)
		print ('%s get' % ip)
		time.sleep(2)
	
	def test1(self):
		print('test1 runing...')
		time.sleep(3)
		print('test1 ended')
	def test2(self):
		time.sleep(3)

	def start_thread(self):
		
		start = time.time()		
		
		with open('./ip.txt', 'r') as fp:
			for line in fp.readlines():
				ip = line.strip()
				self.ips.append(ip)
		threads = []
        	for ip in self.ips:
			self.src.put(ip)
			
			

		for i in range(5):
			t = threading.Thread(target=test.loop, args=(self,))
			threads.append(t)
#			t1 = threading.Thread(target=test.test1, args=(self,))
#			threads.append(t1)
		
		for thr in threads:
			thr.start()
		for thr in threads:
			thr.join()
		
		end = time.time()
		print ('run %s seconds' % (end-start))

if __name__=='__main__':
	b = test()
	b.start_thread()
