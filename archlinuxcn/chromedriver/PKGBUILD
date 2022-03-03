# Maintainer: Raymo111 <aur@raymond.li>
# Contributor: JunYoung Gwak <aur@jgwak.com>
# Contributor: relrel <relrelbachar@gmail.com>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: James An <james@jamesan.ca>
# Contributor: lybin
pkgname=chromedriver
pkgver=99.0.4844.51
pkgrel=1
pkgdesc="Standalone server that implements the W3C WebDriver standard (for google-chrome)"
arch=('x86_64')
url="https://chromedriver.chromium.org/"
license=('BSD')
depends=(alsa-lib gtk3 libcups libxss libxtst nss xdg-utils)
optdepends=(google-chrome)
conflicts=(chromium)
source=("${pkgname}_${pkgver}_linux64.zip::https://chromedriver.storage.googleapis.com/${pkgver}/${pkgname}_linux64.zip")
sha512sums=('15ac3dcbaf6bf4d5d610444b24ca680e23b84d11be978b6ba7889ce9ae2c343a15ac54707a03a81551186edb7f44c161f1dfb23fc586e7445044e8c96ee2537c')

package() {
    install -Dm755 -t "$pkgdir/usr/bin/" "$srcdir/$pkgname"
}
