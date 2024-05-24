# Maintainer: Raymo111 <aur@raymond.li>
# Contributor: Robert Walaski <robert@walaski.cz>
# Contributor: JunYoung Gwak <aur@jgwak.com>
# Contributor: relrel <relrelbachar@gmail.com>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: James An <james@jamesan.ca>
# Contributor: lybin
pkgname=chromedriver
pkgver=125.0.6422.78
pkgrel=1
pkgdesc="Standalone server that implements the W3C WebDriver standard (for google-chrome)"
arch=('x86_64')
url="https://chromedriver.chromium.org/"
license=('BSD')
depends=(alsa-lib gtk3 libcups libxss libxtst nss xdg-utils)
optdepends=(google-chrome)
conflicts=(chromium)
source=("${pkgname}_${pkgver}_linux64.zip::https://storage.googleapis.com/chrome-for-testing-public/${pkgver}/linux64/${pkgname}-linux64.zip")
sha512sums=('1c926e6530e285d61813aadfe224cbe00a5c1a7c32cc1d990fd3266face3cf8bbacfb233c4a34cd36b3e101a14f90a810e626b5bbe0c480a981c73c99b37cfcf')
package() {
    install -Dm755 -t "$pkgdir/usr/bin/" "$srcdir/$pkgname-linux64/$pkgname"
}
