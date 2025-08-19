# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Co-Maintainer Skycoder42 <skycoder42.de@gmx.de>
# Contributor: Danny Dutton <duttondj@vt.edu>

pkgbase=qt-installer-framework
pkgname=(qt-installer-framework qt-installer-framework-docs)
pkgver=4.10.0
pkgrel=1
pkgdesc='The Qt Installer Framework used for the Qt SDK installer'
arch=('x86_64')
url='http://qt-project.org/wiki/Qt-Installer-Framework'
license=('GFDL-1.3-only' 'LicenseRef-GPL3-EXCEPT')
makedepends=('qt6-tools' 'qt6-declarative' 'qt6-5compat' 'clang' 'libarchive')
source=("${pkgbase}-${pkgver}.tar.gz"::"https://github.com/qtproject/installer-framework/archive/${pkgver}.tar.gz"
        "core5compat.patch"
        "commandlineparser.patch")
sha256sums=('b6f6f17e9038f29d3443aca9f739148c966cf38989ea62e02267c15e10682283'
            'e6013877697814051f1e1483d106da05b612ac24d9b43c868764f77d91b91b20'
            'ebe83ebbb786ce0409182d81a39e1de4eb6592d1c66b6c0967fabd21b5480499')
options=('!lto')

prepare() {
  cd "installer-framework-${pkgver}"
  patch -p1 -i "${srcdir}/core5compat.patch"
  patch -p1 -i "${srcdir}/commandlineparser.patch"
}

build() {
  # Build tools and libraries
  cd "installer-framework-${pkgver}"
  /usr/lib/qt6/bin/qmake CONFIG+=libarchive QT+=core5compat .
  make -w --no-silent
  make html_docs_ifw
}

package_qt-installer-framework() {
  pkgdesc='The Qt Installer Framework used for the Qt SDK installer'
  depends=('qt6-tools' 'qt6-declarative' 'qt6-5compat' 'libarchive')
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
