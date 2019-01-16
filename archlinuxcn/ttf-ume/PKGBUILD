# Contributor: noonov <noonov@gmail.com>

pkgname=ttf-ume
pkgver=0.670
_pkgver=${pkgver:2}
pkgrel=2
pkgdesc="Free Japanese Gothic/Mincho Font"
arch=('any')
url="https://osdn.jp/projects/ume-font/"
license=('custom')
depends=('fontconfig')
_mirror="jaist"
source=(http://${_mirror}.dl.osdn.jp/ume-font/22212/umefont_${_pkgver}.7z)
sha256sums=('92c4e4f40ddb4285f99240fb28fa19808d586cb3aa3fccb348ee9da940ca3e35')

package() {
  cd ${srcdir}

  install -d ${pkgdir}/usr/share/fonts/TTF
  install -m644 umefont_${_pkgver}/*.ttf ${pkgdir}/usr/share/fonts/TTF

  install -D -m644 umefont_${_pkgver}/license.html \
          ${pkgdir}/usr/share/licenses/${pkgname}/COPYING.html
}
