import urllib
from datetime import datetime
from urllib.request import urlretrieve
import time


while 1:
	try:
		response = urllib.FancyURLopener('http://nntc.nnov.ru:58080/?action=snapshot')
		if response.getcode() != 200:
			print("server Not connected")
			time.sleep(30)
			continue
"""		else:
			while 2:
				localTime = datetime.strftime(datetime.now(), "%Y-%m-%d %H-%M-%S")
				name = localTime+".jpg"
				urlretrieve("http://nntc.nnov.ru:58080/?action=snapshot",str(name))
				time.sleep(20)
				break
			else:
				break
	except Exception(" error"):
		break """

