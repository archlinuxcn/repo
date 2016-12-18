# Maintainer: yk <yk at archlinuxcn dot org>

_pkgname=libQtShadowsocks
pkgname=libqtshadowsocks
pkgver=1.10.0
pkgrel=1
pkgdesc="A lightweight library for shadowsocks."
arch=("i686" "x86_64")
url="https://github.com/librehat/$_pkgname"
license=("GPL3")
depends=("qt5-base>=5.2" "botan-1.10>=1.10.12")
makedepends=("git" "make")
provides=("$pkgname")
conflicts=("$pkgname" "$pkgname-git")
source=("https://github.com/librehat/$_pkgname/archive/v$pkgver.tar.gz")
sha256sums=("67d2f9d3fa0e8e22e1d7fd1c850177a2d601f9c467fc024c0ba11eaedcef6279")

build() {
	cd "$srcdir/$_pkgname-$pkgver"
	qmake INSTALL_PREFIX=/usr
	make
}

package() {
	cd "$srcdir/$_pkgname-$pkgver"
	make INSTALL_ROOT="$pkgdir" install

    #fix lib6
    cd "$pkgdir/usr"
    if [ -d lib64 ]; then
        ls lib||mkdir lib
        cp -a lib64/* lib/
        rm -rf lib64
    fi
}
