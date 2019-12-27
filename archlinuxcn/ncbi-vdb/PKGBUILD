# This is the PKGBUILD for ncbi-vdb
# Maintainer: Aaron Baker <aa{last name}99{at}gmail{dt}org>
# Maintainer: Georgios Amanakis <g_amanakis{at}yahoo{dt}com>

pkgname=ncbi-vdb
pkgver=2.10.0
pkgrel=2
pkgdesc="The SRA Toolkit and SDK from NCBI is a collection of tools and libraries for using data in the INSDC Sequence Read Archives."
arch=('x86_64')
url="https://github.com/ncbi/ncbi-vdb"
depends=('libxml2' 'ngs' 'hdf5')
provides=('ncbi-vdb')
license=('custom:PublicDomain')
options=('!strip' 'staticlibs')
source=("https://github.com/ncbi/ncbi-vdb/archive/$pkgver.tar.gz" "$pkgname.patch")
sha256sums=('a6cc88e8d12f536dc96d5f60698d0ef4cf2f63e31d3d12d23da39b1de39563e1'
            '62550416a3bd48ad8d8810a4fde593f1e6fdc6b091afbcf903842f8a43da9f58')

prepare(){
  cd "${pkgname}-${pkgver}"
  # ncbi build process frequently checks if we are root user which interferes 
  #   with makepkg use of fakeroot
  patch -p1 -i $srcdir/$pkgname.patch 
}

build(){
  cd "${pkgname}-${pkgver}"
  ./configure --prefix="$pkgdir/usr/" \
	--build-prefix="$srcdir/build_dir" \
	--with-ngs-sdk-prefix="/usr" \
	--with-ngs-java-prefix=/usr/share/java/ngs/ngs-java.jar
  make
}

#check(){
#  cd "${pkgname}-${pkgver}"
#  make -k test
#}

package(){
  cd "$pkgname-$pkgver"
  # ncbi does not use autoconf/automake so there is no respect for DESTDIR
  #   but there is a ROOT(dir)
#  make "ROOT=$pkgdir" install
  make install
  mv "$pkgdir/usr/lib64" "$pkgdir/usr/lib"

  # the source of this package is required by others
  # TODO is there somewhere to put this for namcap not to complain?
  mkdir -p "$pkgdir/usr/src/${pkgname}-${pkgver}/build_dir"
  cp -r . "$pkgdir/usr/src/${pkgname}-${pkgver}"
  cp -a "$srcdir/build_dir" "$pkgdir/usr/src/${pkgname}-${pkgver}"

  # add the license
  mkdir -p "$pkgdir/usr/share/licenses/${pkgname}"
  cp "LICENSE" "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"

  # TODO without this a link from libncbi-vdb-static.a -> libncbi-vdb.a is dead because 
  #   libncbi-vdb.a gets removed somehow??
#  cd "$pkgdir/usr/lib/"
#  ln -sf "libncbi-vdb.a.$pkgver" libncbi-vdb-static.a
#  ln -sf "libncbi-wvdb.a.$pkgver" libncbi-wvdb-static.a
}
