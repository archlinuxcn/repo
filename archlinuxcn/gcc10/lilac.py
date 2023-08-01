from lilaclib import aur_pre_build, edit_file

def pre_build():
    aur_pre_build('gcc10',maintainers=['severach'])

    for line in edit_file('PKGBUILD'):
        if 'sed -i' in line and 'gcc/configure' in line:
            print(line)
            print("sed -i '/HAVE_LIMITS_H/d' libiberty/fibheap.c\n")
            print("sed -i -e '/limits.h/{n;d}' libiberty/fibheap.c\n")
            print("sed -i '/HAVE_FCNTL_H/d' libiberty/pex-unix.c\n")
            print("sed -i -e '/fcntl.h/{n;d}' libiberty/pex-unix.c\n")
        else:
            print(line)
