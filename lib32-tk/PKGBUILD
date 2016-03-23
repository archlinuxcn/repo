# Maintainer: GordonGR <ntheo1979@gmail.com>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=lib32-tk
pkgver=8.6.4
pkgrel=3
pkgdesc="A windowing toolkit for use with tcl"
arch=('x86_64')
url="http://tcl.sourceforge.net/"
license=('custom')
# "lib32-tcl=${pkgver}"
depends=('lib32-libxss' 'lib32-libxft' 'lib32-tcl>=8.6.4' 'tk')
options=('staticlibs')
source=("http://downloads.sourceforge.net/sourceforge/tcl/tk${pkgver}-src.tar.gz")
md5sums=('261754d7dc2a582f00e35547777e1fea')

build() {
cd tk${pkgver}/unix
export CC='gcc -m32'
export CXX='g++ -m32'
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export LDFLAGS+='-L/usr/lib32'
./configure --prefix=/usr --mandir=/usr/share/man \
  --enable-threads --disable-rpath \
  --libdir=/usr/lib32 \
  --libexecdir=/usr/lib32 \
  --with-tcl=/usr/lib32/
make
}

check() {
cd tk${pkgver}/unix
# make test
}

package() {
cd tk${pkgver}/unix
make INSTALL_ROOT="${pkgdir}" install install-private-headers
mv "${pkgdir}/usr/bin/wish${pkgver%.*}" \
  "${pkgdir}/usr/bin/wish${pkgver%.*}-32"
ln -sf wish${pkgver%.*}-32 "${pkgdir}/usr/bin/wish-32"
ln -sf libtk${pkgver%.*}.so "${pkgdir}/usr/lib32/libtk.so"

rm -rf "${pkgdir}/usr/"{share/man,include,lib}

install -Dm644 license.terms "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

# remove buildroot traces
sed -e "s#${srcdir}/tk${pkgver}/unix#/usr/lib32#" \
    -e "s#${srcdir}/tk${pkgver}#/usr/include#" \
    -i "${pkgdir}/usr/lib32/tkConfig.sh"
}
