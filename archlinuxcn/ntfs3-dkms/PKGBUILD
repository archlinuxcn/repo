pkgname=ntfs3-dkms
pkgver=22.0.0
pkgrel=1
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/home/ntfs3-driver-faq/'
license=('GPL2')
depends=('dkms')
options=('!strip')
source=(Makefile.patch
        dkms.conf
        "v$pkgver~1.patch::https://lore.kernel.org/lkml/20210301160102.2884774-2-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~2.patch::https://lore.kernel.org/lkml/20210301160102.2884774-3-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~3.patch::https://lore.kernel.org/lkml/20210301160102.2884774-4-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~4.patch::https://lore.kernel.org/lkml/20210301160102.2884774-5-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~5.patch::https://lore.kernel.org/lkml/20210301160102.2884774-6-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~6.patch::https://lore.kernel.org/lkml/20210301160102.2884774-7-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~7.patch::https://lore.kernel.org/lkml/20210301160102.2884774-8-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~8.patch::https://lore.kernel.org/lkml/20210301160102.2884774-9-almaz.alexandrovich@paragon-software.com/raw"
        kernel_version_fix.patch)
sha512sums=('55523ce0d3c3790c33fbe73bd396e5e5f1d015608303e497202a232f51af9bb172003cc836880a7fa85163947609281754606067e5e0df79e9630cd6d1821b96'
            '91b1f6566930aa67e8ced4d30cddda3bc0c7391d5aedc46d907d7400341aea27dfad696c5dd4cd1e56b2605de8c9188de13f913d491238f13812e475d5c4bd2f'
            '0fbce73d71dd4f4644e13db384f82649d7cada4cc2dd9fb38910db7bca6b2b3dbad62ef39df7df78cfb76cdd3195c9f130e9a8eccebb5225f16963357d41cf47'
            'c44b9d27c76350bf433edc7e3f16ab2b1b661c48344c5978aca144a82e345671111ae60e76a05e09d334db2603b8aeb3037122544dd62856afa3f1ac224f5e15'
            '0171142b3a312ed68b7811a5955706128813348242f189b30d4ed691d8004a791688e611027d8803707be8db0d82ad6ff9fdbed47c08d4b8e387a8b883223683'
            '381aeba0f7373b91de129a971b1e87ba3fdf5a4a26b9fd9ad11eacd5ffb6a3955b68ae8c5f445d49bbe937cea8ffcb6ff1791a0582600b3457df6b46ae599c8e'
            '600de9bd9e3a9596485dc10aa5f2dd5f40d4e2c599f32ebb396cf7e86500f0c526ca17c1bd7f8635cf32173d330630228880c9ff3d2befedfcd6ae31a243c542'
            'da2aba4179565733d7ef5459577e966cece0dea86f7de74b0ae801313851dcb6c004f94c0b3f02fbe60a07e766200fbf451ced305881d3f33aec3193233681f8'
            'c2c3a69bdd84bd5b201a843c178f52c508d3c16efff814a3143b5b7f05b8170f6df4ec98703b63b0443bed8bd644208340b78a84b74375c5586453db2f6f680a'
            '455917687dbade59092cd60844c0796b442fc596c8c25bd3c490ba5bdc532bcb661bb199db4d85f6b2b55d9d7f1e51a4f1b57a2e23a84e4b3380d0b12e7004ad'
            '3c5688afe55f8a6ccd34da26e6e6765d9adc073cb74d38c1f73f9ef3f4e0f8e88b990e32aed494ed40cbe83fd847fdaeca3aaf0c20de8f27e27e879814bb5c86')


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
