import datetime
import re

now = datetime.datetime.now()
date = '{}{:02}{:02}'.format(now.year, now.month, now.day)

with open('setup.py', 'r+') as f:
    text = f.read()
    text = re.sub('name="eclipse-zenoh"', 'name="eclipse-zenoh-nightly"', text)
    #text = re.sub(r'version="(.*dev)0"', r'version="\1{}"'.format(date), text)
    text = re.sub(r'version="(.*dev)0"', r'version="\g<1>{}"'.format(date), text)
    f.seek(0)
    f.write(text)
    f.truncate()

