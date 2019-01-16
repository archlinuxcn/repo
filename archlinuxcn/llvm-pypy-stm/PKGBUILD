# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Contributor: Armin K. <krejzi at email dot com>
# Contributor: Christian Babeux <christian.babeux@0x80.ca>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Roberto Alsina <ralsina@kde.org>
# Contributor: Tomas Lindquist Olsen <tomas@famolsen.dk>
# Contributor: Anders Bergh <anders@archlinuxppc.org>
# Contributor: Tomas Wilhelmsson <tomas.wilhelmsson@gmail.com>

pkgbase=llvm-pypy-stm
pkgname=('llvm-pypy-stm' 'llvm-libs-pypy-stm' 'clang-pypy-stm' 'clang-analyzer-pypy-stm' 'clang-tools-extra-pypy-stm')
_pkgname='llvm'
pkgver=201645
pkgrel=2
arch=('i686' 'x86_64')
url="http://llvm.org"
license=('custom:University of Illinois')
makedepends=('subversion' 'libffi' 'python2' 'python-sphinx' 'chrpath')

# this is always the latest svn so debug info can be useful
options=('staticlibs' '!strip')

source=("${_pkgname}::svn+http://llvm.org/svn/llvm-project/llvm/trunk#revision=201645"
        "clang::svn+http://llvm.org/svn/llvm-project/cfe/trunk#revision=201645"
        "clang-tools-extra::svn+http://llvm.org/svn/llvm-project/clang-tools-extra/trunk#revision=201645"
        "compiler-rt::svn+http://llvm.org/svn/llvm-project/compiler-rt/trunk#revision=201645"
        "addrspacecast-in-constant.diff"
        "no-introduce-bogus-cast-in-combine.diff"
        "no-memset-creation-with-addrspace.diff"
        "llvm-Config-config.h"
        "llvm-Config-llvm-config.h"
        )
sha256sums=('SKIP'
            'SKIP'    
            'SKIP'
            'SKIP'
            'd5e624c8921802b2096f0b0279fb2ef3973dad0ca009d416ac15c839c8dea91f'
            '3113e118aa01968997639dd747b25ba9b5bcaa38415eae0cb9a8e63c703db44b'
            '16dd8e9cc3794189ebde5ee39a99e1a5014185f3ecb369e3ca1d2d22032a1576'
            '312574e655f9a87784ca416949c505c452b819fad3061f2cde8aced6540a19a3'
            '597dc5968c695bbdbb0eac9e8eb5117fcd2773bc91edf5ec103ecffffab8bc48'
            )

pkgver()
{
    cd "${srcdir}/${_pkgname}"
    svnversion | tr -d [A-z]
}

prepare() {
    cd "${srcdir}/${_pkgname}"

    svn export "${srcdir}/clang" tools/clang
    svn export "${srcdir}/clang-tools-extra" tools/clang/tools/extra
    svn export "${srcdir}/compiler-rt" projects/compiler-rt

    # Fix docs installation directory
    sed -e 's:$(PROJ_prefix)/docs/llvm:$(PROJ_prefix)/share/doc/llvm:' \
        -i Makefile.config.in

    # Fix definition of LLVM_CMAKE_DIR in LLVMConfig.cmake
    sed -e '/@LLVM_CONFIG_CMAKE_DIR@/s:$(PROJ_cmake):$(PROJ_prefix)/share/llvm/cmake:' \
        -i cmake/modules/Makefile

    # apply pypy-stm patchs
    patch -p0 < ../addrspacecast-in-constant.diff
    patch -p0 < ../no-introduce-bogus-cast-in-combine.diff
    patch -p0 < ../no-memset-creation-with-addrspace.diff

}

