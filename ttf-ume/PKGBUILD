# Contributor: noonov <noonov@gmail.com>

pkgname=ttf-ume
pkgver=0.540
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
md5sums=('4e8a619dff0dfa205d263e289b357daf')
sha256sums=('52e60630d737fc0ca50d0ba7d8b0d460bbfd997b5db3fcaba111044affcb5305')

package() {
  cd ${srcdir}

  install -d ${pkgdir}/usr/share/fonts/TTF
  install -m644 umefont_${_pkgver}/*.ttf ${pkgdir}/usr/share/fonts/TTF

  install -D -m644 umefont_${_pkgver}/license.html \
          ${pkgdir}/usr/share/licenses/${pkgname}/COPYING.html
}
