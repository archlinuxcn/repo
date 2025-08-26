# Maintainer: Kevin Stolp <kevinstolp@gmail.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Iacopo Isimbaldi <isiachi@rhye.it>

pkgname=zfs-utils
pkgver=2.3.4
pkgrel=1
pkgdesc="Userspace utilities for the Zettabyte File System."
arch=("i686" "x86_64" "aarch64")
url="https://zfsonlinux.org/"
license=('CDDL')
optdepends=('python: for arcstat/arc_summary/dbufstat')
source=("https://github.com/zfsonlinux/zfs/releases/download/zfs-${pkgver}/zfs-${pkgver}.tar.gz"{,.asc}
        "zfs-node-permission.conf"
        "zfs.initcpio.install"
        "zfs.initcpio.hook"
        "zfs.initcpio.zfsencryptssh.install")
sha256sums=('9ec397cf360133161a1180035f3e7d6962186ed2b3457953a28d45aa883fa495'
            'SKIP'
            '7ad45fd291aa582639725f14d88d7da5bd3d427012b25bddbe917ca6d1a07c1a'
            '2f09c742287f4738c7c09a9669f8055cd63d3b9474cd1f6d9447152d11a1b913'
            '15b5acea44225b4364ec6472a08d3d48666d241fe84c142e1171cd3b78a5584f'
            'ac9ed396465e26fa6896762c52a93eb7aaf8af6d7b2c69bd826d219ff821b2c9')
b2sums=('e7619445a9138475e51e1578cb4e85032570830faba5aab44013a652596a07e49cf602acfe7fd0e5411199d11614d4686cc3f14fddf3062695ce3da922075efd'
        'SKIP'
        '7eb3408b1354a4dd504000739101afc7ec0aed1afcdfa029552bf6989e9a8cd4a95b3d3563b3fb7902afa30a80fb01a3f5a2d5af82f9c734c48b5cc23aac25ca'
        'cb774227f157573f960bdb345e5b014c043a573c987d37a1db027b852d77a5eda1ee699612e1d8f4a2770897624889f1a3808116a171cc4c796a95e3caa43012'
        '779c864611249c3f21d1864508d60cfe5e0f5541d74fb3093c6bdfa56be2c76f386ac1690d363beaee491c5132f5f6dbc01553aa408cda579ebca74b0e0fd1d0'
        'fcd871d72c62a7c99d6cf29cb40a4751bfc08238ff39e8c9440d119754e92ded4705414710db86e99d044011f3524e54c778bda94696dde2c06b3289da6628d0')
validpgpkeys=('4F3BA9AB6D1F8D683DC2DFB56AD860EED4598027'  # Tony Hutter (GPG key for signing ZFS releases) <hutter2@llnl.gov>
              'C33DF142657ED1F7C328A2960AB9E991C6AF658B') # Brian Behlendorf <behlendorf1@llnl.gov>
backup=('etc/default/zfs'
        'etc/zfs/zed.d/zed.rc')

prepare() {
    cd "${srcdir}"/zfs-${pkgver}

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
                --without-libunwind \
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
    install -D -m644 "${srcdir}"/zfs.initcpio.zfsencryptssh.install "${pkgdir}"/usr/lib/initcpio/install/zfsencryptssh
}
