# Maintainer: Alex Henrie <alexhenrie24@gmail.com>
pkgname=git-cinnabar
pkgver=0.5.9
pkgrel=1
pkgdesc="Git remote helper to interact with Mercurial repositories"
arch=(x86_64)
url="https://github.com/glandium/$pkgname"
license=(GPL2)
depends=(git mercurial python)
source=("https://github.com/glandium/$pkgname/archive/refs/tags/$pkgver.tar.gz")
sha256sums=(83374ff2c7e9ccbb5e866c6fb350ad3202cab4856841afbadaded1f1bef4d534)

build() {
	cd "$pkgname-$pkgver"
	PYTHONDONTWRITEBYTECODE=1 make
}

package() {
	cd "$pkgname-$pkgver"
	mkdir -p "$pkgdir/opt/$pkgname"
	cp -r cinnabar git-cinnabar git-cinnabar-helper git-remote-hg mercurial "$pkgdir/opt/$pkgname"
	mkdir -p "$pkgdir/usr/bin"
	ln -s "/opt/$pkgname/$pkgname" "$pkgdir/usr/bin/$pkgname"
	ln -s "/opt/$pkgname/$pkgname-helper" "$pkgdir/usr/bin/$pkgname-helper"
	ln -s "/opt/$pkgname/git-remote-hg" "$pkgdir/usr/bin/git-remote-hg"
}
