# Maintainer: Jax Young <jaxvanyang@gmail.com>
pkgname=md-padding
pkgver=1.10.0
pkgrel=1
pkgdesc="Tool for formatting Markdown content with padding"
arch=('any')
url="https://github.com/harttle/md-padding"
license=('MIT')
depends=('nodejs')
makedepends=('npm')
source=("https://registry.npmjs.org/$pkgname/-/$pkgname-$pkgver.tgz")
noextract=("$pkgname-$pkgver.tgz")
sha256sums=('7eb36307f13ac793a6c413c9e2dc2c03938153810f2ee576bc3ba1f880e7c6b1')

package() {
	npm install -g --prefix "$pkgdir/usr" "$srcdir/$pkgname-$pkgver.tgz"
}
