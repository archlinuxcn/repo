# Contributor: noonov <noonov@gmail.com>

pkgname=ttf-mplus
pkgver=TESTFLIGHT_063a
_pkgver=${pkgver/_/-}
pkgrel=1
pkgdesc="M+ Japanese outline fonts"
arch=('any')
url="http://mplus-fonts.osdn.jp/mplus-outline-fonts/index-en.html"
license=('custom')
depends=('fontconfig')
_mirror="jaist"
source=(http://${_mirror}.dl.osdn.jp/mplus-fonts/62344/mplus-${_pkgver}.tar.xz)
sha256sums=('44eb973b4b6aff574de454db105ddc23e6749c2294734bd9cb1e0d734e4cdd79')

package() {
  cd ${srcdir}/mplus-${_pkgver}

  install -d ${pkgdir}/usr/share/fonts/TTF
  install -m644 *.ttf ${pkgdir}/usr/share/fonts/TTF/

  install -D -m644 LICENSE_E \
          ${pkgdir}/usr/share/licenses/${pkgname}/COPYING
}
