# Contributor: noonov <noonov@gmail.com>

pkgname=ttf-ume
pkgver=0.520
_pkgver=${pkgver:2}
pkgrel=1
pkgdesc="Free Japanese Gothic/Mincho Font"
arch=('any')
url="http://sourceforge.jp/projects/ume-font/"
license=('custom')
depends=('fontconfig' 'xorg-font-utils')
install=ttf.install
_mirror="jaist" # keihanna, jaist, iij, osdn
source=(http://${_mirror}.dl.sourceforge.jp/ume-font/22212/umefont_${_pkgver}.tar.xz)
md5sums=('cee5a12d49f96ef2ebf135e5083b320a')
sha256sums=('6730e2d9b291861a5dd6a85688181f2e11786de63a486e133631205a20c8e05b')

package() {
  cd ${srcdir}

  install -d ${pkgdir}/usr/share/fonts/TTF
  install -m644 umefont_${_pkgver}/*.ttf ${pkgdir}/usr/share/fonts/TTF

  install -D -m644 umefont_${_pkgver}/license.html \
          ${pkgdir}/usr/share/licenses/${pkgname}/COPYING.html
}
