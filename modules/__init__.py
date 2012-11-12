from .. import conf

__all__ = []

if "ramdisk_dir" in conf.config and "ramdisk" in conf.enabledModules:
    __all__.append("ramdisk")
    import ramdisk

if "hdd" in conf.enabledModules:
    __all__.append("hdd")
    import hdd
