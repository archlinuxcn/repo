# Maintainer: DDoSolitary <DDoSolitary@gmail.com>

_pkgname=vim-sleuth
pkgname=$_pkgname-git
pkgver=1.2.r0.g38bd401
pkgrel=2
pkgdesc='Heuristically set buffer options'
url=https://github.com/tpope/vim-sleuth
license=(custom:vim)
source=($_pkgname::git+$url.git)
md5sums=(SKIP)
arch=(any)
depends=(vim)
makedepends=(git)
conflicts=($_pkgname)
provides=($_pkgname)

pkgver() {
	cd $_pkgname
	git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

package() {
	cd $_pkgname
	install -Dm644 doc/sleuth.txt "$pkgdir"/usr/share/vim/vimfiles/doc/sleuth.txt
	install -Dm644 plugin/sleuth.vim "$pkgdir"/usr/share/vim/vimfiles/plugin/sleuth.vim
}
