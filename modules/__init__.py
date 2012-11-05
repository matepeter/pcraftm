from .. import conf

__all__ = []

if "ramdisk_dir" in conf.config:
    __all__.append("ramdisk")
    import ramdisk
