# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: John D Jones III (jnbek) <https://aur.archlinux.org/account/jnbek>

_npmname=jshint
pkgname=nodejs-"$_npmname"
pkgver=2.10.1
pkgrel=1
pkgdesc='Static analysis tool for JavaScript'
arch=('any')
url='http://jshint.com/'
license=('MIT')
depends=('nodejs')
makedepends=('nodejs' 'npm')
source=("https://registry.npmjs.org/$_npmname/-/$_npmname-$pkgver.tgz")
sha256sums=('739eaaf228e2390d5187132b6e9b415838af94c63f221849ba99c6b932fb0940')
noextract=("${source[@]##*/}")

package() {
    npm install -g --prefix "$pkgdir/usr" "${source[@]##*/}"
}
