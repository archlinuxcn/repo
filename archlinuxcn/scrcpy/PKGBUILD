# Contributor: Andrew Rabert <ar@nullsum.net>

pkgname=scrcpy
pkgver=1.19
pkgrel=1
pkgdesc='Display and control your Android device'
arch=('i686' 'x86_64')
url='https://github.com/Genymobile/scrcpy'
license=('Apache')
depends=('android-tools' 'ffmpeg' 'sdl2')
makedepends=('meson')
source=("https://github.com/Genymobile/scrcpy/archive/v${pkgver}.tar.gz"
        "https://github.com/Genymobile/scrcpy/releases/download/v${pkgver}/scrcpy-server-v${pkgver}")
sha256sums=('40ac2059618f18a0e6f9cd0e40d3bff240ade98664bd619422f875bff7e8c70e'
            '876f9322182e6aac6a58db1334f4225855ef3a17eaebc80aab6601d9d1ecb867')

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
