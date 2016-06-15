# Contributor: noonov <noonov@gmail.com>

pkgname=ttf-ume
pkgver=0.620
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
sha256sums=('3cca7e4b021b981bfdc7d8fdf587c1b38bea57e4bbb7c78e57de3a60984abfb8')

package() {
  cd ${srcdir}

  install -d ${pkgdir}/usr/share/fonts/TTF
  install -m644 umefont_${_pkgver}/*.ttf ${pkgdir}/usr/share/fonts/TTF

  install -D -m644 umefont_${_pkgver}/license.html \
          ${pkgdir}/usr/share/licenses/${pkgname}/COPYING.html
}
