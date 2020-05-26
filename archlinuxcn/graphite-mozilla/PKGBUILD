# Maintainer: Thaodan <theodorstormgrade@gmail.com>
# Arch Maintainer: AndyRTR <andyrtr@archlinux.org>

# This pkg contains geckoextra methods needed by the sandbox of gecko.
# The source of these methods is from:
# https://hg.mozilla.org/mozilla-central/file/tip/gfx/graphite2
#
# The source is the same as from mozilla except that the mozilla methods
# are linked to the original library instead of staticly linking the library
# to gecko.

_pkgname=graphite
pkgname=$_pkgname-mozilla
pkgver=1.3.14
pkgrel=1
epoch=1
arch=('x86_64')
url="https://github.com/silnrsi/graphite"
pkgdesc='reimplementation of the SIL Graphite text processing engine with mozilla patches for gecko'
license=('LGPL' 'GPL' 'custom')
depends=('gcc-libs')
provides=("$_pkgname")
conflicts=("$_pkgname")
makedepends=('cmake' 'freetype2' 'python'
             # for documentation
             'doxygen' 'dblatex' 'graphviz' 'asciidoc')
checkdepends=('python-fonttools')
options=('!emptydirs')
# https://github.com/silnrsi/graphite/releases/download/1.3.14/graphite2-1.3.14.sha256sum
source=(https://github.com/silnrsi/graphite/releases/download/${pkgver}/graphite2-${pkgver}.tgz
       'add_mozilla_geckoextra.patch')
sha256sums=('f99d1c13aa5fa296898a181dff9b82fb25f6cc0933dbaa7a475d8109bd54209d'
            'ab57e21fbc34da1e816c855b89cea14d82a237064c22b3867466264da5465e5f')

prepare()
{
  cd graphite2-${pkgver}
  patch -Np1 < "$srcdir/add_mozilla_geckoextra.patch"
}

build() {
  mkdir build
  cd build
  cmake -G "Unix Makefiles" ../graphite2-${pkgver} \
	-DCMAKE_C_FLAGS:STRING="${CFLAGS}" \
	-DCMAKE_INSTALL_PREFIX=/usr \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DGRAPHITE2_COMPARE_RENDERER=OFF \

  # fix unwanted -O3 cflag (taken form Debian)
  find . -type f ! -name "rules" ! -name "changelog" -exec sed -i -e 's/\-O3//g' {} \;

  make 
  make -j1 docs
}

check() {
  cd "${srcdir}"/build
  ctest || true
}

package() {
  cd "${srcdir}"/build
  make DESTDIR="$pkgdir/" install
  # install doc files
  mkdir -p "${pkgdir}"/usr/share/doc/graphite2/api
  cp -vrf doc/doxygen/{html,latex/refman.pdf} "${pkgdir}"/usr/share/doc/graphite2/api
  cp -vrf doc/{GTF,manual}.html "${pkgdir}"/usr/share/doc/graphite2

  # licenses
  mkdir -p "${pkgdir}"/usr/share/licenses/${_pkgname}
  install -m644 "${srcdir}"/graphite2-${pkgver}/COPYING "${pkgdir}"/usr/share/licenses/${_pkgname}/
}
