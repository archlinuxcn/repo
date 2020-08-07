# Contributor: Andrew Rabert <ar@nullsum.net>

pkgname=scrcpy
pkgver=1.15
pkgrel=1
pkgdesc='Display and control your Android device'
arch=('i686' 'x86_64')
url='https://github.com/Genymobile/scrcpy'
license=('Apache')
depends=('android-tools' 'ffmpeg' 'sdl2')
makedepends=('meson')
source=("https://github.com/Genymobile/scrcpy/archive/v${pkgver}.tar.gz"
        "https://github.com/Genymobile/scrcpy/releases/download/v${pkgver}/scrcpy-server-v${pkgver}")
sha256sums=('f229ba0b8fca184ab0063ee214e56a2a651d665d4a1c7ac941e111190852c555'
            'e160c46784f30566eae621cad88bfb34e124f945cb8274b8dfc615b613b86dd8')

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
