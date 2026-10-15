# Maintainer: Jax Young <jaxvanyang@gmail.com>
# Contributor: Luis Martinez <luis dot martinez at disroot dot org>

pkgname=fish-pure-prompt
pkgver=4.19.2
pkgrel=1
pkgdesc="Pretty, minimal, and fast prompt for Fish"
arch=('any')
url="https://github.com/pure-fish/pure"
license=('MIT')
groups=('fish-plugins')
depends=('fish')	# remove >=3 to allow fish-git
provides=('fish-prompt')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('3d42523b48d92a83861257f902ff4c8c39ee7ee80d8da51d22b6ad5e1ad091d4')

package() {
	cd "pure-$pkgver"
	find conf.d -type f -exec install -Dm 644 -t "$pkgdir/usr/share/fish/vendor_conf.d/" '{}' \+
	find functions -type f -exec install -Dm 644 -t "$pkgdir/usr/share/fish/vendor_functions.d/" '{}' \+
	install -Dm 644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
	install -Dm 644 README.md -t "$pkgdir/usr/share/doc/$pkgname/"
}
