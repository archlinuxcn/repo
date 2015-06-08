# Contributor: noonov <noonov@gmail.com>

pkgname=ttf-ume
pkgver=0.510
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
md5sums=('a23e8ff6a5654ead1618476937f5c697')
sha256sums=('47748da742a5885219dfb9cce7ed15428c60bf81e3901ecd378f5e49e5d9d1d0')

package() {
  cd ${srcdir}

  install -d ${pkgdir}/usr/share/fonts/TTF
  install -m644 umefont_${_pkgver}/*.ttf ${pkgdir}/usr/share/fonts/TTF

  install -D -m644 umefont_${_pkgver}/license.html \
          ${pkgdir}/usr/share/licenses/${pkgname}/COPYING.html
}
