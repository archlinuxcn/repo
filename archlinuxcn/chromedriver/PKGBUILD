# Maintainer: JunYoung Gwak <aur@jgwak.com>
# Contributor: relrel <relrelbachar@gmail.com>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: James An <james@jamesan.ca>
# Contributor: lybin
pkgname=chromedriver
pkgver=87.0.4280.88
pkgrel=1
pkgdesc="Standalone server that implements the W3C WebDriver standard (for google-chrome)"
arch=('x86_64')
url="https://chromedriver.chromium.org/"
license=('BSD')
depends=(alsa-lib gtk3 libcups libxss libxtst nss xdg-utils)
optdepends=(google-chrome)
conflicts=(chromium)
source=("${pkgname}_${pkgver}_linux64.zip::https://chromedriver.storage.googleapis.com/${pkgver}/${pkgname}_linux64.zip")
sha512sums=('20a6db9f6be3c975bf231d05f05b41b610c9fcf491d1df604e987a652ce97faa20aeb1621776ccbcde10ef9fb9d3005641c185abb2494c978723fdbf7d1f2af2')

package() {
    install -Dm755 -t "$pkgdir/usr/bin/" "$srcdir/$pkgname"
}
