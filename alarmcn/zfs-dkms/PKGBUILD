# Maintainer: Kevin Stolp <kevinstolp@gmail.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Iacopo Isimbaldi <isiachi@rhye.it>

pkgname=zfs-dkms
pkgver=2.2.3
pkgrel=2
pkgdesc="Kernel modules for the Zettabyte File System."
arch=('any')
url="https://zfsonlinux.org/"
license=('CDDL')
provides=("ZFS-MODULE=${pkgver}" "SPL-MODULE=${pkgver}")
# ambiguous, provided for backwards compat, pls don't use
provides+=('zfs')
source=("https://github.com/zfsonlinux/zfs/releases/download/zfs-${pkgver}/zfs-${pkgver}.tar.gz"{,.asc}
        "https://github.com/openzfs/zfs/commit/2b481b5477d3a95d0eab723c6639f7114e146ae1.patch"
        "0001-only-build-the-module-in-dkms.conf.patch")
sha256sums=('30a512f34ec5c841b8b2b32cc9c1a03fd49391b26c9164d3fb30573fb5d81ac3'
            'SKIP'
            'b3444bbb71b508e12dcbce1a61d01275960f6c38b8db9c163aced83e4cd092c8'
            '8d5c31f883a906ab42776dcda79b6c89f904d8f356ade0dab5491578a6af55a5')
b2sums=('f83439aa929609191a048dd326b2a15e0f57c72d2901cbfb205b81a29aa42dab49b42eb61647ca3eaed17518b8c907e81343364bfecf83ed441271648f8efd4b'
        'SKIP'
        '245f489ba2f916e95fbbc9616ac7d9f6149dd3b6c63580b25c0af69aa2ad96d2ed28bf4e1446cbf7c8299f5c14de4712c931d3f4949bb8149d5a966310ca6977'
        '58dc2494e71b50833d44c126b72acad52e9817626542afbc245b7ba82009e8c8252ebde6023592aac42d9942207e7655c0a421da9067fbdd619746ebc372d791')
validpgpkeys=('4F3BA9AB6D1F8D683DC2DFB56AD860EED4598027'  # Tony Hutter (GPG key for signing ZFS releases) <hutter2@llnl.gov>
              'C33DF142657ED1F7C328A2960AB9E991C6AF658B') # Brian Behlendorf <behlendorf1@llnl.gov>

prepare() {
    cd "${srcdir}"/${pkgname%-dkms}-${pkgver}

    patch -p1 -i ../0001-only-build-the-module-in-dkms.conf.patch

    # Apply patch to warn on unsupported kernel version. (https://github.com/openzfs/zfs/pull/15986)
    patch -p1 -i ../2b481b5477d3a95d0eab723c6639f7114e146ae1.patch

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
