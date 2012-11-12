import os
from __functions import *

def getStatus ( mountpoint="/" ) :
	failed = False
	result = dict()
	
	if not os.path.exists(mountpoint):
		result['NOT_EXISTING'] = True
		failed = True

	if not failed:
		result['is_mountpoint'] = os.path.ismount(mountpoint)
		r = getStatvfs(mountpoint)
		for x in r.iterkeys():
			result[x] = r[x]
		
		result['stats']['device'] = getDevice(mountpoint)

	return result
