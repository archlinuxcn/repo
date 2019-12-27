# This is the PKGBUILD for ngs
# Maintainer: Aaron Baker <aa{last name}99{at}gmail{dt}org>
# Maintainer: Georgios Amanakis <g_amanakis{at}yahoo{dt}com>

pkgname=ngs
pkgver=2.10.0
pkgrel=2
pkgdesc="A new, domain-specific API for accessing reads, alignments and pileups produced from Next Generation Sequencing."
arch=('x86_64')
url="https://github.com/ncbi/ngs"
depends=('java-environment' 'perl-file-copy-recursive' 'zlib')
provides=('ngs')
license=('custom:PublicDomain')
source=("https://github.com/ncbi/ngs/archive/$pkgver.tar.gz" "$pkgname.patch")
sha256sums=('4139adff83af213d7880bc80d1c0f5ee9b00c6c4e615d00aa47aaa267e40ed25'
            '004eb006e9bbd9f4368c54663e7d991833aeae3e9c6583e61566340cd04d5bb6')

prepare(){
  cd "${pkgname}-${pkgver}"
  # ncbi build process frequently checks if we are root user which interferes 
  #   with makepkg use of fakeroot
  patch -p1 -i $srcdir/$pkgname.patch 
}

build(){
  cd "${pkgname}-${pkgver}"
  ./configure --prefix="$pkgdir/usr/" --build-prefix="$srcdir/build"
  make -C ngs-sdk
  make -C ngs-java
}

#check(){
#  cd "${pkgname}-${pkgver}"
#  make -k test
#}

package(){
  cd "$pkgname-$pkgver"
  # ncbi does not use autoconf/automake so there is no respect for DESTDIR
  #   but there is a ROOT(dir)
  #make "ROOT=$pkgdir" install
  make -C ngs-sdk install
  make -C ngs-java install

  # add license
  mkdir -p "$pkgdir/usr/share/licenses/${pkgname}"
  cp "LICENSE" "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"

  # reorganize files from build process to fit Arch
  mv "$pkgdir/usr/lib64" "$pkgdir/usr/lib"
  mkdir -p "$pkgdir/usr/share/java"
  mv "$pkgdir/usr/jar" "$pkgdir/usr/share/java/$pkgname"
}
