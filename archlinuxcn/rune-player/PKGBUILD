# Maintainer: Roald Clark <roaldclark@gmail.com>

_name=rune
pkgname=rune-player
pkgver=1.1.0
pkgrel=1
pkgdesc="The player that blends classic design with modern technology"
arch=('x86_64')
url="https://github.com/Losses/${_name}"
license=('MPL-2.0')
depends=(
    'alsa-lib'
    'at-spi2-core'
    'ayatana-ido'
    'cairo'
    'dbus'
    'fontconfig'
    'gcc-libs'
    'gdk-pixbuf2'
    'glib2'
    'glibc'
    'gtk3'
    'harfbuzz'
    'hicolor-icon-theme'
    'libayatana-appindicator'
    'libayatana-indicator'
    'libdbusmenu-glib'
    'libepoxy'
    'libnotify'
    'openssl'
    'pango'
    'zlib'
)
makedepends=(
    'patchelf'
    'protobuf'
    'protoc-gen-dart'
    'protoc-gen-prost'
    'rustup'
)
makedepends+=(
    'clang'
    'cmake'
    'fvm'
    'ninja'
)
conflicts=("${pkgname}-git")
options=(!lto)
source=(
    "${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
    "${_name}.desktop"
)
sha256sums=('c6c6a288b70338b4ba2c11ad6cf7c84ec42d97ecb8b63796111de3fa2b20f88c'
            '8c680492966831e2da2968007f2d5d3dbfbf72fdab670592689ac42f37af2121')

prepare() {
    cd "${srcdir}/${_name}-${pkgver}"

    export FVM_CACHE_PATH="${SRCDEST}/fvm-cache"

    sed -i '$a\' .gitignore
    echo ".fvm/" >> .gitignore

    fvm install stable
    fvm use stable

    fvm flutter --no-version-check config --no-analytics
    fvm flutter --no-version-check pub get
}

build() {
    cd "${srcdir}/${_name}-${pkgver}"

    export LDFLAGS="${LDFLAGS} -Wl,--no-as-needed"
    export FVM_CACHE_PATH="${SRCDEST}/fvm-cache"
    export RUSTUP_TOOLCHAIN=stable
    export CARGO_TARGET_DIR=target

    fvm flutter --no-version-check pub run rinf message
    fvm flutter --no-version-check build linux --no-pub --release --verbose
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"

    install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"

    pushd assets/icons
    find ./breeze ./gnome -type f -exec install -v -Dm644 {} ${pkgdir}/usr/share/icons/{} \;
    cd Papirus
    find . -type f -exec install -v -Dm644 {} ${pkgdir}/usr/share/icons/hicolor/{} \;
    popd
    ln -sfrv ${pkgdir}/usr/share/icons/breeze/apps/1024/${_name}.png ${pkgdir}/usr/share/icons/${_name}.png

    cd build/linux/x64/release/bundle
    install -Dm755 ${_name} -t "${pkgdir}/usr/lib/${pkgname}/"
    pushd lib
    find . -type f -exec install -v -Dm644 {} ${pkgdir}/usr/lib/${pkgname}/lib/{} \;
    popd
    pushd data
    find . -type f -exec install -v -Dm644 {} ${pkgdir}/usr/lib/${pkgname}/data/{} \;
    popd
    install -dm755 "${pkgdir}/usr/bin"
    ln -sfrv "${pkgdir}/usr/lib/${pkgname}/${_name}" "${pkgdir}/usr/bin/${_name}"

    # Fix rpath that causes 'Insecure RUNPATH'
    for shared_lib in "${pkgdir}/usr/lib/${pkgname}/lib"/*.so; do
        [[ -z $(patchelf --print-rpath "${shared_lib}") ]] && continue
        [[ $(patchelf --print-rpath "${shared_lib}") == '$ORIGIN' ]] && continue
        patchelf --set-rpath '$ORIGIN' "${shared_lib}"
    done

    install -Dm644 "${srcdir}/${_name}.desktop" -t "${pkgdir}/usr/share/applications/"
}
