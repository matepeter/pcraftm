import os
import _functions

def get_info ( path ) :
	failed = False
	result = dict()

	if not os.path.ismount(path):
		raise _functions.ModuleError(__name__, "NO_RAMDISK")

	r = _functions.get_statvfs(path)
	for x in r.iterkeys():
		result[x] = r[x]

	return result
