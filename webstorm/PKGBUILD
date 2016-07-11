# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>
# Contributor: Pablo Vilas <pablovilas89 at gmail dot com>
# Contributor: Testuser_01 <arch@nico-siebler.de>

pkgname=webstorm
_pkgname=WebStorm
pkgver=2016.2
_pkgver=162.1121.31
pkgrel=1
pkgdesc="JavaScript IDE and HTML editor."
arch=('x86_64' 'i686')
options=('!strip')
url="http://www.jetbrains.com/${pkgname}/"
license=('Commercial')
optdepends=('java-environment>=8: use system java'
            'java-runtime-common: use system java')
source=(https://download.jetbrains.com/webstorm/${_pkgname}-${pkgver}.tar.gz
        jetbrains-webstorm.desktop
        webstorm.sh)
sha512sums=('fe9067d3b2b9ef5468ae821f9a6c5e56442e022bfa6c75966ee46aae80074a1ac9ab914714bc0b42b80aabdaba36f5a037921e3d29f010a23c33d2b386e0c379'
            'd963f93c39ae9e3525064d3974ba096074c815ac8d5e7084ec41fb5c07ec46e341a9adafd01356061e84d50431e815cfbffe8c5f7effd087e84380bd6317215f'
            'cd3a2de35858d581b84bb78e57637cbcf0e9f1606c088ff981532eb153707326d5d3fa81776106cd1e3df7e833840ea84e5573e40bf6dc906c94f9231cf31948')

package() {
  install -d -m 755 ${pkgdir}/opt/
  install -d -m 755 ${pkgdir}/usr/bin/
  install -d -m 755 ${pkgdir}/usr/share/applications/
  install -d -m 755 ${pkgdir}/usr/share/pixmaps/
  install -d -m 755 ${pkgdir}/etc/profile.d/

  cp -a ${srcdir}/${_pkgname}-${_pkgver} $pkgdir/opt/${pkgname}
  # if using system java you may remove the bundled jre and save about 100M
  #rm -rf $pkgdir/opt/${pkgname}/jre

  ln -s /opt/$pkgname/bin/${pkgname}.sh $pkgdir/usr/bin/${pkgname}
  install -D -m 644 ${srcdir}/jetbrains-${pkgname}.desktop ${pkgdir}/usr/share/applications/
  install -D -m 644 ${srcdir}/${pkgname}.sh ${pkgdir}/etc/profile.d/
  install -D -m 644 "${pkgdir}/opt/${pkgname}/bin/${pkgname}.svg" "${pkgdir}/usr/share/pixmaps/${pkgname}.svg"
}
