# Maintainer: Tilman BLUMENBACH <tilman+aur AT ax86 DOT net>

pkgname=(barrier barrier-headless)
pkgver=2.3.2
pkgrel=1
pkgdesc="Open-source KVM software based on Synergy"
url="https://github.com/debauchee/barrier"
license=("custom:GPL2WithOpenSSLException")
changelog=CHANGELOG.rst
source=(
    "https://github.com/debauchee/barrier/archive/v${pkgver?}.tar.gz"
)
arch=(x86_64)
depends=(
    # Barrier core dependencies:
    curl
    avahi
    libx11
    libxrandr
    libxext
    libxinerama
    xorgproto
    libxtst
    libxi
    libsm
    libice
    openssl
)
makedepends=(
    cmake

    # Barrier GUI dependencies:
    qt5-base
    hicolor-icon-theme
)

prepare() {
    cd "barrier-${pkgver?}"

    for patch in "${srcdir?}"/*.patch; do
        if [ -f "${patch?}" ]; then
            patch -Np1 -i "${patch?}"
        fi
    done
}

build() {
    cd "barrier-${pkgver?}"

    mkdir -p build
    cd build

    cmake -G "Unix Makefiles" \
        -D CMAKE_BUILD_TYPE:STRING=Release \
        -D CMAKE_INSTALL_PREFIX:STRING=/usr \
        -D BARRIER_REVISION:STRING=00000000 \
        -D BARRIER_VERSION_STAGE:STRING=RELEASE \
        ..
    make
}

_package_common() {
    # Install binaries:
    cd "barrier-${pkgver?}/build"
    DESTDIR="${pkgdir?}" make install

    # Install the license:
    cd ..
    install -m 644 -D LICENSE "${pkgdir?}/usr/share/licenses/${pkgname?}/LICENSE"

    # Install the manpages:
    mkdir -p "${pkgdir?}/usr/share/man/man1"
    install -m 644 doc/*.1 "${pkgdir?}/usr/share/man/man1"

    # Install the examples:
    mkdir -p "${pkgdir?}/usr/share/doc/${pkgname?}"
    install -m 644 doc/barrier.conf* "${pkgdir?}/usr/share/doc/${pkgname?}"
}

package_barrier() {
    pkgdesc="Open-source KVM software based on Synergy (GUI)"
    depends=(
        "barrier-headless=${pkgver?}-${pkgrel?}"
        qt5-base
        hicolor-icon-theme
    )

    # Install all the files:
    _package_common

    # Now go and delete files that are already in
    # barrier-headless:
    for file in \
        /usr/share/doc \
        /usr/share/man \
        /usr/bin/barrier{s,c} \
    ;do
        rm -rf "${pkgdir:?}/${file:?}"
    done
}

package_barrier-headless() {
    pkgdesc="Open-source KVM software based on Synergy (client and server CLI binaries)"

    # Install all the files:
    _package_common

    # Now go and delete the GUI-related files:
    for file in \
        /usr/bin/barrier \
        /usr/share/applications \
        /usr/share/icons \
    ;do
        rm -rf "${pkgdir:?}/${file:?}"
    done
}

sha256sums=('6b92a70c5f4d625065842d133386982ec2ad1db2a809af47e46ab8ce2acd39b5')
