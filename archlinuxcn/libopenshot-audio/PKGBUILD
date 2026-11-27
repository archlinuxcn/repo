# Maintainer: Mahdi Sarikhani <mahdisarikhani@outlook.com>
# Contributor: Andréas Caumeil <andreas.caumeil@proton.me>
# Contributor: Rafael Dominiquini <rafaeldominiquini at gmail dot com>
# Contributor: Caleb Maclennan <caleb@alerque.com>
# Contributor: David Runge <dvzrv@archlinux.org>
# Contributor: Martin Wimpress <code@flexion.org>
# Contributor: Foster McLane <fkmclane@gmail.com>
# Contributor: Jonathan Thomas <jonathan@openshot.org>

pkgbase=libopenshot-audio
pkgname=(libopenshot-audio libopenshot-audio-docs)
pkgver=1.0.2
pkgrel=1
pkgdesc="A high-quality audio editing and playback library used by libopenshot"
arch=('x86_64')
url="https://github.com/OpenShot/libopenshot-audio"
license=('GPL-3.0-or-later')
makedepends=('alsa-lib' 'cmake' 'doxygen' 'zlib')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('1391bcbcf35afbb815e823e6e2df941ef94427beb4cca3b7e5c5dadf75c582728fe0dbb71f0058c0e46360357222562d9fcfc31b376b4799a483116dbec0b73e')
b2sums=('d457e0f9eb415dc45d72ff19b1e8928430c90fc56e4f1476b0e87dd7c90cec9b004764c398749bb1748f33d8275bdf1858fc598fe3ff56cb15f1dc08157cfd93')

_pick() {
    local p="$1" f d
    shift
    for f; do
        d="${srcdir}/${p}/${f#${pkgdir}/}"
        mkdir -p "$(dirname "${d}")"
        mv "${f}" "${d}"
        rmdir -p --ignore-fail-on-non-empty "$(dirname "${f}")"
    done
}

build() {
    local cmake_options=(
        -B build
        -S "${pkgname}-${pkgver}"
        -D CMAKE_BUILD_TYPE=None
        -D CMAKE_INSTALL_PREFIX=/usr
    )
    cmake "${cmake_options[@]}"
    cmake --build build
}

check() {
    ctest --test-dir build --output-on-failure
}

package_libopenshot-audio() {
    depends=('alsa-lib' 'glibc' 'libgcc' 'libstdc++' 'zlib')
    optdepends=('libopenshot-audio-docs: for documentation')
    provides=('libopenshot-audio.so')

    DESTDIR="${pkgdir}" cmake --install build

    cd "${pkgdir}"
    _pick docs usr/share/doc
}

package_libopenshot-audio-docs() {
    pkgdesc+=" (documentation)"

    mv -v docs/* "${pkgdir}"
}
