# Maintainer: DDoSolitary <DDoSolitary@gmail.com>

_pkgname=vim-surround
pkgname=$_pkgname-git
pkgver=2.1.r18.gf51a26d
pkgrel=3
pkgdesc='quoting/parenthesizing made simple'
url=https://github.com/tpope/vim-surround
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
	install -Dm644 doc/surround.txt "$pkgdir"/usr/share/vim/vimfiles/doc/surround.txt
	install -Dm644 plugin/surround.vim "$pkgdir"/usr/share/vim/vimfiles/plugin/surround.vim
}
