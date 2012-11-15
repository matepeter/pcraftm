import os

def getStatvfs ( path ):
	result = dict()
	
	stats = dict()
	try:
		# disk usage
		st = os.statvfs(path)
		stats['du_free'] = st.f_bavail * st.f_frsize
		stats['du_total'] = st.f_blocks * st.f_frsize
		stats['du_used'] = (st.f_blocks - st.f_bfree) * st.f_frsize
		# inodes
		stats['in_total'] = st.f_files
		stats['in_free'] = st.f_favail
		stats['in_used'] = st.f_files - st.f_ffree

		result['stats'] = stats
	except:
		result['UNKNOWN_ERROR'] = True
		failed = True
	return result

def getDevice ( path ):
	# props to Anders Waldenborg for this snippet
	dev = os.stat(path).st_dev
	major, minor = os.major(dev), os.minor(dev)

	from glob import glob
	needle = "%d:%d" % (major, minor)
		
	files = glob("/sys/class/block/*/dev")
	for f in files:
		if file(f).read().strip() == needle:
			return os.path.dirname(f).rsplit('/', 1)[1]

	return None
