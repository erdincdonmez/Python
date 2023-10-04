import os
print(os.stat("rehber.txt"))

"""
st_mode: It represents file type and file mode bits (permissions).
st_ino: It represents the inode number on Unix and the file index on Windows platform.
st_dev: It represents the identifier of the device on which this file resides.
st_nlink: It represents the number of hard links.
st_uid: It represents the user identifier of the file owner.
st_gid: It represents the group identifier of the file owner.
st_size: It represents the size of the file in bytes.
st_atime: It represents the time of most recent access. It is expressed in seconds.
st_mtime: It represents the time of most recent content modification. It is expressed in seconds.
st_ctime: It represents the time of most recent metadata change on Unix and creation time on Windows. It is expressed in seconds.
st_atime_ns: It is same as st_atime but the time is expressed in nanoseconds as an integer.
st_mtime_ns: It is same as st_mtime but the time is expressed in nanoseconds as an integer.
st_ctime_ns: It is same as st_ctime but the time is expressed in nanoseconds as an integer.
st_blocks: It represents the number of 512-byte blocks allocated for file.
st_rdev: It represents the type of device, if an inode device.
st_flags: It represents the user defined flags for file.
"""