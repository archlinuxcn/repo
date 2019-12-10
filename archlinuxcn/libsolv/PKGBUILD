pkgname=libsolv
pkgver=0.7.10
pkgrel=1
pkgdesc="Library for solving packages and reading repositories"
arch=('i686' 'x86_64')
url="https://github.com/openSUSE/$pkgname"
license=('custom:BSD')
depends=('bzip2' 'expat' 'rpm-org' 'xz' 'zchunk' 'zlib' 'zstd')
makedepends=('cmake' 'perl' 'python' 'ruby' 'swig')
optdepends=('perl: for perl bindings'
            'python: for python bindings'
            'ruby: for ruby bindings')
source=("$url/archive/$pkgver/$pkgname-$pkgver.tar.gz")
md5sums=('bc2bf0cc9a444dad0c3908bcae2d7f29')

prepare() {
	cd "$pkgname-$pkgver"
	rm -rf build
	mkdir build
}

build() {
	cd "$pkgname-$pkgver"/build

	cmake -DCMAKE_BUILD_TYPE=Release \
	      -DCMAKE_C_FLAGS="$CFLAGS $CPPFLAGS" \
	      -DCMAKE_INSTALL_PREFIX=/usr \
	      -DCMAKE_INSTALL_LIBDIR=lib \
	      -DUSE_VENDORDIRS=ON \
	      -DFEDORA=1 \
	      -DENABLE_APPDATA=ON \
	      -DENABLE_ARCHREPO=ON \
	      -DENABLE_BZIP2_COMPRESSION=ON \
	      -DENABLE_COMPLEX_DEPS=1 \
	      -DENABLE_COMPS=ON \
	      -DENABLE_CONDA=ON \
	      -DENABLE_CUDFREPO=ON \
	      -DENABLE_DEBIAN=ON \
	      -DENABLE_HAIKU=OFF \
	      -DENABLE_HELIXREPO=ON \
	      -DENABLE_LZMA_COMPRESSION=ON \
	      -DENABLE_MDKREPO=ON \
	      -DENABLE_PERL=ON \
	      -DENABLE_PUBKEY=ON \
	      -DENABLE_PYTHON=ON \
	      -DENABLE_RPMDB=ON \
	      -DENABLE_RPMDB_BYRPMHEADER=ON \
	      -DENABLE_RPMMD=ON \
	      -DENABLE_RPMPKG=ON \
	      -DENABLE_RUBY=ON \
	      -DENABLE_SUSEREPO=ON \
	      -DENABLE_TCL=OFF \
	      -DENABLE_ZCHUNK_COMPRESSION=ON \
	      -DWITH_SYSTEM_ZCHUNK=ON \
	      -DENABLE_ZSTD_COMPRESSION=ON \
	      -DMULTI_SEMANTICS=ON \
	      -DWITH_LIBXML2=OFF \
	      ..

	make
}

check() {
	cd "$pkgname-$pkgver"/build
	make ARGS="-V" test
}

package() {
	cd "$pkgname-$pkgver"/build
	make DESTDIR="$pkgdir/" install

	install -Dp -m644 ../LICENSE.BSD "$pkgdir/usr/share/licenses/$pkgname/LICENSE.BSD"
	install -Dp -m644 ../README      "$pkgdir/usr/share/doc/$pkgname/README"
}

# vim: set ft=sh ts=4 sw=4 noet:
