pkgname=libsolv
pkgver=0.7.17
pkgrel=1
pkgdesc="Library for solving packages and reading repositories"
arch=('i686' 'x86_64')
url="https://github.com/openSUSE/$pkgname"
license=('custom:BSD')
depends=('bzip2' 'expat' 'rpm-tools' 'xz' 'zchunk' 'zlib' 'zstd')
makedepends=('cmake>=3.13' 'perl' 'python' 'ruby' 'swig')
optdepends=('perl: for perl bindings'
            'python: for python bindings'
            'ruby: for ruby bindings')
source=("$url/archive/$pkgver/$pkgname-$pkgver.tar.gz")
md5sums=('0c0394275be0c5eff1e76abacfb28705')

build() {
	cd "$pkgname-$pkgver"

	cmake -B build \
	      -DCMAKE_BUILD_TYPE=Release \
	      -DCMAKE_C_FLAGS_RELEASE='-DNDEBUG' \
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
	      -DENABLE_RPMDB_LIBRPM=ON \
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

	make -C build
}

check() {
	cd "$pkgname-$pkgver"

	make -C build ARGS="-V" test
}

package() {
	cd "$pkgname-$pkgver"

	make -C build DESTDIR="$pkgdir/" install

	install -Dp -m644 LICENSE.BSD "$pkgdir/usr/share/licenses/$pkgname/LICENSE.BSD"
	install -Dp -m644 README      "$pkgdir/usr/share/doc/$pkgname/README"
}

# vim: set ft=sh ts=4 sw=4 noet:
