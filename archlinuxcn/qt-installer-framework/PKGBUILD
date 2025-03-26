# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Co-Maintainer Skycoder42 <skycoder42.de@gmx.de>
# Contributor: Danny Dutton <duttondj@vt.edu>

pkgbase=qt-installer-framework
pkgname=(qt-installer-framework qt-installer-framework-docs)
pkgver=4.8.1
pkgrel=3
pkgdesc='The Qt Installer Framework used for the Qt SDK installer'
arch=('x86_64')
url='http://qt-project.org/wiki/Qt-Installer-Framework'
license=('GFDL-1.3-only' 'LicenseRef-GPL3-EXCEPT')
makedepends=('qt6-tools' 'qt6-declarative' 'qt6-5compat' 'clang' 'libarchive')
source=("${pkgbase}-${pkgver}.tar.gz"::"https://github.com/qtproject/installer-framework/archive/${pkgver}.tar.gz"
        "qt6_7.patch"::"https://github.com/qtproject/installer-framework/commit/0b1103b41db101d2a509e1bdf5385b29410e41e9.patch"
        "qt6_8.patch"::"https://github.com/qtproject/installer-framework/commit/d24e8c20ea263e4528f11553a4dfbd93433b203e.patch"
        "core5compat.patch"
        "qt6_8_1.patch")
sha256sums=('cab2fa4d5f04298cfe4f63b9721bb389d1efb0fa7333a0ed0795b4ff51108978'
            '7e1961f741f0de55b01d568b57a3f4a25841c774b6eb293866272e048d73412a'
            '586e80274375ace226476ecc8014a8391d9ac1fc70d9e382fb1b25582e815fb8'
            'e6013877697814051f1e1483d106da05b612ac24d9b43c868764f77d91b91b20'
            '94e36e7195895a3076158aa978681bb989ac19b9d6fe8a00662f156f6c076860')
options=('!lto')

prepare() {
  cd "installer-framework-${pkgver}"
  patch -p1 -i "${srcdir}/qt6_7.patch"
  patch -p1 -i "${srcdir}/qt6_8.patch"
  patch -p1 -i "${srcdir}/qt6_8_1.patch"
  patch -p1 -i "${srcdir}/core5compat.patch"
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
  depends=('qt6-declarative' 'libarchive')
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
