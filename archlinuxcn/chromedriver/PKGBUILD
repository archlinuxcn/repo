# Maintainer: Raymo111 <aur@raymond.li>
# Contributor: JunYoung Gwak <aur@jgwak.com>
# Contributor: relrel <relrelbachar@gmail.com>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: James An <james@jamesan.ca>
# Contributor: lybin
pkgname=chromedriver
pkgver=106.0.5249.61
pkgrel=1
pkgdesc="Standalone server that implements the W3C WebDriver standard (for google-chrome)"
arch=('x86_64')
url="https://chromedriver.chromium.org/"
license=('BSD')
depends=(alsa-lib gtk3 libcups libxss libxtst nss xdg-utils)
optdepends=(google-chrome)
conflicts=(chromium)
source=("${pkgname}_${pkgver}_linux64.zip::https://chromedriver.storage.googleapis.com/${pkgver}/${pkgname}_linux64.zip")
sha512sums=('989801fe5ac7f4eb22b8fe914f1e1ad63d1903e04c095c757ab8caaa489f314e97e169e9694745415d9e84332210788df58c3ddde4343755316cbdc0dcd3f391')

package() {
    install -Dm755 -t "$pkgdir/usr/bin/" "$srcdir/$pkgname"
}
