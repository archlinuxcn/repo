# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: Danny Dutton <duttondj@vt.edu>

pkgbase=qt-installer-framework
pkgname=(qt-installer-framework qt-installer-framework-docs)
pkgver=3.0.1
pkgrel=1
pkgdesc='The Qt Installer Framework used for the Qt SDK installer'
arch=('i686' 'x86_64')
url='http://qt-project.org/wiki/Qt-Installer-Framework'
license=('FDL' 'LGPL')
makedepends=('qt5-tools' 'qt5-declarative')
source=("https://download.qt.io/official_releases/${pkgbase}/${pkgver}/${pkgbase}-opensource-src-${pkgver}.tar.gz")
sha256sums=('e1aca203f6f34e5f79b2e16d0ab50016875be877920cc4a66fef7c84b60acb7a')

build() {
  # Build tools and libraries
  qmake-qt5 ./installerfw.pro
  make
  make docs
}

package_qt-installer-framework() {
  pkgdesc='The Qt Installer Framework used for the Qt SDK installer'
  depends=('qt5-declarative')
  optdepends=('python: needed to run some sample tests'
              'qt-installer-framework-docs: examples and documentation files')

  cd "${srcdir}"
  # Install executables
  install -m 755 -d "${pkgdir}/usr/bin"
  install -m 755 -t "${pkgdir}/usr/bin" "bin/archivegen" \
                                        "bin/binarycreator" \
                                        "bin/devtool" \
                                        "bin/installerbase" \
                                        "bin/repogen"
  # Install libraries
  install -m 755 -d "${pkgdir}/usr/lib"
  install -m 755 -t "${pkgdir}/usr/lib" "lib/libinstaller.so.1.0.0"
  ln -s "libinstaller.so.1.0.0" "${pkgdir}/usr/lib/libinstaller.so"
  ln -s "libinstaller.so.1.0.0" "${pkgdir}/usr/lib/libinstaller.so.1"
  ln -s "libinstaller.so.1.0.0" "${pkgdir}/usr/lib/libinstaller.so.1.0"
  # Install tests
  install -m 755 -d "${pkgdir}/usr/lib/${pkgbase}"
  cp -a -t "${pkgdir}/usr/lib/${pkgbase}/" "tests"
  # Install licenses
  install -m 755 -d "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" "3RDPARTY" \
                                                              "LICENSE.GPL3-EXCEPT" \
                                                              "LICENSE.FDL"
}

package_qt-installer-framework-docs() {
  pkgdesc='The Qt Installer Framework used for the Qt SDK installer (examples and documentation)'
  arch=('any')

  cd "${srcdir}"
  # Install examples
  install -m 755 -d "${pkgdir}/usr/share/${pkgbase}"
  cp -a -t "${pkgdir}/usr/share/${pkgbase}/" "examples"
  # Install licenses
  install -m 755 -d "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" "3RDPARTY" \
                                                              "LICENSE.GPL3-EXCEPT" \
                                                              "LICENSE.FDL"
  # Install documentation
  install -m 755 -d "${pkgdir}/usr/share/doc/${pkgbase}"
  cp -a "doc/html" "${pkgdir}/usr/share/doc/${pkgbase}"
  install -m 755 -d "${pkgdir}/usr/share/doc/qt"
  install -m 644 -t "${pkgdir}/usr/share/doc/qt" "doc/ifw.qch"
}
