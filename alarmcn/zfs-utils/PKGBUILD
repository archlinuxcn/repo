# Maintainer: Kevin Stolp <kevinstolp@gmail.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Iacopo Isimbaldi <isiachi@rhye.it>

pkgname=zfs-utils
pkgver=2.2.1
pkgrel=2
pkgdesc="Userspace utilities for the Zettabyte File System."
arch=("i686" "x86_64" "aarch64")
url="https://zfsonlinux.org/"
license=('CDDL')
optdepends=('python: for arcstat/arc_summary/dbufstat')
source=("https://github.com/zfsonlinux/zfs/releases/download/zfs-${pkgver}/zfs-${pkgver}.tar.gz"{,.asc}
        "https://github.com/openzfs/zfs/commit/30d581121bb122c90959658e7b28b1672d342897.patch"
        "zfs-node-permission.conf"
        "zfs.initcpio.install"
        "zfs.initcpio.hook")
sha256sums=('4ff2de43d39710283ae8ff1744aa96e6cdc83c8efe86a715294d4f6bc34a8e8e'
            'SKIP'
            '0a066b4c5f2bbe87dd02c19b4fb3bd51c7a237ed5ea23c5090e5915a1af3b10c'
            '7ad45fd291aa582639725f14d88d7da5bd3d427012b25bddbe917ca6d1a07c1a'
            '2f09c742287f4738c7c09a9669f8055cd63d3b9474cd1f6d9447152d11a1b913'
            '15b5acea44225b4364ec6472a08d3d48666d241fe84c142e1171cd3b78a5584f')
b2sums=('c3ff95c892024a11ee5c266b10e3354074606665a201fbab16e1ed12550340e0d991d98bd74f794331b68bd16cd6147a9e8937b8cda72d454abce72a22bafec6'
        'SKIP'
        '26d1aebb0293cf2ab555c119bea7d991e0ff80c4d72f7707d2c4dad945d67d6f489324b914fa884f1f2d16cba6db63a85d85257da3400d7469cb4a12c88759d0'
        '7eb3408b1354a4dd504000739101afc7ec0aed1afcdfa029552bf6989e9a8cd4a95b3d3563b3fb7902afa30a80fb01a3f5a2d5af82f9c734c48b5cc23aac25ca'
        'cb774227f157573f960bdb345e5b014c043a573c987d37a1db027b852d77a5eda1ee699612e1d8f4a2770897624889f1a3808116a171cc4c796a95e3caa43012'
        '779c864611249c3f21d1864508d60cfe5e0f5541d74fb3093c6bdfa56be2c76f386ac1690d363beaee491c5132f5f6dbc01553aa408cda579ebca74b0e0fd1d0')
validpgpkeys=('4F3BA9AB6D1F8D683DC2DFB56AD860EED4598027'  # Tony Hutter (GPG key for signing ZFS releases) <hutter2@llnl.gov>
              'C33DF142657ED1F7C328A2960AB9E991C6AF658B') # Brian Behlendorf <behlendorf1@llnl.gov>
backup=('etc/default/zfs'
        'etc/zfs/zed.d/zed.rc')

prepare() {
    cd "${srcdir}"/zfs-${pkgver}

    # Backport fix for issue related to file corruption. (https://github.com/openzfs/zfs/issues/15526)
    patch -p1 -i ../30d581121bb122c90959658e7b28b1672d342897.patch

    # pyzfs is not built, but build system tries to check for python anyway
    ln -sf /bin/true python3-fake

    autoreconf -fi
}

build() {
    # Disable tree vectorization. Related issues:
    # https://github.com/openzfs/zfs/issues/13605
    # https://github.com/openzfs/zfs/issues/13620
    export CFLAGS="$CFLAGS -fno-tree-vectorize"
    export CXXFLAGS="$CXXFLAGS -fno-tree-vectorize"

    cd "${srcdir}"/zfs-${pkgver}

    ./configure --prefix=/usr \
                --sysconfdir=/etc \
                --sbindir=/usr/bin \
                --with-mounthelperdir=/usr/bin \
                --with-udevdir=/usr/lib/udev \
                --libexecdir=/usr/lib \
                --localstatedir=/var \
                --with-python="$PWD/python3-fake" \
                --enable-pyzfs=no \
                --enable-systemd \
                --with-config=user
    make
}

package() {
    cd "${srcdir}"/zfs-${pkgver}

    make DESTDIR="${pkgdir}" install
    install -D -m644 contrib/bash_completion.d/zfs "${pkgdir}"/usr/share/bash-completion/completions/zfs

    # Fix for permissions being overwritten on /dev/zfs. Related issues:
    # https://github.com/openzfs/zfs/issues/15146
    # https://github.com/systemd/systemd/issues/28653
    install -D -m644 "${srcdir}"/zfs-node-permission.conf "${pkgdir}"/usr/lib/tmpfiles.d/zfs-node-permission.conf

    # Remove uneeded files
    rm -r "${pkgdir}"/etc/init.d
    rm -r "${pkgdir}"/etc/sudoers.d #???
    # We're experimenting with dracut in [extra], so start installing this.
    #rm -r "${pkgdir}"/usr/lib/dracut
    rm -r "${pkgdir}"/usr/lib/modules-load.d
    rm -r "${pkgdir}"/usr/share/initramfs-tools
    rm -r "${pkgdir}"/usr/share/zfs/*.sh
    rm -r "${pkgdir}"/usr/share/zfs/{runfiles,test-runner,zfs-tests}

    install -D -m644 "${srcdir}"/zfs.initcpio.hook "${pkgdir}"/usr/lib/initcpio/hooks/zfs
    install -D -m644 "${srcdir}"/zfs.initcpio.install "${pkgdir}"/usr/lib/initcpio/install/zfs
}
