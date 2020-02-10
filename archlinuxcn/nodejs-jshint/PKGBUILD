# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: John D Jones III (jnbek) <https://aur.archlinux.org/account/jnbek>

_npmname=jshint
pkgname=nodejs-"$_npmname"
pkgver=2.11.0
pkgrel=1
pkgdesc='Static analysis tool for JavaScript'
arch=('any')
url='https://jshint.com/'
license=('MIT')
depends=('nodejs')
makedepends=('nodejs' 'npm')
source=("https://registry.npmjs.org/$_npmname/-/$_npmname-$pkgver.tgz")
sha256sums=('1a7fa84101fb2212110a41543e88bca26d3b9762bce63c95627ac0dbdf4d5a3a')
noextract=("${source[@]##*/}")

package() {
    npm install -g --prefix "$pkgdir/usr" "${source[@]##*/}"
}
