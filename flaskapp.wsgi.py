#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0,"/home/k/MySites/akadrone")
from  aka import app as application

application.secret_key = 'akadrone secret key'