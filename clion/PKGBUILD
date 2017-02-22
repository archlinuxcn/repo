# Maintainer: Michael Hansen <zrax0111 gmail com>
# Contributor: Raphaël Doursenaud <rdoursenaud@gpcsolutions.fr>
# Contributor: Jesse Jaara <gmail.com: jesse.jaara>

# Uncomment if you want to disable compressing the package to save some time.
#PKGEXT=.pkg.tar

pkgbase=clion
pkgname=(clion clion-jre clion-cmake clion-gdb clion-lldb)
_pkgname=clion
_dlname=CLion
# Make sure to use vercmp to check version is seen as newer. Bump epoch if not.
pkgver=2016.3.3
pkgrel=1
# Bump when JetBrains uses silly letters in stable releases
epoch=1
pkgdesc="C/C++ IDE. Free 30-day trial."
arch=('x86_64')
options=(!strip)
url="http://www.jetbrains.com/${_pkgname}"
license=('custom')
makedepends=('rsync')
source=("https://download.jetbrains.com/cpp/${_dlname}-${pkgver}.tar.gz"
        "jetbrains-${pkgbase}.desktop")
sha256sums=('057c7b5bf464aee51d9f8d01f8c89ed7334e52e378204cddf28e86e2c1f3f1ff'
            '9f0f4335f410e0587018c85ebfcf4b65a7a47ad682a58972624378953ef288d6')
noextract=("${_dlname}-${pkgver}.tar.gz")

build() {
    mkdir -p "${srcdir}/opt/${pkgbase}"
    bsdtar --strip-components 1 -xf "${_dlname}-${pkgver}.tar.gz" \
           -C "${srcdir}/opt/${pkgbase}"

    rm -f "${srcdir}/opt/${pkgbase}/bin/libyjpagent-linux.so"
    rm -f "${srcdir}/opt/${pkgbase}/bin/fsnotifier"
}

package_clion() {
    optdepends=(
        'clion-jre: JetBrains custom Java Runtime (Recommended)'
        'clion-cmake: JetBrains packaged CMake tools'
        'clion-gdb: JetBrains packaged GNU debugger'
        'clion-lldb: JetBrains packaged LLVM debugger'
        'java-runtime: JRE - Required if clion-jre is not installed'
        'cmake: Build system - Required if clion-cmake is not installed'
        'gdb: native GNU debugger'
        'lldb: native LLVM debugger'
        'gcc: GNU compiler'
        'clang: LLVM compiler'
        'biicode: C/C++ dependency manager'
        'gtest: C++ testing'
        'swift: Swift programming language support (Also requires the plugin)'
        'python: Python 3 programming language support'
        'python2: Python 2 programming language support'
        'doxygen: Code documentation generation'
    )

    rsync -rtl "${srcdir}/opt" "${pkgdir}" \
          --exclude=/opt/${pkgbase}/jre \
          --exclude=/opt/${pkgbase}/bin/cmake \
          --exclude=/opt/${pkgbase}/bin/gdb \
          --exclude=/opt/${pkgbase}/bin/lldb

    mkdir -p "${pkgdir}/usr/bin/"
    mkdir -p "${pkgdir}/usr/share/applications/"
    mkdir -p "${pkgdir}/usr/share/pixmaps/"
    mkdir -p "${pkgdir}/usr/share/licenses/${pkgbase}"

    install -m 644 "${srcdir}/jetbrains-${pkgbase}.desktop" \
            "${pkgdir}/usr/share/applications/"

    ln -s "/opt/${pkgbase}/bin/${_pkgname}.svg" \
            "${pkgdir}/usr/share/pixmaps/${pkgbase}.svg"
    ln -s "/opt/${pkgbase}/license/CLion_Preview_License.txt" \
            "${pkgdir}/usr/share/licenses/${pkgbase}"
    ln -s "/opt/${pkgbase}/bin/${_pkgname}.sh" \
            "${pkgdir}/usr/bin/${pkgbase}"
}

package_clion-jre() {
    install -d -m755 "${pkgdir}/opt/${pkgbase}"
    rsync -rtl "${srcdir}/opt/${pkgbase}/jre" "${pkgdir}/opt/${pkgbase}"
}

package_clion-cmake() {
    install -d -m755 "${pkgdir}/opt/${pkgbase}/bin"
    rsync -rtl "${srcdir}/opt/${pkgbase}/bin/cmake" "${pkgdir}/opt/${pkgbase}/bin"
}

package_clion-gdb() {
    install -d -m755 "${pkgdir}/opt/${pkgbase}/bin"
    rsync -rtl "${srcdir}/opt/${pkgbase}/bin/gdb" "${pkgdir}/opt/${pkgbase}/bin"
}

package_clion-lldb() {
    install -d -m755 "${pkgdir}/opt/${pkgbase}/bin"
    rsync -rtl "${srcdir}/opt/${pkgbase}/bin/lldb" "${pkgdir}/opt/${pkgbase}/bin"
}
