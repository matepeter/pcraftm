import os
from __functions import *

def getStatus ( path ) :
	failed = False
	result = dict()

	if not os.path.ismount(path):
		result['NOT_MOUNTED'] = True
		failed = True

	if not failed:
		r = getStatvfs(path)
		for x in r.iterkeys():
			result[x] = r[x]

	return result
