# Maintainer: DDoSolitary <DDoSolitary@gmail.com>

_pkgname=vim-auto-pairs
pkgname=$_pkgname-git
pkgver=2.0.0.r3.g39f06b8
pkgrel=3
pkgdesc='Vim plugin, insert or delete brackets, parens, quotes in pair'
url=https://github.com/jiangmiao/auto-pairs
license=(MIT)
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
	install -Dm644 doc/AutoPairs.txt "$pkgdir"/usr/share/vim/vimfiles/doc/auto-pairs.txt
	install -Dm644 plugin/auto-pairs.vim "$pkgdir"/usr/share/vim/vimfiles/plugin/auto-pairs.vim
}
