import os
from _functions import *

def get_info ( mountpoint="/" ) :
	failed = False
	result = dict()
	
	if not os.path.exists(mountpoint):
		raise ModuleError('PATH_DOES_NOT_EXIST')

	result['is_mountpoint'] = os.path.ismount(mountpoint)
	r = getStatvfs(mountpoint)
	for x in r.iterkeys():
		result[x] = r[x]
	
	result['stats']['device'] = getDevice(mountpoint)

	return result
