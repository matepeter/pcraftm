import os
from _functions import *

def get_info ( path ) :
	failed = False
	result = dict()

	if not os.path.ismount(path):
		raise ModuleError(__name__, "NO_RAMDISK")

	r = getStatvfs(path)
	for x in r.iterkeys():
		result[x] = r[x]

	return result
