# Maintainer: Daniel Peukert <daniel@peukert.cc>
# Contributor: Maxim Baz <archlinux at maximbaz dot com>
# Contributor: Fredrik Haikarainen <fredrik.haikarainen@gmail.com>
# Contributor: Marcin (CTRL) Wieczorek <marcin@marcin.co>
pkgname='light'
pkgver='1.2.2'
_commit='2a54078cbe3814105ee4f565f451b1b5947fbde0'
pkgrel='5'
pkgdesc='A program to control backlights (and other hardware lights)'
arch=('x86_64' 'i486' 'i686' 'pentium4' 'armv7h' 'aarch64')
url="https://gitlab.com/dpeukert/$pkgname"
license=('GPL-3.0-only')
install="$pkgname.install"
source=(
	# $pkgrel added to make sure our cached source file doesn't get used, as the previous pkgrel used a different upstream
	"$pkgname-$pkgver-$pkgrel.tar.gz::$url/-/archive/$_commit/$pkgname-$_commit.tar.gz"
	'fix-global-var.diff'
	'namespace-udev-rule.diff'
	'update-manpage.diff'
)
sha512sums=('343bffdf7d007066fb82b4305fe961b70b74c206e0f8c1fb3d2d184a09fee9f02491a3fbe01515663a90ec40c20cf2a3dccb8a252597b907ab8ad0b6e33b5238'
            'e020deaca76f65a032f6f694f07b43af6318d46f52e0e16554a883d54c43c5519c7bbb3ecbc6e8f39d2828fbebe73d37aa82d4051b2cc652a1775286188b6ded'
            '1cee6c3f10a6534e03bdf6874b95e699fdf8900f7cb9d86df6f8b99f0f77ff2b80d515eb3f4e43602f5ae19fa3009db63301ff862f1d02b8a17f3282ea063232'
            '36cad74b303c206035dd6941269209278c0661358820444ce97b6ef383761e258ccf56d12c80590278972db0e1be98fae3632269cbababc49690726a61fc1708')

_sourcedirectory="$pkgname-$_commit"

prepare() {
	cd "$srcdir/$_sourcedirectory/"

	patch --forward -p1 < '../fix-global-var.diff'
	patch --forward -p1 < '../namespace-udev-rule.diff'
	patch --forward -p1 < '../update-manpage.diff'
}

build() {
	cd "$srcdir/$_sourcedirectory/"
	./autogen.sh
	./configure --prefix='/usr' --with-udev
	make
}

check() {
	# Not using -V, as it doesn't match the real version
	_checkoutput="$("$srcdir/$_sourcedirectory/src/$pkgname" -h)"
	printf '%s\n' "$_checkoutput"
	printf '%s\n' "$_checkoutput" | grep -q 'Increase brightness by value$'
}

package() {
	cd "$srcdir/$_sourcedirectory/"
	make install DESTDIR="$pkgdir" PREFIX='/usr'
}
