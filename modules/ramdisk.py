import os
from . import conf
from __functions import *

def getStatus ( ) :
	failed = False
	result = dict()

	if not os.path.ismount(conf.config['ramdisk_dir']):
		result['NOT_MOUNTED'] = True
		failed = True

	if not failed:
		r = getStatvfs(conf.config['ramdisk_dir'])
		for x in r.iterkeys():
			result[x] = r[x]

	return result
