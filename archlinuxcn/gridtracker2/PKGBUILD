# Maintainer: Cryolitia <cryolitia at gmail dot com>

pkgname=gridtracker2
pkgver=2.250820.0
pkgrel=1
_electronver=35
pkgdesc="An Amateur Radio Companion"
arch=('any')
url="https://gridtracker.org"
license=('BSD-3-Clause')
makedepends=('npm')
depends=("electron${_electronver}" 'libxss' 'libappindicator-gtk3' 'libxtst' 'at-spi2-core' 'util-linux-libs' 'libsecret')
source=("https://gitlab.com/gridtracker.org/${pkgname}/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz"
        "gridtracker2.desktop"
        "gridtracker2.sh")
sha512sums=('cb6e0ed0406be0081ef1514ff0b20d02a45d056f6f0d26eb4c5890531925877022ca3cbf2e3473a0574941c7cf5941e2a604f40d334a2096b91056a6e1a8dca4'
            'd0b2a0aa0a1ef8826d594bfab433ce38bd2ba9c6db1fa290552e7cd72312d7de88fb5912b8a0459ba4a137251cc91fb1f981ffcf21d98234555d5fc59fca219f'
            'bc530bac0b04211bbf1f81851a3c23869a519d9ed6b77c56fcc13b43b56cf855bb01497aa453c69a2a141e17a6003bc534bc75bc3591dcc1e666d5c66202cd53')

prepare() {
  cd ${pkgname}-v$pkgver

  sed -i "s/@_electronver@/$_electronver/" "$srcdir/${pkgname}.sh"
  grep -q "\"electron\": \"$_electronver\." package.json \
    || ( echo "Electron version mismatch in package.json"; exit 1 )

  npm install
}

build() {
  cd ${pkgname}-v$pkgver
  ./node_modules/.bin/electron-builder --linux --x64 --dir \
     -c.electronDist=/usr/lib/electron$_electronver \
     -c.electronVersion=$_electronver
}

package() {
  cd ${pkgname}-v$pkgver

  install -Dvm644 -t "${pkgdir}/usr/share/${pkgname}/resources" \
    ./dist/linux-unpacked/resources/*
  install -Dvm644 -t "${pkgdir}/usr/share/${pkgname}/locales" \
    ./dist/linux-unpacked/locales/*
  install -Dvm644 -t "${pkgdir}/usr/share/applications" \
    "${srcdir}/gridtracker2.desktop"
  install -Dvm755 "${srcdir}/gridtracker2.sh" \
    "${pkgdir}/usr/bin/gridtracker2"
  install -Dvm644 ./resources/icon.png \
    "${pkgdir}/usr/share/pixmaps/gridtracker2.png"
  install -Dvm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
    ./LICENSE
}
