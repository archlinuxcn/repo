pkgname=ntfs3-dkms
pkgver=5.15
pkgrel=2
epoch=1
pkgdesc="NTFS3 is fully functional NTFS Read-Write driver. The driver works with NTFS versions up to 3.1."
arch=('any')
url='https://www.kernel.org/doc/html/latest/filesystems/ntfs3.html'
license=('GPL2')
depends=('dkms')
provides=('NTFS3-MODULE' "ntfs3=${pkgver}" "ntfs3-dkms=${pkgver}")
conflicts=('ntfs3')
options=('!strip')

_snapshot="linux-86a44e9067c95083d5dbf5a140e3f4560e5af1ca"
_archive="${_snapshot}.tar.gz"

source=(
    "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/snapshot/${_archive}"
    Makefile.patch
    dkms.conf
    kernel-5.12-backport.patch
    kernel-5.14-backport.patch
    kernel-5.15-backport.patch
)

sha512sums=(
    '153b8eb241515d1043fac1e455b47229bef25ffb200cd07366dda5ceb483f0427a170890a2da16c61ee089dde28a240cd7639f503a9293e8e3bfec9422335569'
    '533c249f0f6bd4833faf02d0d92ca1b5802a49afc5feb2e46a7d37275cfca7896db76cd83593f4f313977d278a9a7e92eda550667be2b93910c49cfb68ead4fb'
    '5e2f2493fbf7a4d12e7cd7d3c0bb8fc3d8bd5d290f990e5b73c52bfa4ab58127c08eeff09fab7b0ba3a2c4ab1861fec68ce711b1cb57867bb61a81785f312677'
    '4b1976b40f67c210ee4052407a359ed8db0709a568387ffacc15e695b43af7c77b53fbe27a3365197521e5c9baa8bd9c7aaffa2f8345be17129216b1ac141fbe'
    '61a1948e3e607dabaca47742777b4ea92fadf9f5416ebaef8c06f1e17aab0f3ced34e900c0cf1ed462303f391f4a4713b5b30a488b349839780bde3248e19f3c'
    '3a9395f5729c14cd8d8bf2ecda566730d90c6990319ed5e33310fa2dbe4d4a33df925950ff652fff338ef0135e5aeecf4b991603bba797847f8f1ef9130420c7'
)

noextract=("${_archive}")

prepare() {
    cd "${srcdir}"
    tar xf "${_archive}" "${_snapshot}/fs/ntfs3" --strip-components=2
}

build() {
    cd "${srcdir}/ntfs3"
    patch -p0 -N -i "${srcdir}/Makefile.patch"

    # For testing
    # patch -p1 -N -i "${srcdir}/kernel-5.15-backport.patch"
    # patch -p1 -N -i "${srcdir}/kernel-5.14-backport.patch"
    # patch -p1 -N -i "${srcdir}/kernel-5.12-backport.patch"
}

package() {
    cd "${srcdir}"

    local dest=$(install -dm755 "${pkgdir}/usr/src/ntfs3-${pkgver}" && echo "$_")

    cp -rt "${dest}" "ntfs3/"*

    install -Dm644 -t "${dest}" "dkms.conf"

    install -dm755 "${dest}/patches" && cp -t "$_" "kernel-"*.patch
}
