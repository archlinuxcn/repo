# Maintainer: Jax Young <jaxvanyang@gmail.com>
# Contributor: Luis Martinez <luis dot martinez at disroot dot org>

pkgname=fish-pure-prompt
pkgver=4.18.0
pkgrel=1
pkgdesc="Pretty, minimal, and fast prompt for Fish"
arch=('any')
url="https://github.com/pure-fish/pure"
license=('MIT')
groups=('fish-plugins')
depends=('fish')	# remove >=3 to allow fish-git
provides=('fish-prompt')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('50e89094d18f54790ce4c8362d0cb021c5a0b9cc54a42b2e8bd484803446d928')

package() {
	cd "pure-$pkgver"
	find conf.d -type f -exec install -Dm 644 -t "$pkgdir/usr/share/fish/vendor_conf.d/" '{}' \+
	find functions -type f -exec install -Dm 644 -t "$pkgdir/usr/share/fish/vendor_functions.d/" '{}' \+
	install -Dm 644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
	install -Dm 644 README.md -t "$pkgdir/usr/share/doc/$pkgname/"
}
