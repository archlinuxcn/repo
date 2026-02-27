# Maintainer: Jax Young <jaxvanyang@gmail.com>
# Contributor: Luis Martinez <luis dot martinez at disroot dot org>

pkgname=fish-pure-prompt
pkgver=4.15.1
pkgrel=1
pkgdesc="Pretty, minimal, and fast prompt for Fish"
arch=('any')
url="https://github.com/pure-fish/pure"
license=('MIT')
groups=('fish-plugins')
depends=('fish')	# remove >=3 to allow fish-git
provides=('fish-prompt')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('d8e267d19f3fb10df0ca12a05042e20febabcbac4c73c70329c7b5ec1ae64582')

package() {
	cd "pure-$pkgver"
	find conf.d -type f -exec install -Dm 644 -t "$pkgdir/usr/share/fish/vendor_conf.d/" '{}' \+
	find functions -type f -exec install -Dm 644 -t "$pkgdir/usr/share/fish/vendor_functions.d/" '{}' \+
	install -Dm 644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
	install -Dm 644 README.md -t "$pkgdir/usr/share/doc/$pkgname/"
}
