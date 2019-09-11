# Maintainer: JunYoung Gwak <i@jgwak.com>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: James An <james@jamesan.ca>
# Contributor: lybin

pkgname=chromedriver
pkgver=77.0.3865.40
pkgrel=1
pkgdesc="Standalone server which implements WebDriver's wire protocol (for google-chrome)"
arch=('x86_64')
url="https://sites.google.com/a/chromium.org/chromedriver/"
license=('Apache')
conflicts=('chromium')
depends=('libpng' 'gconf')
optdepends=('google-chrome')
md5sums=('b4431816072192a2d36a10fa8cfde344')

source=("${pkgname}_${pkgver}_linux64.zip::http://chromedriver.storage.googleapis.com/${pkgver}/${pkgname}_linux64.zip")

package() {
  mkdir -p "$pkgdir/usr/bin/"
  install -D -m 755 "$srcdir/$pkgname" "$pkgdir/usr/bin/"
}
