# Contributor: Andrew Rabert <ar@nullsum.net>

pkgname=scrcpy
pkgver=1.12
pkgrel=2
pkgdesc='Display and control your Android device'
arch=('i686' 'x86_64')
url='https://github.com/Genymobile/scrcpy'
license=('Apache')
depends=('android-tools' 'ffmpeg' 'sdl2')
makedepends=('meson')
optdepends=('android-tools: required if adb is not already installed')
source=("https://github.com/Genymobile/scrcpy/archive/v${pkgver}.tar.gz"
        "https://github.com/Genymobile/scrcpy/releases/download/v${pkgver}/scrcpy-server-v${pkgver}")
sha256sums=('95aab189448582870d8e7d8a27a2c9b40838bd45ee2737be0f255f7a11647870'
            'b6595262c230e9773fdb817257abcc8c6e6e00f15b1c32b6a850ccfd8176dc10')

prepare() {
    cd "${pkgname}-${pkgver}"
    rm -rf build
}

build() {
    cd "${pkgname}-${pkgver}"
    meson \
        --prefix /usr \
        --buildtype release \
        --strip \
        -Db_lto=true \
        -Dprebuilt_server="../scrcpy-server-v${pkgver}" \
        build
    ninja -C build
}

package() {
    cd "${pkgname}-${pkgver}"
    DESTDIR="${pkgdir}" ninja -C build install
    install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
