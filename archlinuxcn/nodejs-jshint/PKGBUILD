# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: John D Jones III (jnbek) <https://aur.archlinux.org/account/jnbek>

_npmname=jshint
pkgname=nodejs-"$_npmname"
pkgver=2.10.2
pkgrel=1
pkgdesc='Static analysis tool for JavaScript'
arch=('any')
url='http://jshint.com/'
license=('MIT')
depends=('nodejs')
makedepends=('nodejs' 'npm')
source=("https://registry.npmjs.org/$_npmname/-/$_npmname-$pkgver.tgz")
sha256sums=('250fbe74b61670d7ca77dbba53724bec4d78a2c27bff58afcf5c1c006728f013')
noextract=("${source[@]##*/}")

package() {
    npm install -g --prefix "$pkgdir/usr" "${source[@]##*/}"
}
