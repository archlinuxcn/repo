# Maintainer: Michael Koloberdin <koloberdin@gmail.com>
pkgname=urweb
pkgver=20180616
pkgrel=1
pkgdesc="Ur/Web: purely functional language/framework for web programming"
arch=('i686' 'x86_64')
url="http://www.impredicative.com/ur/"
license=('BSD')
makedepends=('curl' 'mlton')
depends=('libmariadbclient' 'postgresql-client' 'sqlite3' 'openssl' 'uthash')
source=("https://github.com/urweb/urweb/releases/download/$pkgver/$pkgname-$pkgver.tar.gz"
	"use-system-uthash.patch")
sha512sums=('8e79887192b0a5c8c7a8e8104253eecdaa8e9f7a583c408473562d0594938ff29aaae2b6144e0d9121929db371bfd43b8c528498ed3254439359d05f2cfa3b3c'
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
