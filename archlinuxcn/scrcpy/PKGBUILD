# Contributor: Andrew Rabert <ar@nullsum.net>

pkgname=scrcpy
pkgver=1.16
pkgrel=1
pkgdesc='Display and control your Android device'
arch=('i686' 'x86_64')
url='https://github.com/Genymobile/scrcpy'
license=('Apache')
depends=('android-tools' 'ffmpeg' 'sdl2')
makedepends=('meson')
source=("https://github.com/Genymobile/scrcpy/archive/v${pkgver}.tar.gz"
        "https://github.com/Genymobile/scrcpy/releases/download/v${pkgver}/scrcpy-server-v${pkgver}")
sha256sums=('94cbd59e26faa08ca25d5126d6c8d45e831b6a9e716ce05cd57bc4bcc751f742'
            '94a79e05b4498d0460ab7bd9d12cbf05156e3a47bf0c5d1420cee1d4493b3832')

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
