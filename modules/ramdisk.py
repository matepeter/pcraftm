import __functions
import os
import subprocess
from . import conf

def getStatus ( ) :
	result = dict()
	rd_failed = False
	
	## RAMDISK
	if not os.path.ismount(conf.config['ramdisk_dir']):
		result['RD_NOT_MOUNTED'] = True
		rd_failed = True
	
	if not rd_failed:
		rd = dict()
		try:
			# space
			dfh = subprocess.Popen(["df", "-h", conf.config['ramdisk_dir']], stdout=subprocess.PIPE)
			output = dfh.communicate()[0]
			rd['device'], rd['size'], rd['used'], rd['available'], rd['percentage'], rd['mountpoint'] = \
				output.split("\n")[1].split()
			
			# inodes
			dfi = subprocess.Popen(["df", "-i", conf.config['ramdisk_dir']], stdout=subprocess.PIPE)
			output = dfi.communicate()[0]
			rd['in_device'], rd['in_total'], rd['in_used'], rd['in_free'], rd['in_percentage'], rd['in_mountpoint'] = \
				output.split("\n")[1].split()
			
			result['rd'] = rd
		except:
			result['RD_DF_ERROR'] = True
			rd_failed = True
	return result
