# Contributor: noonov <noonov@gmail.com>

pkgname=ttf-ume
pkgver=0.670
_pkgver=${pkgver:2}
pkgrel=3
pkgdesc="Free Japanese Gothic/Mincho Font"
arch=('any')
url="https://osdn.jp/projects/ume-font/"
license=('custom')
depends=('fontconfig' 'xorg-mkfontscale')
source=(https://osdn.net/dl/ume-font/umefont_${_pkgver}.tar.xz)
md5sums=('9603b086be384030d059bc36d8ac4dd4')
b2sums=('4a5d544e7ddcdb74aa62d10f424d2a9d5d6c4b82c730531ac410681962f61a13eaca2dc2f159089aedca5d38c71da5b11b5f776e9e209793c0583cef23cc4809')

package() {
  cd ${srcdir}

  install -d ${pkgdir}/usr/share/fonts/TTF
  install -m644 umefont_${_pkgver}/*.ttf ${pkgdir}/usr/share/fonts/TTF

  install -D -m644 umefont_${_pkgver}/license.html \
          ${pkgdir}/usr/share/licenses/${pkgname}/COPYING.html
}
