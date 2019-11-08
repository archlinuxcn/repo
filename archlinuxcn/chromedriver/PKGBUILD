# Maintainer: JunYoung Gwak <i@jgwak.com>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: James An <james@jamesan.ca>
# Contributor: lybin

pkgname=chromedriver
pkgver=78.0.3904.70
pkgrel=1
pkgdesc="Standalone server which implements WebDriver's wire protocol (for google-chrome)"
arch=('x86_64')
url="https://sites.google.com/a/chromium.org/chromedriver/"
license=('Apache')
conflicts=('chromium')
depends=('libpng' 'gconf')
optdepends=('google-chrome')
md5sums=('37f077132433b20db3f0f5636e89f142')

source=("${pkgname}_${pkgver}_linux64.zip::http://chromedriver.storage.googleapis.com/${pkgver}/${pkgname}_linux64.zip")

package() {
  mkdir -p "$pkgdir/usr/bin/"
  install -D -m 755 "$srcdir/$pkgname" "$pkgdir/usr/bin/"
}
