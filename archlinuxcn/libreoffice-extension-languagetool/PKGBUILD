# Maintainer: 3ED <krzysztofas /at/ protonmail /dot/ com>
# Contributor: jtts

pkgname=libreoffice-extension-languagetool
_pkgname=languagetool
pkgver=5.4
pkgrel=1
pkgdesc="An Open Source style and grammar checker (more than 30 languages)"
arch=('any')
url="https://www.languagetool.org/"
license=('LGPL')
groups=('libreoffice-extensions')
depends=('libreoffice' 'java-runtime>=8')
optdepends=('jre8-openjdk: java 8 or greater is required')
source=("LanguageTool-${pkgver}.oxt::https://extensions.libreoffice.org/assets/downloads/99/LanguageTool-5.4.oxt")
noextract=("LanguageTool-${pkgver}.oxt")
sha512sums=('bfa05d8c834234e1313227cf161292987651c1abba49abbd50b1d2ce348ddec6b611c779278ac49e7482599262ac86830165ed51d4811f224bddc5bdda12d885')

package() {
  _DESTDIR="${pkgdir}/usr/lib/libreoffice/share/extensions/${_pkgname}/"
  install -dm755 "${_DESTDIR}"
  bsdtar -xf LanguageTool-${pkgver}.oxt -C "${_DESTDIR}"
  chmod -R a=r,a+X,u+w "${_DESTDIR}"
}
