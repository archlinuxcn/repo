# Contributor: noonov <noonov@gmail.com>

pkgname=ttf-ume
pkgver=0.640
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
sha256sums=('cd27fcfd4c7e0e7dcaac49c33b1f181c59c507134c812f1531eb076d6134a604')

package() {
  cd ${srcdir}

  install -d ${pkgdir}/usr/share/fonts/TTF
  install -m644 umefont_${_pkgver}/*.ttf ${pkgdir}/usr/share/fonts/TTF

  install -D -m644 umefont_${_pkgver}/license.html \
          ${pkgdir}/usr/share/licenses/${pkgname}/COPYING.html
}
