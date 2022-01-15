pkgname=ntfs3-dkms
pkgver=5.16
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

sha512sums=(
    'e7e2e3208e681eef8557138763e7460418264d8fbad3dbb965cf7d40e9d55800419199de78774458775ca593f550f6b50e7e3bc8fad75edd085d08d1c5933b40'
    '533c249f0f6bd4833faf02d0d92ca1b5802a49afc5feb2e46a7d37275cfca7896db76cd83593f4f313977d278a9a7e92eda550667be2b93910c49cfb68ead4fb'
    'a46d538f3d166741dafcbc880f6322932478170aa0edf17b57a4e9f1543bea4c75970f08b39d67a14d48b63ac7a1c18f3a30fe763660b39ed404933eb0e37308'
    '4b1976b40f67c210ee4052407a359ed8db0709a568387ffacc15e695b43af7c77b53fbe27a3365197521e5c9baa8bd9c7aaffa2f8345be17129216b1ac141fbe'
    '61a1948e3e607dabaca47742777b4ea92fadf9f5416ebaef8c06f1e17aab0f3ced34e900c0cf1ed462303f391f4a4713b5b30a488b349839780bde3248e19f3c'
    '3a9395f5729c14cd8d8bf2ecda566730d90c6990319ed5e33310fa2dbe4d4a33df925950ff652fff338ef0135e5aeecf4b991603bba797847f8f1ef9130420c7'
    'd13e320a127bb3c8988d040d6c27b98981ca4352fb29ca57e5afa9b549f271c33a668beaefd142ca21f8930371aec5aedaaf1d07c157abb05c30f4899b643cdf'
)

noextract=("${_archive}")

prepare() {
    cd "${srcdir}"
    tar xf "${_archive}" "${_snapshot}/fs/ntfs3" --strip-components=2
}

package() {
    cd "${srcdir}"

    local dest=$(install -dm755 "${pkgdir}/usr/src/ntfs3-${pkgver}" && echo "$_")

    install -Dm644 -t "${dest}" "dkms.conf"

    install -dm755 "${dest}/patches" && cp -t "$_" "kernel-"*.patch

    cd "ntfs3"

    patch -p0 -N -i "${srcdir}/Makefile.patch"

    # For testing
    # patch -p1 -N -i "${srcdir}/kernel-5.16-backport.patch"
    # patch -p1 -N -i "${srcdir}/kernel-5.15-backport.patch"
    # patch -p1 -N -i "${srcdir}/kernel-5.14-backport.patch"
    # patch -p1 -N -i "${srcdir}/kernel-5.12-backport.patch"

    cp -rt "${dest}" *
}
