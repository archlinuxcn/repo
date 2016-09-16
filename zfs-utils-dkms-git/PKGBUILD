#
# Maintainer: Iacopo Isimbaldi <isiachi@rhye.it>
#

pkgbase="zfs-dkms-git"
pkgname=("zfs-dkms-git" "zfs-utils-dkms-git")
pkgver=0.6.5_r229_g1ab3678
pkgrel=1
license=('CDDL')
makedepends=("git" "spl-dkms-git")
arch=("i686" "x86_64")
url="http://zfsonlinux.org/"
source=("git+https://github.com/zfsonlinux/zfs.git"
        "zfs.bash-completion-r1"
        "zfs.initcpio.install"
        "zfs.initcpio.hook")
sha256sums=('SKIP'
            'b60214f70ffffb62ffe489cbfabd2e069d14ed2a391fac0e36f914238394b540'
            '1e20071fa61a33874505dae0f2d71bb560f43e7faaea735cbde770ea10c133df'
            '250f1232c464a81cc9c8b8ee05f21d752ebeebbc8614fae1c6d0bc600e816ac1')

pkgver() {
    cd "${srcdir}/zfs"
    git describe --match "zfs-*" --long --tags | sed -e 's|zfs-||' -e 's|-\([0-9]*-g\)|-r\1|' -e 's|[-: ]|_|g'
}

build() {
    cd "${srcdir}/zfs"
    ./autogen.sh

    ./configure --prefix=/usr \
                --sysconfdir=/etc \
                --sbindir=/usr/bin \
                --with-mounthelperdir=/usr/bin \
                --libdir=/usr/lib \
                --datadir=/usr/share \
                --includedir=/usr/include \
                --with-udevdir=/lib/udev \
                --libexecdir=/usr/lib/zfs \
                --with-config=user
    make
}

package_zfs-dkms-git() {
    pkgdesc="Kernel modules for the Zettabyte File System. (Git version)"
    depends=("spl-dkms-git" "zfs-utils-dkms-git=${pkgver}-${pkgrel}" "dkms")
    provides=("zfs")
    conflicts=("zfs-git" "zfs-lts" "zfs-dkms")

    dkmsdir="${pkgdir}/usr/src/zfs-${pkgver%%_*}"
    install -d "${dkmsdir}"
    cp -a ${srcdir}/zfs/. ${dkmsdir}

    cd "${dkmsdir}"
    make clean distclean
    find . -name ".git*" -print0 | xargs -0 rm -fr --
    scripts/dkms.mkconf -v ${pkgver%%_*} -f dkms.conf -n zfs
    chmod g-w,o-w -R .
}

package_zfs-utils-dkms-git() {
    pkgdesc="Kernel module support files for the Zettabyte File System. (Git version)"
    provides=("zfs-utils")
    conflicts=("zfs-utils-git" "zfs-utils-lts" "zfs-utils")

    cd "${srcdir}/zfs"
    make DESTDIR="${pkgdir}" install

    # Remove uneeded files
    rm -r "${pkgdir}"/etc/init.d
    rm -r "${pkgdir}"/usr/lib/dracut
    rm -r "${pkgdir}"/usr/share/initramfs-tools

    # move module tree /lib -> /usr/lib
    cp -r "${pkgdir}"/{lib,usr}
    rm -r "${pkgdir}"/lib

    install -D -m644 "${srcdir}"/zfs.initcpio.hook "${pkgdir}"/usr/lib/initcpio/hooks/zfs
    install -D -m644 "${srcdir}"/zfs.initcpio.install "${pkgdir}"/usr/lib/initcpio/install/zfs
    install -D -m644 "${srcdir}"/zfs.bash-completion-r1 "${pkgdir}"/usr/share/bash-completion/completions/zfs

    mkdir -p "${pkgdir}"/usr/lib/initcpio/install
}
