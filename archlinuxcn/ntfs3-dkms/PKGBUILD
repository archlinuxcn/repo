pkgname=ntfs3-dkms
pkgver=24.0.0
pkgrel=1
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/home/ntfs3-driver-faq/'
license=('GPL2')
depends=('dkms')
options=('!strip')
source=(Makefile.patch
        dkms.conf
        "v$pkgver~1.patch::https://lore.kernel.org/lkml/20210319185210.1703925-2-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~2.patch::https://lore.kernel.org/lkml/20210319185210.1703925-3-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~3.patch::https://lore.kernel.org/lkml/20210319185210.1703925-4-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~4.patch::https://lore.kernel.org/lkml/20210319185210.1703925-5-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~5.patch::https://lore.kernel.org/lkml/20210319185210.1703925-6-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~6.patch::https://lore.kernel.org/lkml/20210319185210.1703925-7-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~7.patch::https://lore.kernel.org/lkml/20210319185210.1703925-8-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~8.patch::https://lore.kernel.org/lkml/20210319185210.1703925-9-almaz.alexandrovich@paragon-software.com/raw"
        kernel_version_fix.patch)
sha512sums=('5b5b487eb66d2f74699cbd10c0c669c0dbbd87c0c8ed1d96685aa5f3eb992fdfe859f0eb7aa3a31ade9e267cf6a9a9df228a760f305ff4a2874f01cd7844bf98'
            '7f2b1a5c83f2bb0777824905260b554854bbc5020fb5674802a4e0e31cb53da6e74f359e3b1430db1c756930237503936157a274c430ba9611e269323b53c672'
            '7715eb8c97cd372f9c68f093cbb73b234e06587d7392ac195169e225b8ec9be5347bc661da8c94fdbe28d8401847545b97197e1f9c3ad10b94f4ecf8536638f6'
            '69f96e0d0e712d26cc87d75a9dbd653cce8a3490e93e5195a0e2108743daee03452d2b03e118387c9b425deeada682bdcf76a32b2803639b04efea0e802210a2'
            '1c741d12c1c3512218f416af601c8ad405094141eabf84188936baa3120e22e86b9415128b231e77e68963ebef380a4a37d7f82ee04313cfbe8cb57dc897bce3'
            '740586652674a7abdaa463d6cdf88b33f70c6ca0b59964a5b7b1f1dbd8ca6c759c7c258256a346b93fd208e4f4e867614e92ebb88bfbe778627d1832b0bad29f'
            '6d13c52f4a705f7954e16e5db3cd6cae943039e4b80f09a58b610e32e00cd62b4ee85f47a0792250d97a8953833adbb637e325a05f4a94ded9b8047a0df6d8f6'
            '876a5ac20a6725e083c1d5fb3fb23f87240b6345d4c4d208def870db1ddf331db2a4967ce2c7d17db168465e218be7d3ec6c8e4082c9bf3853e6c70df11ed5d3'
            'e2c1ab9ef6193b99b6a4e1e3c38c11701c85e72755e7014e73c2900506373e251c738792af6a2177559122d3dbf47daf9e618cb78bc89746c338c07d6e70d1d1'
            'c0f48670cc99742323c3ffb38e158ed6c9633e4ff9354cb4ac9c089dcb3e4fe45c468aa59576ed4718bf8c0ab5e7e4b2e3b197f214e53c758009a491e823c11f'
            '0e4f8343aa2dd6d862707baebef7bdeb48546064d58becc291a92af6ba03416da6f98233fd0c8b6f84a85c69f2536ef56a8ad0c2aeedf3da398828d4a1e4b888')


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
