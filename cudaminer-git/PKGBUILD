# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: TJM <tommy.mairo@gmail.com>
pkgname=cudaminer-git
_gitname=CudaMiner
pkgver=209.746a773
pkgrel=2
pkgdesc="CUDA accelerated mining application for scrypt coins(Litecoin etc.)."
url="https://github.com/cbuchner1/CudaMiner"
arch=('i686' 'x86_64')
license=('GPL')
depends=('cuda' 'automake' 'jansson')
makedepends=('git')
source=("git+https://github.com/cbuchner1/CudaMiner" 'gcc6.1.1.patch')
sha256sums=('SKIP' '1e9727d44b3b1cc9e4e2a1fc013122bb401ab9c59bd5d368b5dd0af291f7af7c')

pkgver() {
    cd $_gitname
    echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}
prepare(){
	patch -p1 $_gitname/Makefile.am < gcc6.1.1.patch
}
build(){
	cd $_gitname
	./autogen.sh
	CFLAGS=-O2 ./configure --with-cuda=/opt/cuda  --prefix=/usr
	make
}

package() {
	cd $_gitname
	make DESTDIR=${pkgdir} install
}
