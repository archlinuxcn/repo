# Maintainer: Jesse R. Adams <jesse -at- techno -dash- geeks -dot- org>
pkgname=ruby1.8
_pkgname='ruby'
pkgver=1.8.7_p374
_pkgver="${pkgver/_/-}"
pkgrel=2
pkgdesc='The obsolete version of the ruby programming language. Consider 2.x instead.'
arch=('i686' 'x86_64' 'arm')
license=('custom')
url='http://www.ruby-lang.org/en/'
provides=('ruby=1.8.7')
options=('!emptydirs')
makedepends=('tk')
depends=('gdbm' 'db' 'openssl' 'zlib' 'readline')
optdepends=('tk: for Ruby/TK')

source=("ftp://ftp.ruby-lang.org/pub/ruby/1.8/$_pkgname-$_pkgver.tar.bz2" "fix.patch")
md5sums=('83c92e2b57ea08f31187060098b2200b' 'f560402603b3dca36d4a6abfcb180cb9')

_optimal_make_jobs() {
	if [ -r /proc/cpuinfo ]; then
		local core_count=$(grep -Fc processor /proc/cpuinfo)
	else
		local core_count=0
	fi

	if [ $core_count -gt 1 ]; then
		echo -n $[$core_count-1]
	else
		echo -n 1
	fi
}

build() {
  echo
  echo
  echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
  echo "!!! WARNING !!! Ruby 1.8.7 is no longer supported."
  echo "Please consider upgrading to ruby 2.x instead."
  echo "This package will not be maintained for ArchLinux much longer."
  echo "See https://www.ruby-lang.org/en/news/2013/06/30/we-retire-1-8-7/ for more info!"
  echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
  echo
  echo
  sleep 5

	cd "${srcdir}/${_pkgname}-${_pkgver}"

	msg 'Running configure...'
	./configure \
		--prefix=/opt/ruby1.8 \
		--disable-rpath \
		--enable-shared \
		--enable-pthread \
		CFLAGS="-O2 -fno-tree-dce -fno-optimize-sibling-calls"

	msg 'Applying patch...'
	patch -Np1 < ${srcdir}/fix.patch

	msg 'Running make...'
	make -j$(_optimal_make_jobs)
}

package() {
	cd "${srcdir}/${_pkgname}-${_pkgver}"

	make DESTDIR="$pkgdir" install

	install -Dm644 COPYING "$pkgdir/usr/share/licenses/$pkgname/COPYING"

	install -dm755 $pkgdir/usr/bin
	install -dm755 $pkgdir/usr/lib
	for i in erb irb rdoc ri ruby testrb; do
		ln -s /opt/ruby1.8/bin/$i $pkgdir/usr/bin/$i-1.8
	done
	ln -s /opt/ruby1.8/lib/libruby.so.1.8 $pkgdir/usr/lib/libruby.so.1.8
}
