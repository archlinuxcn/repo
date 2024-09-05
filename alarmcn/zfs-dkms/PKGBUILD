# Maintainer: Kevin Stolp <kevinstolp@gmail.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Iacopo Isimbaldi <isiachi@rhye.it>

pkgname=zfs-dkms
pkgver=2.2.6
pkgrel=1
pkgdesc="Kernel modules for the Zettabyte File System."
arch=('any')
url="https://zfsonlinux.org/"
license=('CDDL')
provides=("ZFS-MODULE=${pkgver}" "SPL-MODULE=${pkgver}")
# ambiguous, provided for backwards compat, pls don't use
provides+=('zfs')
source=("https://github.com/zfsonlinux/zfs/releases/download/zfs-${pkgver}/zfs-${pkgver}.tar.gz"{,.asc}
        "enforce_kernel_max_version.patch::https://github.com/openzfs/zfs/commit/2b481b5477d3a95d0eab723c6639f7114e146ae1.patch?full_index=1"
        "0001-only-build-the-module-in-dkms.conf.patch")
sha256sums=('c92e02103ac5dd77bf01d7209eabdca55c7b3356aa747bb2357ec4222652a2a7'
            'SKIP'
            'c372060ce43be8fd0fd8b2ea2d147e048d51d6c8713433b15a5f29085f90106d'
            '8d5c31f883a906ab42776dcda79b6c89f904d8f356ade0dab5491578a6af55a5')
b2sums=('0bbe36df779aaf19460a75725af9c9b13e64e77a6020974ad18d60d9fd52db2ddd6ea98b3e6c7451195bdfb347b8aab51db9b3f9a7c15c77bff47329bbd07dd2'
        'SKIP'
        'dd902faa9d8ddc2ec5eeba3810f719764da05bae2e2af80b72dac619c979625e3e366762bdfab72a97b487128b2f281c833a2c3ebe73c5999c49949e478bcffc'
        '58dc2494e71b50833d44c126b72acad52e9817626542afbc245b7ba82009e8c8252ebde6023592aac42d9942207e7655c0a421da9067fbdd619746ebc372d791')
validpgpkeys=('4F3BA9AB6D1F8D683DC2DFB56AD860EED4598027'  # Tony Hutter (GPG key for signing ZFS releases) <hutter2@llnl.gov>
              'C33DF142657ED1F7C328A2960AB9E991C6AF658B') # Brian Behlendorf <behlendorf1@llnl.gov>

prepare() {
    cd "${srcdir}"/${pkgname%-dkms}-${pkgver}

    patch -p1 -i ../0001-only-build-the-module-in-dkms.conf.patch

    # Apply patch to warn on unsupported kernel version. (https://github.com/openzfs/zfs/pull/15986)
    patch -p1 -i ../enforce_kernel_max_version.patch

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
