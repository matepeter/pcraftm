import os

class ModuleError ( Exception ):
	""" Base class for errors raised by Pcraftm modules """ 
	def __init__(self, module, message):
		self.module = module
		self.message = message
	def __str__(self):
		return "{0}: {1}".format(self.module, self.message)

def get_statvfs ( path ):
	result = dict()
	
	stats = dict()
	try:
		st = os.statvfs(path)
	except Exception:
		raise ModuleError(__name__, "STATVFS_FAILURE")
	else:
		# disk usage
		stats['du_free'] = st.f_bavail * st.f_frsize
		stats['du_total'] = st.f_blocks * st.f_frsize
		stats['du_used'] = (st.f_blocks - st.f_bfree) * st.f_frsize
		# inodes
		stats['in_total'] = st.f_files
		stats['in_free'] = st.f_favail
		stats['in_used'] = st.f_files - st.f_ffree

		result['stats'] = stats

	return result

def get_device ( path ):
	# props to Anders Waldenborg for this snippet
	dev = os.stat(path).st_dev
	major, minor = os.major(dev), os.minor(dev)

	from glob import glob
	needle = "%d:%d" % (major, minor)
		
	files = glob("/sys/class/block/*/dev")
	for f in files:
		try:
			if file(f).read().strip() == needle:
				return os.path.dirname(f).rsplit('/', 1)[1]
		except Exception:
			raise ModuleError(__name__, \
				'ERROR_READING \'{0}\''.format(os.path.abspath(f)))

	return None
