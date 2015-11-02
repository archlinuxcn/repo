# Contributor: noonov <noonov@gmail.com>

pkgname=ttf-ume
pkgver=0.560
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
md5sums=('82a4e6fa7bbf283e13cd98a7b2683549')
sha256sums=('7f0a64250c1878e65276723bdf9e08e78ef1b323f6721542a89a511b571fd772')

package() {
  cd ${srcdir}

  install -d ${pkgdir}/usr/share/fonts/TTF
  install -m644 umefont_${_pkgver}/*.ttf ${pkgdir}/usr/share/fonts/TTF

  install -D -m644 umefont_${_pkgver}/license.html \
          ${pkgdir}/usr/share/licenses/${pkgname}/COPYING.html
}
