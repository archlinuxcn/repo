pkgname=ntfs3-dkms
pkgver=27.0.0
pkgrel=5
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/home/ntfs3-driver-faq/'
license=('GPL2')
depends=('dkms')
provides=('NTFS3-MODULE' "ntfs3=${pkgver}" "ntfs3-dkms=${pkgver}")
conflicts=('ntfs3')
options=('!strip')

source=(
    Makefile.patch
    dkms.conf
    kernel-5.12-backport.patch
    kernel-5.14-backport.patch
    kernel-5.15-backport.patch
    "ntfs3-v${pkgver}.patch::https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/rawdiff/?id=f7464060f7ab9a2424428008f0ee9f1e267e410f&id2=6abaa83c7352b31450d7e8c173f674324c16b02b"
)

sha512sums=(
    '533c249f0f6bd4833faf02d0d92ca1b5802a49afc5feb2e46a7d37275cfca7896db76cd83593f4f313977d278a9a7e92eda550667be2b93910c49cfb68ead4fb'
    'f61ad1d95b577c1fa183fc0ad4c8c0d1d269db7603892ae6b121ee1b0ab34063692bb39136ecef4ed548b4648b8519101ca44ea268d60241f1ea047718aa12f9'
    '6f6190825febee219e10be6583718afc9360b3b4c69e06f8d59715da8f73a855d4f652b1ef77064ca100fd15678e13a0ef10bb7837f10c0784530eff1694340d'
    '0392b665aced96aa92cd6e0f72c2276c0233e661c7cc3b6fe8e074c2be654f2c8836b1d0468a8a665f43fac08704896d0ef0dcbb8826b4deef88a3a894bdf050'
    'c68307e0dd9fbf17b36599bb850d9aa7b6fee5c38a9c2da975643a311ac8d09ecabd145ba09d8a5062630cac3a853bb035b641ff6fe75672940ccc3b7b164aa8'
    'd19089027897871b6ae339b206f74aed12a0c9e7235a104eb995ca1b7ddf49cb531631b360e4c678f37ccdd7bac629959040e810be18d247259334ef35f32af6'
)

prepare() {
    mkdir -p "${pkgver}"
    cd "${pkgver}"

    patch -p3 -t -N -i "${srcdir}/ntfs3-v${pkgver}.patch" || true

    patch -p0 -N -i "${srcdir}/Makefile.patch"

    # For testing
    # patch -p1 -N -i "${srcdir}/kernel-5.15-backport.patch"
    # patch -p1 -N -i "${srcdir}/kernel-5.14-backport.patch"
    # patch -p1 -N -i "${srcdir}/kernel-5.12-backport.patch"
}

package() {
    local dest="${pkgdir}/usr/src/ntfs3-${pkgver}"
    mkdir -p "${dest}"
    cd "${dest}"
    cp -r "${srcdir}/${pkgver}/"* ./
    cp "${srcdir}/dkms.conf" ./
    mkdir -p "./patches"
    cp "${srcdir}/kernel-"*.patch "./patches/"
}
