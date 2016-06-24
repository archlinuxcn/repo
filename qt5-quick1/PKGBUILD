# Maintainer: AudioLinux  <audiolinux AT fastmail DOT fm>
# Contributor: almack

pkgname=qt5-quick1
pkgver=5.7.0
_pkgver=5.7.0
pkgrel=2
arch=('i686' 'x86_64')
url='http://qt-project.org/'
pkgdesc='Qt Declarative is provided for Qt 4 compatibility'
license=('LGPL2.1' 'GPL3')
#options=("debug")
depends=('qt5-webkit' 'qt5-script')
makedepends=('git')
source=("git+https://code.qt.io/qt/qtquick1.git#branch=5.7")
sha1sums=('SKIP')

_prlfix() {
  # Fix wrong path in prl files
  find "${pkgdir}/usr/lib" -type f -name '*.prl' \
    -exec sed -i -e '/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/' {} \;
}

prepare() {
  cd qtquick1

  if [ ! -d include ]; then
    syncqt.pl-qt5 -version 5.7.0 sync.profile
  fi
}

build() {
  cd qtquick1
  mkdir -p build
  cd build
  qmake-qt5 ..

  make

  make docs
}

package() {
  cd qtquick1/build
  make INSTALL_ROOT="${pkgdir}" install
  make INSTALL_ROOT="${pkgdir}" install_docs

  _prlfix
  
  # create some symlinks in /usr/bin, postfixed with -qt5
  install -d "${pkgdir}"/usr/bin
  for i in $(ls ${pkgdir}/usr/lib/qt5/bin); do
      ln -s /usr/lib/qt5/bin/${i} ${pkgdir}/usr/bin/${i}-qt5
  done

  install -D -m644 ../LGPL_EXCEPTION.txt \
    "${pkgdir}"/usr/share/licenses/${pkgname}/LGPL_EXCEPTION.txt
}
