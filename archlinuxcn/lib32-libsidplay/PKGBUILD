# Maintainer: GordonGR <gordongr@freemail.gr>
# Contributor: Kritoke <kritoke@gamebox.net>
# Contributor: Jan de Groot <jgc@archlinux.org>

pkgname=lib32-libsidplay
_pkgname=libsidplay
pkgver=1.36.59
pkgrel=6
pkgdesc="A library for playing SID music files, lib32."
arch=('x86_64')
url="http://critical.ch/distfiles/"
license=('GPL')
options=('!libtool')
depends=("${_pkgname}" "lib32-gcc-libs")
source=("https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/${_pkgname}/${pkgver}-11/${_pkgname}_${pkgver}.orig.tar.gz"
	"libsidplay-1.36.59-gcc43.patch"
	"g++-6_build.patch")
md5sums=('37c51ba4bd57164b1b0bb7b43b9adece'
         'c24d7bca2639f4fee03c40c7dcaadfee'
         '4fbea288f7f427818462343e33794356')

prepare() {
cd ${_pkgname}-${pkgver}
patch -Np1 -i ../libsidplay-1.36.59-gcc43.patch
patch -Np1 -i ../g++-6_build.patch
}

build() {
cd ${_pkgname}-${pkgver}
export CC="gcc -m32"
export CXX="g++ -m32 -Wno-narrowing"
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

./configure --prefix=/usr --libdir=/usr/lib32 --libexecdir=/usr/lib32

make
}

package() {
cd ${_pkgname}-${pkgver}
make DESTDIR=${pkgdir} install

cd "$pkgdir/usr"
rm -rf include/
}
