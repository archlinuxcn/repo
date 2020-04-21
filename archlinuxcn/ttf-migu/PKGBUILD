# Maintainer: ny-a <nyaarch64@gmail..com>
# Contributor: noonov <noonov@gmail.com>
# Contributor: gasuketsu02 <gasuketsu02@gmail.com>

pkgname=ttf-migu
pkgver=20200307
_release=72511
pkgrel=1
pkgdesc="Good looking Japanese TrueType font by mixing M+ and IPA."
arch=('any')
url="http://mix-mplus-ipa.osdn.jp/migu/"
license=('custom')
depends=('fontconfig')
_mirror="jaist"
source=("http://${_mirror}.dl.osdn.jp/mix-mplus-ipa/${_release}/migu-1c-${pkgver}.zip"
        "http://${_mirror}.dl.osdn.jp/mix-mplus-ipa/${_release}/migu-1m-${pkgver}.zip"
        "http://${_mirror}.dl.osdn.jp/mix-mplus-ipa/${_release}/migu-1p-${pkgver}.zip"
        "http://${_mirror}.dl.osdn.jp/mix-mplus-ipa/${_release}/migu-2m-${pkgver}.zip")
sha256sums=('6324807e7a7a7738298d86a0b4fcbd3f5f0180416a98a15aa552bdf801b10e0e'
            'a4770fca22410668d2747d7898ed4d7ef5d92330162ee428a6efd5cf247d9504'
            'de3fb44777ec2d623db33fefd16e9ceb6caff793e08809cd2e35edb3ec9aa22d'
            'dbfd177bf3d7645ba080b7b1e07c5b1966a2cd6e003c7586e3d53490377938be')

package() {
  cd ${srcdir}

  install -d ${pkgdir}/usr/share/fonts/TTF
  install -m644 */*.ttf ${pkgdir}/usr/share/fonts/TTF

  install -D -m644 migu-1c-*/migu-README.txt \
          ${pkgdir}/usr/share/licenses/${pkgname}/COPYING.txt
  install -D -m644 migu-1c-*/ipag00303/IPA_Font_License_Agreement_v1.0.txt \
          ${pkgdir}/usr/share/licenses/${pkgname}/COPYING_IPA.txt
}
