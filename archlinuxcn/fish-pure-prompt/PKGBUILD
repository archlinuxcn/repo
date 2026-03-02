# Maintainer: Jax Young <jaxvanyang@gmail.com>
# Contributor: Luis Martinez <luis dot martinez at disroot dot org>

pkgname=fish-pure-prompt
pkgver=4.16.0
pkgrel=1
pkgdesc="Pretty, minimal, and fast prompt for Fish"
arch=('any')
url="https://github.com/pure-fish/pure"
license=('MIT')
groups=('fish-plugins')
depends=('fish')	# remove >=3 to allow fish-git
provides=('fish-prompt')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('8e2f6b98801e1e3b5446d967f9b6404b3ed4e222fa22ad2f65c5207012c4943b')

package() {
	cd "pure-$pkgver"
	find conf.d -type f -exec install -Dm 644 -t "$pkgdir/usr/share/fish/vendor_conf.d/" '{}' \+
	find functions -type f -exec install -Dm 644 -t "$pkgdir/usr/share/fish/vendor_functions.d/" '{}' \+
	install -Dm 644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
	install -Dm 644 README.md -t "$pkgdir/usr/share/doc/$pkgname/"
}
