# Maintainer: 3ED <krzysztofas /at/ protonmail /dot/ com>
# Contributor: jtts

pkgname=libreoffice-extension-languagetool
_pkgname=languagetool
pkgver=4.2
pkgrel=1
pkgdesc="An Open Source style and grammar checker (more than 30 languages)"
arch=('any')
url="https://www.languagetool.org/"
license=('LGPL')
groups=('libreoffice-extensions')
depends=('libreoffice' 'java-runtime>=8')
source=("https://www.languagetool.org/download/LanguageTool-${pkgver}.oxt")
noextract=("LanguageTool-${pkgver}.oxt")
sha512sums=('d72a656a40cf7cdebe8e5fc4d0d015dbc510418ff0c98fc6fb34aa0031c74553e594d3ad333168a108660426125d3ea2ee07a11d43b0b3d80a3be4f4d787e031')

package() {
  _DESTDIR="${pkgdir}/usr/lib/libreoffice/share/extensions/${_pkgname}/"
  install -dm755 "${_DESTDIR}"
  bsdtar -xf LanguageTool-${pkgver}.oxt -C "${_DESTDIR}"
  chmod -R a=r,a+X,u+w "${_DESTDIR}"
}
