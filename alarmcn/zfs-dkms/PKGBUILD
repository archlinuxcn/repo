# Maintainer: Kevin Stolp <kevinstolp@gmail.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Iacopo Isimbaldi <isiachi@rhye.it>

pkgname=zfs-dkms
pkgver=2.1.12
pkgrel=1
pkgdesc="Kernel modules for the Zettabyte File System."
arch=('any')
url="https://zfsonlinux.org/"
license=('CDDL')
conflicts=('spl-dkms')
provides=("ZFS-MODULE=${pkgver}" "SPL-MODULE=${pkgver}" 'spl-dkms')
# ambiguous, provided for backwards compat, pls don't use
provides+=('zfs')
replaces=('spl-dkms')
source=("https://github.com/zfsonlinux/zfs/releases/download/zfs-${pkgver}/zfs-${pkgver}.tar.gz"{,.asc}
        "0001-only-build-the-module-in-dkms.conf.patch")
sha256sums=('64daa26aed3e12c931f6f4413d7527c4ebdb8da35416b356152b5f9fdd4c6e6d'
            'SKIP'
            '8d5c31f883a906ab42776dcda79b6c89f904d8f356ade0dab5491578a6af55a5')
b2sums=('652780e6bf7b63f45909110726d53795fada034f6044c8393fa3980e30217ada6931e3c2bb57210719e3c78c16f973f69287b7e2b475601f4ce12d701d9d96ae'
        'SKIP'
        '58dc2494e71b50833d44c126b72acad52e9817626542afbc245b7ba82009e8c8252ebde6023592aac42d9942207e7655c0a421da9067fbdd619746ebc372d791')
validpgpkeys=('4F3BA9AB6D1F8D683DC2DFB56AD860EED4598027'  # Tony Hutter (GPG key for signing ZFS releases) <hutter2@llnl.gov>
              'C33DF142657ED1F7C328A2960AB9E991C6AF658B') # Brian Behlendorf <behlendorf1@llnl.gov>

prepare() {
    cd "${srcdir}"/${pkgname%-dkms}-${pkgver}

    patch -p1 -i ../0001-only-build-the-module-in-dkms.conf.patch

    # remove unneeded sections from module build
    sed -ri "/AC_CONFIG_FILES/,/]\)/{
/AC_CONFIG_FILES/n
/]\)/n
/^\s*(module\/.*|${pkgname%-dkms}.release|Makefile)/!d
}" configure.ac

    autoreconf -fi
}

build() {
    cd "${srcdir}"/${pkgname%-dkms}-${pkgver}

    ./scripts/dkms.mkconf -n ${pkgname%-dkms} -v ${pkgver} -f dkms.conf
    ./scripts/make_gitrev.sh include/zfs_gitrev.h
}

package() {
    depends=("zfs-utils=${pkgver}" 'dkms')

    cd "${srcdir}"/${pkgname%-dkms}-${pkgver}

    dkmsdir="${pkgdir}/usr/src/${pkgname%-dkms}-${pkgver}"
    install -d "${dkmsdir}"/{config,scripts}
    cp -a configure dkms.conf Makefile.in META ${pkgname%-dkms}_config.h.in ${pkgname%-dkms}.release.in include/ module/ "${dkmsdir}"/
    cp config/compile config/config.* config/missing config/*sh "${dkmsdir}"/config/
    cp scripts/enum-extract.pl scripts/dkms.postbuild "${dkmsdir}"/scripts/
}
