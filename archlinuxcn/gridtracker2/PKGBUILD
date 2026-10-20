# Maintainer: Cryolitia <cryolitia at gmail dot com>

pkgname=gridtracker2
pkgver=2.261019.2
pkgrel=1
pkgdesc="An Amateur Radio Companion"
arch=('any')
url="https://gridtracker.org"
license=('BSD-3-Clause')
makedepends=('npm')
depends=('electron' 'libxss' 'libappindicator-gtk3' 'libxtst' 'at-spi2-core' 'util-linux-libs' 'libsecret')
source=("https://gitlab.com/gridtracker.org/${pkgname}/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz"
        "gridtracker2.desktop"
        "gridtracker2.sh")
sha512sums=('c48c904c9233b94c4c50ac90f98841d829e19c8c75e08ebcbc61bdf033e47b5dfa8073e36e29134c8944fb631d9992a9c375202985b93e214120d18a7dc3ba6c'
            'd0b2a0aa0a1ef8826d594bfab433ce38bd2ba9c6db1fa290552e7cd72312d7de88fb5912b8a0459ba4a137251cc91fb1f981ffcf21d98234555d5fc59fca219f'
            '349837d334e216402c244f6cafda95bd4de4cec046a55d08989659ed064caeb0d9de7f3e492f1e85b3de584335c56509c1db72a85b32aacb231fb2fae989fa64')

prepare() {
  cd "${pkgname}-v$pkgver"

  ELECTRON_SKIP_BINARY_DOWNLOAD=1 npm ci --cache "$srcdir/npm-cache"
}

build() {
  cd "${pkgname}-v$pkgver"
  local electronver
  electronver=$(< /usr/lib/electron/version)

  ./node_modules/.bin/electron-builder --linux --x64 --dir --publish never \
     -c.electronDist=/usr/lib/electron \
     -c.electronVersion="$electronver"
}

package() {
  cd "${pkgname}-v$pkgver"

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
