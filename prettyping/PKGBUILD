# Maintainer: Wyatt J. Brown <sushidudeteam@gmail.com>
pkgname=prettyping
pkgver=1.0.0
pkgrel=2
epoch=1
pkgdesc='A wrapper around the standard ping tool with the objective of making the output prettier, more colorful, more compact, and easier to read.'
arch=('any')
url='https://github.com/denilsonsa/prettyping'
license=('MIT')
source=("https://github.com/denilsonsa/prettyping/archive/v$pkgver.tar.gz")
sha512sums=('ec117bde13efd713567b0d991024a00409de1e6e2054771cdb78c41322a36ae53e255e07a4bc2b14ecd9dde20d91751a0dcb6e4bb8e810d579850efc9f49ed09')

package()
{
	install -Dm644 "$srcdir/prettyping-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
	install -Dm755 "$srcdir/prettyping-$pkgver/prettyping" "$pkgdir/usr/bin/prettyping"
}
