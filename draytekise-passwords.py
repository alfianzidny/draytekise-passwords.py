#!/usr/bin/env python
import base64
import sys
import urllib


with open(sys.argv[1]) as f:
	for line in f.readlines():
		print urllib.quote_plus(base64.b64encode(line.strip()))
