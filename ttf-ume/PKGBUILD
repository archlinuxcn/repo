# Contributor: noonov <noonov@gmail.com>

pkgname=ttf-ume
pkgver=0.600
_pkgver=${pkgver:2}
pkgrel=1
pkgdesc="Free Japanese Gothic/Mincho Font"
arch=('any')
url="http://sourceforge.jp/projects/ume-font/"
license=('custom')
depends=('fontconfig' 'xorg-font-utils')
install=ttf.install
_mirror="jaist" # keihanna, jaist, iij, osdn
source=(http://${_mirror}.dl.sourceforge.jp/ume-font/22212/umefont_${_pkgver}.7z)
sha256sums=('3606fd9636557422f2910d31d52cc14f7197bacfcf641ac9c109ea712cc555a5')

package() {
  cd ${srcdir}

  install -d ${pkgdir}/usr/share/fonts/TTF
  install -m644 umefont_${_pkgver}/*.ttf ${pkgdir}/usr/share/fonts/TTF

  install -D -m644 umefont_${_pkgver}/license.html \
          ${pkgdir}/usr/share/licenses/${pkgname}/COPYING.html
}
