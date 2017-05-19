#Package from: isoft-linux <github.com/isoft-linux/kjieba>
#Maintainer : Sasasu <lizhaolong0123@gmail.com>
pkgname=kjieba
pkgver=20170519
pkgrel=1
pkgdesc="DBus interface of libcppjieba && Chinese2Pinyin for KDE5"
arch=('i686' 'x86_64')
url="https://github.com/isoft-linux/kjieba"
license=('GPL2')
depends=('gcc' 'qt5-base' 'krunner')
makedepends=('git' 'make' 'extra-cmake-modules' 'extra-cmake-modules' 'ki18n' 'kdbusaddons' 'kservice' 'kactivities' 'kactivities-stats' 'kio' 'python')
source=("$pkgname::git+https://github.com/isoft-linux/kjieba"
        "libcppjieba::git+https://github.com/yanyiwu/libcppjieba")
md5sums=('SKIP'
         'SKIP')

build() {
	cd "$srcdir"/"$_pkgname/$pkgname"
	cp  -r ../libcppjieba/* ./libcppjieba
	mkdir -p build
	cd build
	cmake .. -DCMAKE_INSTALL_PREFIX=/usr    \
	-DLIB_INSTALL_DIR=lib   \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON   \
	-DENABLE_DEBUG=OFF
	make
}

package() {
	cd "$srcdir"/"$_pkgname/$pkgname"
	cd build
	make install DESTDIR="${pkgdir}"
}
