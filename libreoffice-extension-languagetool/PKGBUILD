# Maintainer: 3ED <krzysztofas /at/ protonmail /dot/ com>
# Contributor: jtts

pkgname=libreoffice-extension-languagetool
_pkgname=languagetool
pkgver=4.3
pkgrel=1
pkgdesc="An Open Source style and grammar checker (more than 30 languages)"
arch=('any')
url="https://www.languagetool.org/"
license=('LGPL')
groups=('libreoffice-extensions')
depends=('libreoffice' 'java-runtime>=8')
source=("https://www.languagetool.org/download/LanguageTool-${pkgver}.oxt")
noextract=("LanguageTool-${pkgver}.oxt")
sha512sums=('6b5bea3c864b9ddb082f4e56ee79f6f31a266bd4c28734caa7a802261d05b8e91e57a790c1c725a540f7fa5539b3beeb665de79c4f9b5241b0c135baa59645b0')

package() {
  _DESTDIR="${pkgdir}/usr/lib/libreoffice/share/extensions/${_pkgname}/"
  install -dm755 "${_DESTDIR}"
  bsdtar -xf LanguageTool-${pkgver}.oxt -C "${_DESTDIR}"
  chmod -R a=r,a+X,u+w "${_DESTDIR}"
}
