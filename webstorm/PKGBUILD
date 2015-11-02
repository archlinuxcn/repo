# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>
# Contributor: Pablo Vilas <pablovilas89 at gmail dot com>
# Contributor: Testuser_01 <arch@nico-siebler.de>

pkgname=webstorm
_pkgname=WebStorm
pkgver=11.0.0
_pkgver=143.381.46
pkgrel=2
pkgdesc="JavaScript IDE and HTML editor."
arch=('x86_64' 'i686')
options=('!strip')
url="http://www.jetbrains.com/${pkgname}"
license=('custom')
depends=('java-environment')
source=(https://download.jetbrains.com/webstorm/${_pkgname}-${pkgver}.tar.gz
        jetbrains-webstorm.desktop
        webstorm.install)
sha256sums=('ae8ae6ec6f3b400b1df4d999fcb6efc80435e630e8e8f80bba4771ac7c59f771'
            'df1155779ec87c1f9e3237a2b79a0bea1242f4f2661d3d0f5f152ef24af93166'
            'a12071f48cfaa0fa41bf5ebf4d977366ca142329938183139adb044078b2f105')

package() {
  install -d -m 755 ${pkgdir}/opt/
  install -d -m 755 ${pkgdir}/usr/bin/
  install -d -m 755 ${pkgdir}/usr/share/applications/
  install -d -m 755 ${pkgdir}/usr/share/pixmaps/

  cp -a ${srcdir}/${_pkgname}-${_pkgver} $pkgdir/opt/${pkgname}

  ln -s /opt/$pkgname/bin/${pkgname}.sh $pkgdir/usr/bin/${pkgname}
  install -D -m 644 ${srcdir}/jetbrains-${pkgname}.desktop ${pkgdir}/usr/share/applications/
  install -D -m 644 "${pkgdir}/opt/${pkgname}/bin/webstorm.svg" "${pkgdir}/usr/share/pixmaps/webstorm.svg"
}
