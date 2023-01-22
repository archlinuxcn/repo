# Maintainer: 3ED <krzysztofas /at/ protonmail /dot/ com>
# Contributor: jtts

pkgname=libreoffice-extension-languagetool
_pkgname=languagetool
pkgver=6.0
pkgrel=1
_url_obfuscation_code="3710/1673297554"
pkgdesc="An Open Source style and grammar checker (more than 30 languages)"
arch=('any')
url="https://www.languagetool.org/"
license=('LGPL')
groups=('libreoffice-extensions')
depends=('libreoffice' 'java-runtime>=8')
optdepends=('jre8-openjdk: java 8 or greater is required')
source=("LanguageTool-${pkgver}.oxt::https://extensions.libreoffice.org/assets/downloads/${_url_obfuscation_code}/LanguageTool-${pkgver}.oxt")
noextract=("LanguageTool-${pkgver}.oxt")
sha512sums=('3c1635c23e4624346001cbaf586c1c4d087f725dca35f8ef1f446e7bf19c0718b98bdf862d582c3e90ecd5525d5ddc37ab2945019b426546edd6c8c70a0b54ec')

package() {
  _DESTDIR="${pkgdir}/usr/lib/libreoffice/share/extensions/${_pkgname}/"
  install -dm755 "${_DESTDIR}"
  bsdtar -xf LanguageTool-${pkgver}.oxt -C "${_DESTDIR}"
  chmod -R a=r,a+X,u+w "${_DESTDIR}"
}
