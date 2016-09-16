#!/bin/bash

build() {
    map add_module \
        zavl \
        znvpair \
        zunicode \
        zcommon \
        zfs \
        zpios \
        spl \
        splat \
        zlib_deflate

    map add_binary \
        arcstat.py \
        dbufstat.py \
        fsck.zfs \
        mount.zfs \
        zdb \
        zed \
        zfs \
        zhack \
        zinject \
        zpios \
        zpool \
        zstreamdump \
        ztest \
        splat \
        hostid \
        /lib/udev/vdev_id \
        /lib/udev/zvol_id

    map add_file \
        /lib/udev/rules.d/60-zvol.rules \
        /lib/udev/rules.d/69-vdev.rules \
        /lib/udev/rules.d/90-zfs.rules

    map add_dir \
        /etc/zfs/zed.d

    add_runscript

    # allow mount(8) to "autodetect" ZFS
    echo 'zfs' >>"$BUILDROOT/etc/filesystems"

    [[ -f /etc/zfs/zpool.cache ]] && add_file "/etc/zfs/zpool.cache"
    [[ -f /etc/modprobe.d/zfs.conf ]] && add_file "/etc/modprobe.d/zfs.conf"
    [[ -f /etc/hostid ]] && add_file "/etc/hostid"
}

help() {
    cat<<HELPEOF
This hook allows you to use ZFS as your root filesystem.

Command Line Setup:

    You can append the following arguments to your kernel parameters list. See
    https://wiki.archlinux.org/index.php/Kernel_parameters for more information.

    To use ZFS as your boot filesystem:

        zfs=bootfs or zfs=auto or root=zfs

    To use a pool or dataset:

        zfs=<pool/dataset>

    To force importing of a ZFS pool:

        zfs_force=1

        If set to 1, this will use "zpool import -f" when attempting to import
        pools.

    To search for devices in a directory other than "/dev":

        zfs_import_dir=/dev/disk/by-uuid
            or
        zfs_import_dir=/dev/disk/by-partuuid
            or
        zfs_import_dir=/dev/disk/by-path
            etc.

    Following initcpio convention, the 'rw' option must be specified to load the
    pool as read/write. Pools are loaded as read only by default.

Examples:

    To use bootfs on your pool, use

        zfs=bootfs rw

    This will setup your root using tank/root zfs pool.

        zfs=tank/root rw

If you want to set properties for zfs-on-linux module, you should add them to
/etc/modprobe.d/zfs.conf and then rebuild initcpio.

HELPEOF
}

# vim: set ts=4 sw=4 ft=sh et:
