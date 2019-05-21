#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Adrian Perez <aperez@igalia.com>
#
# Distributed under terms of the MIT license.

from os import path, unlink, fstat, utime, chmod


VERBOSE = False
def verbose(fmt, *arg):
    if VERBOSE:
        from sys import stdout
        stdout.write(fmt % arg)


def is_python_shebang(line):
    return line.startswith("#!") and \
            (line.split()[-1].startswith("python") or
             line.split("/")[-1].startswith("python"))


def add_shebang(fpath, fd, shebang=None):
    if shebang is None:
        shebang = "#! /usr/bin/env python2"

    # Save metadata of the open file.
    stat = fstat(fd.fileno())

    # Unlink the original file name. The contents will be available
    # for reading as long as we keep an open file descriptor to it.
    unlink(fpath)

    # Write new shebang as first line, then the original contents
    with open(fpath, "w") as outfd:
        outfd.write(shebang)
        outfd.write("\n")
        [outfd.write(chunk) for chunk in fd]

    # Restore original file metadata.
    utime(fpath, (stat.st_atime, stat.st_mtime))
    chmod(fpath, stat.st_mode)


def check_files(arg, dirname, fnames):
    assert arg is None
    for fname in fnames:
        if fname.startswith("."):
            continue
        fpath = path.join(dirname, fname)
        if not path.isfile(fpath) or path.islink(fpath):
            continue
        with open(fpath, "rU") as fd:
            line = fd.readline().strip()
            if is_python_shebang(line):
                verbose("Fixing: %s\n", fpath)
                add_shebang(fpath, fd)
            else:
                verbose("Skipped: %s\n", fpath)


if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    if len(argv) > 0 and argv[0] in ("-v", "--verbose"):
        VERBOSE = True
        argv = argv[1:]

    if len(argv) == 0:
        argv.append(".")

    [path.walk(top, check_files, None) for top in argv]
