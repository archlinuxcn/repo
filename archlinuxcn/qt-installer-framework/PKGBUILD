# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Co-Maintainer Skycoder42 <skycoder42.de@gmx.de>
# Contributor: Danny Dutton <duttondj@vt.edu>

pkgbase=qt-installer-framework
pkgname=(qt-installer-framework qt-installer-framework-docs)
pkgver=4.7.0
pkgrel=1
pkgdesc='The Qt Installer Framework used for the Qt SDK installer'
arch=('x86_64')
url='http://qt-project.org/wiki/Qt-Installer-Framework'
license=('GFDL-1.3-only' 'LicenseRef-GPL3-EXCEPT')
makedepends=('qt5-tools' 'qt5-declarative' 'clang')
source=("${pkgbase}-${pkgver}.tar.gz"::"https://github.com/qtproject/installer-framework/archive/${pkgver}.tar.gz"
        "componentalias_const_qjsonarray.patch")
sha256sums=('bb5cccd294fa357ca6571397e22adb8e88bf6827adf96d02152b95f01d4c4cb9'
            '7190ba7321dde12b4b13963f1b6d94f10299766980578f2498f21f985a4f2e46')

prepare() {
  cd "installer-framework-${pkgver}"
  patch -p1 -i "${srcdir}/componentalias_const_qjsonarray.patch"
}

build() {
  # Build tools and libraries
  cd "installer-framework-${pkgver}"
  qmake .
  make
  make html_docs_ifw
}

package_qt-installer-framework() {
  pkgdesc='The Qt Installer Framework used for the Qt SDK installer'
  depends=('qt5-declarative')
  optdepends=('python: needed to run some sample tests'
              'qt-installer-framework-docs: examples and documentation files')

  cd "installer-framework-${pkgver}"
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

  cd "installer-framework-${pkgver}"
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
}
