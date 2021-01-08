pkgname=ntfs3-dkms
pkgver=17.0.0
pkgrel=2
pkgdesc="NTFS read-write driver GPL implementation by Paragon Software. Current version works with NTFS (including v3.1), normal/compressed/sparse files and supports journal replaying."
arch=('any')
url='https://www.paragon-software.com/home/ntfs3-driver-faq/'
license=('GPL2')
depends=('dkms')
options=('!strip')
source=(Makefile.patch
        dkms.conf
        "v$pkgver~1.patch::https://lore.kernel.org/lkml/20201231152401.3162425-2-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~2.patch::https://lore.kernel.org/lkml/20201231152401.3162425-3-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~3.patch::https://lore.kernel.org/lkml/20201231152401.3162425-4-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~4.patch::https://lore.kernel.org/lkml/20201231152401.3162425-5-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~5.patch::https://lore.kernel.org/lkml/20201231152401.3162425-6-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~6.patch::https://lore.kernel.org/lkml/20201231152401.3162425-7-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~7.patch::https://lore.kernel.org/lkml/20201231152401.3162425-8-almaz.alexandrovich@paragon-software.com/raw"
        "v$pkgver~8.patch::https://lore.kernel.org/lkml/20201231152401.3162425-9-almaz.alexandrovich@paragon-software.com/raw")
sha512sums=('3d47cccc7914b42dbcc670bcb9144f948a42d0ba57843140373afec0483570597b4b4ad61753742b282626f50aec25cabbeb88aadc94d2cb67ec1c612b6ed41d'
            '9b0cef4cd4e2c9978666440afc128d893efecd86ef481f5d3c00674b18a8318575ef17016d5a0a57dbb12df3a62409758f2a70270bba1f1ac41bae707686c085'
            '75add010b7b7d12802c0f62652d3c843ac69744378650528172adf41f4ac80be4926272a9ea19af07af0b31fe56fdacb8afccbbfe0f4d40ea9054aebc03d47dc'
            'ca74559dac13a96d3a57e4ffa2739e7383de22515be9ded3e4785653632e378c9e35f8d5c8444eb5ac5f764f4a5bce85b9324aada092bf417ddcd82761db2836'
            '1fd37b4e74e2d323c3881f8b0811cb431d02bdb4cb6cdd67e5dfeec66ccf27ed952ea7cebddce2d72e8d013e47cadce3171d2159ac49f8dffb16c81876869a69'
            '3ce92db85e18525abf98377a7d5b2d6a513b9ee0a504648be3049ea230744cd233727ac8fa035143f261acb58a838579cd0201201c2dc79d27d14e6e5692cef0'
            '54225e1d46bf9303a6b566e2ae0ccbb7640173a286384fb8c04103826f251481d0fb2452d2ba1c96a759a389d0712926a56ed32080024936479ab2dd26695169'
            '996cfb5f11014316429dac9a1bcedb67b73e3778bd32169440096f4b06d82c98923883370e106d071c9ad337113af5523836e182414d6e2f3206a33f786d5d73'
            '81add656be3ed853569590f03f78cb85be332d920ac74a0de67e5da38c0ea48ee7d2a397841a1cc0774999d4d4f30e321795f23b8d995d4298489b0bead16654'
            '7d2095b9a82d8a878f316995aa9dc6b5a75ced29cf405b5f7ca95948be5fe4f9b1a2d884043ce744552133a53993900eee656f1ecd620a96b3da34ab86fec444')


prepare() {
  mkdir -p ${pkgname}-${pkgver}
  cd ${pkgname}-${pkgver}
  for patch in "$srcdir/v$pkgver~"*
  do
    patch -p3 -N -i "$patch"
  done
  patch -p0 -N -i "$srcdir/Makefile.patch"
}

package() {
  mkdir -p "${pkgdir}/usr/src"
  cp -r "${pkgname}-${pkgver}" "${pkgdir}/usr/src/ntfs3-${pkgver}"
  install -Dm644 "${srcdir}/dkms.conf" "${pkgdir}/usr/src/ntfs3-${pkgver}/dkms.conf"
}
