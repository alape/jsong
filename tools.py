from uos import statvfs

def fs_stat():
    stat = statvfs("/")
    fs_size = stat[2] * stat[1]
    fs_free = stat[3] * stat[1]

    return (fs_size // 1024, fs_free // 1024)
