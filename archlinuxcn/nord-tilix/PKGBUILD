# Maintainer: Arctic Ice Studio <development@arcticicestudio.com>
pkgname=nord-tilix
pkgver=0.3.0
pkgrel=2
pkgdesc="An arctic, north-bluish clean and elegant Tilix color scheme"
arch=("any")
url="https://github.com/arcticicestudio/nord-tilix"
license=("Apache", "CC-BY-SA-4.0")
depends=("tilix>=1.5")
makedepends=("git")
source=("$pkgname::git+https://github.com/arcticicestudio/nord-tilix.git#tag=v$pkgver")
md5sums=("SKIP")

package() {
  cd "${srcdir}/${pkgname}"
  install -dm755 "$pkgdir/usr/share/tilix/schemes"
  install -Dm644 "src/json/nord.json" "$pkgdir/usr/share/tilix/schemes"
}
