pkgname=ntfs3-dkms
pkgver=5.17
pkgrel=1
epoch=1
pkgdesc="NTFS3 is fully functional NTFS Read-Write driver. The driver works with NTFS versions up to 3.1."
arch=('any')
url='https://www.kernel.org/doc/html/latest/filesystems/ntfs3.html'
license=('GPL2')
depends=('dkms')
provides=('NTFS3-MODULE' 'ntfs3')
conflicts=('ntfs3')
options=('!strip' '!emptydirs')

_snapshot="linux-${pkgver}"
_archive="${_snapshot}.tar.gz"

source=(
    "${_archive}::https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/snapshot/${_archive}"
    "Makefile.patch"
    "dkms.conf"
    "kernel-5.12-backport.patch"
    "kernel-5.14-backport.patch"
    "kernel-5.15-backport.patch"
    "kernel-5.16-backport.patch"
)

sha256sums=(
    'f58338c5b06314559a269afe70b33b9b0b75cc2fe5e8a537ac29f70caa6e489b'
    'fd4cf0e2dc160efecc55d4ea99667669b870599e4e81be435ec2201381b7e2ac'
    '9cb620446fc07ade4018637313a749e192d44a03e1f8b10529746730bacf6feb'
    '44ce1edf931aec236d3dcb5a08441f4c03ccd60fdcd5ba949989c11938eeb371'
    '869165f7b738a5fee41f1015d531459650d2c862fa2aaed252e692474d77c84c'
    '26613999994cec08dfa4b53e9a5c1f97174ac2fc2b7f99c52b7ff7b88fdd1a45'
    '8d397fd1c7d64835f712d47bf425732ae8abe8305aea570f1b53cfca9c8a97cf'
)

noextract=("${_archive}")

prepare() {
    cd "${srcdir}"
    tar --strip-components=2 -xf "${_archive}" "${_snapshot}/fs/ntfs3"

    cd "ntfs3"
    patch -p0 -N -i "${srcdir}/Makefile.patch"

    # For testing
    # patch -p1 -N -i "${srcdir}/kernel-5.16-backport.patch"
    # patch -p1 -N -i "${srcdir}/kernel-5.15-backport.patch"
    # patch -p1 -N -i "${srcdir}/kernel-5.14-backport.patch"
    # patch -p1 -N -i "${srcdir}/kernel-5.12-backport.patch"
}

package() {
    local dest="${pkgdir}/usr/src/ntfs3-${pkgver}"
    install -dm755 "${dest}"

    cd "${srcdir}"
    install -Dm644 -t "${dest}" "dkms.conf"
    install -dm755 "${dest}/patches" && cp -t "$_" "kernel-"*.patch

    cd "ntfs3"
    cp -rt "${dest}" *
}
