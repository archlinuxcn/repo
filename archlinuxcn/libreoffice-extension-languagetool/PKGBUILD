# Maintainer: 3ED <krzysztofas /at/ protonmail /dot/ com>
# Contributor: jtts

pkgname=libreoffice-extension-languagetool
_pkgname=languagetool
pkgver=5.6
pkgrel=1
_url_obfuscation_code=1643401435
pkgdesc="An Open Source style and grammar checker (more than 30 languages)"
arch=('any')
url="https://www.languagetool.org/"
license=('LGPL')
groups=('libreoffice-extensions')
depends=('libreoffice' 'java-runtime>=8')
optdepends=('jre8-openjdk: java 8 or greater is required')
source=("LanguageTool-${pkgver}.oxt::https://extensions.libreoffice.org/assets/downloads/99/${_url_obfuscation_code}/LanguageTool-${pkgver}.oxt")
noextract=("LanguageTool-${pkgver}.oxt")
sha512sums=('2856a941e71a2f357e5c89fcc3cbb5b3d49f363b0d934987824135473f9d0adc8f572101cef284b1d11ce45c2115b56add0431da24543530aa0020a98d265773')

package() {
  _DESTDIR="${pkgdir}/usr/lib/libreoffice/share/extensions/${_pkgname}/"
  install -dm755 "${_DESTDIR}"
  bsdtar -xf LanguageTool-${pkgver}.oxt -C "${_DESTDIR}"
  chmod -R a=r,a+X,u+w "${_DESTDIR}"
}
