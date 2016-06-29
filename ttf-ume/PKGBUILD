# Contributor: noonov <noonov@gmail.com>

pkgname=ttf-ume
pkgver=0.630
_pkgver=${pkgver:2}
pkgrel=1
pkgdesc="Free Japanese Gothic/Mincho Font"
arch=('any')
url="https://osdn.jp/projects/ume-font/"
license=('custom')
depends=('fontconfig' 'xorg-font-utils')
install=ttf.install
_mirror="jaist" # keihanna, jaist, iij, osdn
source=(http://${_mirror}.dl.osdn.jp/ume-font/22212/umefont_${_pkgver}.7z)
sha256sums=('f248ad742bb93ecc7469e5c3507b452fe31c413b3df6c88e3b2e353cd1e4fde3')

package() {
  cd ${srcdir}

  install -d ${pkgdir}/usr/share/fonts/TTF
  install -m644 umefont_${_pkgver}/*.ttf ${pkgdir}/usr/share/fonts/TTF

  install -D -m644 umefont_${_pkgver}/license.html \
          ${pkgdir}/usr/share/licenses/${pkgname}/COPYING.html
}
