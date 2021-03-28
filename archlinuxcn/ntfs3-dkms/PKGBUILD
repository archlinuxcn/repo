pkgname=ntfs3-dkms
pkgver=25.0.0
pkgrel=1
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/home/ntfs3-driver-faq/'
license=('GPL2')
depends=('dkms')
options=('!strip')
source=(Makefile.patch
        dkms.conf
        "v$pkgver~1.patch::https://lore.kernel.org/lkml/20210327214023.3214923-2-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~2.patch::https://lore.kernel.org/lkml/20210327214023.3214923-3-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~3.patch::https://lore.kernel.org/lkml/20210327214023.3214923-4-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~4.patch::https://lore.kernel.org/lkml/20210327214023.3214923-5-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~5.patch::https://lore.kernel.org/lkml/20210327214023.3214923-6-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~6.patch::https://lore.kernel.org/lkml/20210327214023.3214923-7-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~7.patch::https://lore.kernel.org/lkml/20210327214023.3214923-8-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~8.patch::https://lore.kernel.org/lkml/20210327214023.3214923-9-almaz.alexandrovich@paragon-software.com/raw"
        kernel_version_fix.patch)
sha512sums=('5b5b487eb66d2f74699cbd10c0c669c0dbbd87c0c8ed1d96685aa5f3eb992fdfe859f0eb7aa3a31ade9e267cf6a9a9df228a760f305ff4a2874f01cd7844bf98'
            '73ca8f543ed3d1e16e99ecf8ce2b74ebf10aa5d0cd66b217ded1391afc35ef5eaa1d4cd8c6b6027ff4c8af5d4608ac0671138a2bd008e2a5a7f49989d2f354e0'
            '9f790f1360bbe01bf715f9602a41d46d53943283c49de32c798462c78d67c299c28ec29baa79314e4021295e50b499907f0ce68d89929c55fe5da179bfcd9f55'
            'b0dde294a0c9407e139e92185fd13a30bce4d82e9663bd60b5eba3ecce790d35a3b5c8d9372fa2d136d820adc571ba452d71e5741b651feb92da44d108e105d3'
            '3d3b91ed0bd1859f864ed0d7fd2a5fd497815510b2a936f5177dd91bd23b2fd99d29390c76a2dc557df55b25c9987445ec4de124e3291bddaaf5dbe407dd8193'
            '7b9c454be26cf7c89be62912ed395818e74fe627b1dbdb5ba2b50846c593ed8cb42e24b368872c708c230951e6101b0c2791f3c4719bab7029b0ca220820294f'
            '7635e209c1dd429d87b08f7004ddaa9714ed67666dc01baca717240e70fba89f8c96cdca8385063d040b883381d9cbba75124ae99f35f3a693d1b67a8a1be69c'
            '90a728c660a3cd04d7465880005148f143163988305d83f470fdd1359a468f9e4ba17311599c4714d09e17f9edc83fed9065fd5e8021f51abf07b4b64e20fcd5'
            '256a4d756a1b3400089f1566a5bbeb07b872156faf72a15d99a64fad93708e032c3bc19f53965e8c2d606f704d1a7d63c91c3fdf27315fd0abbda76b16c3fe53'
            '28cb13c13faf379472878b6cb5c4aa077964549279ed42f8973be4500e5f5471c8df980462f7b4a2536bb23934286b6105fa36b82cd845c9811753d47d138bcd'
            '091c3e2e7dbcad387ad1bed4c7a16ce9113b4ecaf90e2e529408b7d4db7fcb89a279d067faf7e8ac9504139573cc36b01038f3237e4cdd08ded0e11bb96ddb4f')


prepare() {
  mkdir -p ${pkgname}-${pkgver}
  cd ${pkgname}-${pkgver}
  for patch in "$srcdir/v$pkgver~"*
  do
    patch -p3 -N -i "$patch"
  done
  patch -p3 -N -i "$srcdir/kernel_version_fix.patch"
  patch -p0 -N -i "$srcdir/Makefile.patch"
}

package() {
  mkdir -p "${pkgdir}/usr/src"
  cp -r "${pkgname}-${pkgver}" "${pkgdir}/usr/src/ntfs3-${pkgver}"
  install -Dm644 "${srcdir}/dkms.conf" "${pkgdir}/usr/src/ntfs3-${pkgver}/dkms.conf"
}
