# Maintainer: Raymo111 <aur@raymond.li>
# Contributor: JunYoung Gwak <aur@jgwak.com>
# Contributor: relrel <relrelbachar@gmail.com>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: James An <james@jamesan.ca>
# Contributor: lybin
pkgname=chromedriver
pkgver=108.0.5359.71
pkgrel=1
pkgdesc="Standalone server that implements the W3C WebDriver standard (for google-chrome)"
arch=('x86_64')
url="https://chromedriver.chromium.org/"
license=('BSD')
depends=(alsa-lib gtk3 libcups libxss libxtst nss xdg-utils)
optdepends=(google-chrome)
conflicts=(chromium)
source=("${pkgname}_${pkgver}_linux64.zip::https://chromedriver.storage.googleapis.com/${pkgver}/${pkgname}_linux64.zip")
sha512sums=('82debce470a48d8fe7c0b39faffb28cd102f192b2ed977afcb286de3bfbd4d519a894be910317b2e8847660db016ebc544e081f050adb22c67f3c57b0a9a7089')

package() {
    install -Dm755 -t "$pkgdir/usr/bin/" "$srcdir/$pkgname"
}
