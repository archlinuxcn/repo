# Maintainer: 3ED <krzysztofas /at/ protonmail /dot/ com>
# Contributor: jtts

pkgname=libreoffice-extension-languagetool
_pkgname=languagetool
pkgver=5.5.1
pkgrel=1
_url_obfuscation_code=1635796125
pkgdesc="An Open Source style and grammar checker (more than 30 languages)"
arch=('any')
url="https://www.languagetool.org/"
license=('LGPL')
groups=('libreoffice-extensions')
depends=('libreoffice' 'java-runtime>=8')
optdepends=('jre8-openjdk: java 8 or greater is required')
source=("LanguageTool-${pkgver}.oxt::https://extensions.libreoffice.org/assets/downloads/99/${_url_obfuscation_code}/LanguageTool-5.5.1.oxt")
noextract=("LanguageTool-${pkgver}.oxt")
sha512sums=('bca1ea063bd06f55d1786175fdd0f0e8bf6ea4854d87a63e112ad93169da8b19c076938abb02fe650b5e88524211deedfffd2ba2c94d09be3e330bd2324c7f9e')

package() {
  _DESTDIR="${pkgdir}/usr/lib/libreoffice/share/extensions/${_pkgname}/"
  install -dm755 "${_DESTDIR}"
  bsdtar -xf LanguageTool-${pkgver}.oxt -C "${_DESTDIR}"
  chmod -R a=r,a+X,u+w "${_DESTDIR}"
}
