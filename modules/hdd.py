import os
import _functions

def get_info ( mountpoint="/" ) :
	failed = False
	result = dict()

	if not os.path.exists(mountpoint):
		raise _functions.ModuleError(__name__, \
			'PATH_DOES_NOT_EXIST \'{0}\''.format(mountpoint))

	result['is_mountpoint'] = os.path.ismount(mountpoint)
	r = _functions.get_statvfs(mountpoint)
	for x in r.iterkeys():
		result[x] = r[x]

	result['stats']['device'] = _functions.get_device(mountpoint)

	return result
