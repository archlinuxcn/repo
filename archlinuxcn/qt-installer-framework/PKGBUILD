# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Co-Maintainer Skycoder42 <skycoder42.de@gmx.de>
# Contributor: Danny Dutton <duttondj@vt.edu>

pkgbase=qt-installer-framework
pkgname=(qt-installer-framework qt-installer-framework-docs)
pkgver=3.0.6
pkgrel=1
pkgdesc='The Qt Installer Framework used for the Qt SDK installer'
arch=('x86_64')
url='http://qt-project.org/wiki/Qt-Installer-Framework'
license=('FDL' 'LGPL')
makedepends=('qt5-tools' 'qt5-declarative' 'clang')
source=("https://download.qt.io/official_releases/${pkgbase}/${pkgver}/${pkgbase}-opensource-src-${pkgver}.tar.gz")
#md5sums=('8907ee07987010f0998e976a13318be3')
sha256sums=('5e32adca8f27f8a0730a036cb233b3668d158a546b20e41256e2811e47bade15')

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
