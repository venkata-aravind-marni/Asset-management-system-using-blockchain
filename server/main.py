import configparser

import time
import json
import datetime
from datetime import timedelta

from mqttMain import MQtt



m = MQtt("iot.eclipse.org",1883,"sub")
m.connect()
# while True:
# 	if (m.payload!=None):
# 		print m.payload			


		