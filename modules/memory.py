import re

## get_meminfo() written by Ray Slakinski (http://forrst.com/people/rays)
def get_info():
    """
    dict of data from meminfo (str:int).
    Values are in kilobytes.
    """
    re_parser = re.compile(r'^(?P<key>\S*):\s*(?P<value>\d*)\s*kB')
    result = dict()
    for line in open('/proc/meminfo'):
        match = re_parser.match(line)
        if not match:
            continue # skip lines that don't parse
        key, value = match.groups(['key', 'value'])
        result[key] = int(value)
    return result
