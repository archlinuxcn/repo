# Maintainer: Michael Koloberdin <koloberdin@gmail.com>
pkgname=urweb
pkgver=20190217
pkgrel=1
pkgdesc="Ur/Web: purely functional language/framework for web programming"
arch=('i686' 'x86_64')
url="http://www.impredicative.com/ur/"
license=('BSD')
makedepends=('curl' 'mlton')
depends=('libmariadbclient' 'postgresql-client' 'sqlite3' 'openssl' 'uthash')
source=("https://github.com/urweb/urweb/releases/download/$pkgver/$pkgname-$pkgver.tar.gz"
	"use-system-uthash.patch")
sha512sums=('5f21ef3b5330ab2a5be204cc89b4184d9dad03b4d30f87c81fd48366d43dc115ab9a4c1b3e2de203c876413b528b221935282a020851c4e4ea7dcd13529dadf3'
            'df7089e75d91c14568bcc01d0a0cf9d57e073c5e2c278508305176a8b7f2775f27a26b66d82e1566f00d473e89099480273a7b6f5f11d927802de959da3678ac')

prepare() {
	cd "$pkgname-$pkgver"
	patch -p1 -i "$srcdir/use-system-uthash.patch"
}

build() {
	cd "$pkgname-$pkgver"
	./configure --prefix=/usr
	make
}

check() {
	cd "$pkgname-$pkgver"
	make -k check
}

package() {
	cd "$pkgname-$pkgver"
	
	make DESTDIR="$pkgdir/" install
	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
