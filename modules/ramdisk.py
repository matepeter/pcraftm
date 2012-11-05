import os
import subprocess
from . import conf
from __functions import *

def getStatus ( ) :
	return getStatvfs(conf.config['ramdisk_dir'])
