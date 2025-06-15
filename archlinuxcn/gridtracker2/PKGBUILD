# Maintainer: Cryolitia <cryolitia at gmail dot com>

pkgname=gridtracker2
pkgver=2.250507.0
pkgrel=3
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
sha512sums=('7041cb1802303315b1038d88310687049cc339c845281eb67760db25d0df8248b1ebeb249013318cc70ee2ca63c65512ed599c07d2c7c028ab3bdd3ffb66fb96'
            'SKIP'
            'SKIP')

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