build() {
    cd "${srcdir}/${_pkgname}"

    # Apply strip option to configure
    _optimized_switch="enable"
    [[ $(check_option strip) == n ]] && _optimized_switch="disable"

    # Include location of libffi headers in CPPFLAGS
    CPPFLAGS+=" $(pkg-config --cflags libffi)"

    # Force the use of GCC instead of clang
    CC=gcc CXX=g++ \
    ./configure \
        --prefix=/usr \
        --sysconfdir=/etc \
        --enable-shared \
        --enable-libffi \
        --enable-targets=all \
        --disable-expensive-checks \
        --disable-debug-runtime \
        --disable-assertions \
        --with-binutils-include=/usr/include \
        --with-python=/usr/bin/python2 \
        --$_optimized_switch-optimized

    make REQUIRES_RTTI=1
    make -C docs -f Makefile.sphinx man
    make -C docs -f Makefile.sphinx html
    make -C tools/clang/docs -f Makefile.sphinx html
}

package_llvm-pypy-stm() {
    pkgdesc="Low Level Virtual Machine, patched for pypy-stm"
    depends=("llvm-libs-pypy-stm" 'perl')
    provides=('llvm')
    conflicts=('llvm')

    cd "${srcdir}/${_pkgname}"

    # We move the clang directory out of the tree so it won't get installed and
    # then we bring it back in for the clang package
    mv tools/clang "${srcdir}/clang.src"

    # -j1 is due to race conditions during the installation of the OCaml bindings
    make -j1 DESTDIR="${pkgdir}" install
    mv "${srcdir}/clang.src" tools/clang

    # The runtime library goes into llvm-libs
    rm -rf "${srcdir}"/*.so
    mv "${pkgdir}"/usr/lib/libLLVM-*.so "${srcdir}/"

    # Fix permissions of static libs
    chmod -x "${pkgdir}"/usr/lib/*.a

    # Get rid of example Hello transformation
    rm -rf "${pkgdir}"/usr/lib/*LLVMHello.*

    # Symlink LLVMgold.so into /usr/lib/bfd-plugins
    # https://bugs.archlinux.org/task/28479
    install -m755 -d "${pkgdir}/usr/lib/bfd-plugins"
    ln -s ../LLVMgold.so "${pkgdir}/usr/lib/bfd-plugins/LLVMgold.so"

    if [[ $CARCH == x86_64 ]]; then
        # Needed for multilib (https://bugs.archlinux.org/task/29951)
        # Header stubs are taken from Fedora
        for _header in config llvm-config; do
            mv "${pkgdir}/usr/include/llvm/Config/${_header}"{,-64}.h
            cp "${srcdir}/llvm-Config-${_header}.h" \
                 "${pkgdir}/usr/include/llvm/Config/${_header}.h"
        done
    fi

    # Install man pages
    install -d "${pkgdir}/usr/share/man/man1"
    cp docs/_build/man/*.1 "${pkgdir}/usr/share/man/man1/"

    # Install html docs
    cp -r docs/_build/html/* "${pkgdir}/usr/share/doc/$_pkgname/html/"
    rm -r "${pkgdir}/usr/share/doc/${_pkgname}/html/_sources"

    install -Dm644 LICENSE.TXT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_llvm-libs-pypy-stm() {
    pkgdesc="Low Level Virtual Machine (runtime library), patched for pypy-stm"
    depends=('gcc-libs' 'zlib' 'libffi' 'ncurses')
    provides=('llvm-libs')
    conflicts=('llvm-libs')

    install -m755 -d "${pkgdir}"/usr/lib/

    mv "${srcdir}"/libLLVM-*.so "${pkgdir}/usr/lib/"

    for _shlib in "${pkgdir}"/usr/lib/*.so
    do
      test -L "${_shlib}" && ln -sf $(basename $(readlink ${_shlib})) ${_shlib}
    done

    install -Dm644 "${srcdir}/${_pkgname}/LICENSE.TXT" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_clang-pypy-stm() {
    pkgdesc="C language family frontend for LLVM, patched for pypy-stm"
    url="http://clang.llvm.org/"
    depends=("llvm-pypy-stm" 'gcc')
    provides=('clang')
    conflicts=('clang')

    sed -e 's:$(PROJ_prefix)/share/doc/llvm:$(PROJ_prefix)/share/doc/clang:' \
        -i "${srcdir}/${_pkgname}/Makefile.config"

    cd "${srcdir}/${_pkgname}/tools/clang"

    # We move the extra tools directory out of the tree so it won't get
    # installed and then we bring it back in for the clang-tools-extra package
    mv tools/extra "${srcdir}/"

    make DESTDIR="${pkgdir}" install
    mv "${srcdir}/extra" tools/

    # Fix permissions of static libs
    chmod -x "${pkgdir}"/usr/lib/*.a

    # Revert the path change in case we want to do a repackage later
    sed -e 's:$(PROJ_prefix)/share/doc/clang:$(PROJ_prefix)/share/doc/llvm:' \
        -i "${srcdir}/${_pkgname}/Makefile.config"

    # Install html docs
    cp -r docs/_build/html/* "${pkgdir}/usr/share/doc/clang/html/"
    rm -r "${pkgdir}/usr/share/doc/clang/html/_sources"

    # Install Python bindings
    install -m755 -d "${pkgdir}/usr/lib/python2.7/site-packages"
    cp -r bindings/python/clang "${pkgdir}/usr/lib/python2.7/site-packages/"
    python2 -m compileall "${pkgdir}/usr/lib/python2.7/site-packages/clang"
    python2 -O -m compileall "${pkgdir}/usr/lib/python2.7/site-packages/clang"

    # Install clang-format editor integration files (FS#38485)
    # Destination paths are copied from clang-format/CMakeLists.txt
    install -m755 -d "$pkgdir/usr/share/clang"
    (
    cd tools/clang-format
    cp clang-format-diff.py \
       clang-format-sublime.py \
       clang-format.el \
       clang-format.py \
       "${pkgdir}/usr/share/clang/"

      cp git-clang-format "${pkgdir}/usr/bin/"
      sed -e 's|/usr/bin/python$|&2|' \
          -i "${pkgdir}/usr/bin/git-clang-format" \
          -i "${pkgdir}/usr/share/clang/clang-format-diff.py"
    )

    install -Dm644 LICENSE.TXT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_clang-analyzer-pypy-stm() {
    pkgdesc="A source code analysis framework, patched for pypy-stm"
    url="http://clang-analyzer.llvm.org/"
    depends=("clang-pypy-stm" 'python2')
    provides=('clang-analyzer')
    conflicts=('clang-analyzer')

    cd "${srcdir}/${_pkgname}/tools/clang"

    install -m755 -d "${pkgdir}"/usr/{bin,lib/clang-analyzer}
    for _tool in scan-{build,view}; do
        cp -r tools/${_tool} "${pkgdir}/usr/lib/clang-analyzer/"
        ln -s /usr/lib/clang-analyzer/${_tool}/${_tool} "${pkgdir}/usr/bin/"
    done

    # scan-build looks for clang within the same directory
    ln -s /usr/bin/clang "${pkgdir}/usr/lib/clang-analyzer/scan-build/"

    # Relocate man page
    install -m755 -d "${pkgdir}/usr/share/man/man1"
    mv "${pkgdir}/usr/lib/clang-analyzer/scan-build/scan-build.1" \
       "${pkgdir}/usr/share/man/man1/"

    # Use Python 2
    sed -e 's|env python$|&2|' \
        -e 's|/usr/bin/python$|&2|' \
        -i "${pkgdir}/usr/lib/clang-analyzer/scan-view/scan-view" \
           "${pkgdir}/usr/lib/clang-analyzer/scan-build/set-xcode-analyzer"

    # Compile Python scripts
    python2 -m compileall "${pkgdir}/usr/lib/clang-analyzer"
    python2 -O -m compileall "${pkgdir}/usr/lib/clang-analyzer"

    install -Dm644 LICENSE.TXT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_clang-tools-extra-pypy-stm() {
    pkgdesc="Extra tools built using Clang's tooling APIs, patched for pypy-stm"
    url="http://clang.llvm.org/"
    depends=("clang-pypy-stm")
    provides=('clang-tools-extra')
    conflicts=('clang-tools-extra')

    cd "${srcdir}/${_pkgname}/tools/clang/tools/extra"

    make DESTDIR="${pkgdir}" install

    # Fix permissions of static libs
    chmod -x "${pkgdir}"/usr/lib/*.a

    install -Dm644 LICENSE.TXT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
