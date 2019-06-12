# Contributor: Andrew Rabert <ar@nullsum.net>

pkgname=scrcpy
pkgver=1.9
pkgrel=1
pkgdesc='Display and control your Android device'
arch=('i686' 'x86_64')
url='https://github.com/Genymobile/scrcpy'
license=('Apache')
depends=('ffmpeg' 'sdl2')
makedepends=('gcc' 'meson')
optdepends=('android-tools: required if adb is not already installed')
source=("https://github.com/Genymobile/scrcpy/archive/v${pkgver}.tar.gz"
        "https://github.com/Genymobile/scrcpy/releases/download/v${pkgver}/scrcpy-server-v${pkgver}.jar")
sha256sums=('905fe62e2825310eeb77187f8974763c3ae2f08ca1f649bcaf4721f1fd14a764'
            'ad7e539f100e48259b646f26982bc63e0a60a81ac87ae135e242855bef69bd1a')

src_name="scrcpy-${pkgver}"
src_server="scrcpy-server-v${pkgver}.jar"

build() {
    cd "${src_name}"

    rm -rf build
    meson build --buildtype release --strip -Db_lto=true \
        -Dprebuilt_server="../${src_server}"
    cd build
    ninja
}

package() {
    install -Dm 755 "${src_name}/build/app/scrcpy" "${pkgdir}/usr/share/scrcpy/scrcpy"
    install -Dm 644 "${src_server}" "${pkgdir}/usr/share/scrcpy/scrcpy-server.jar"
    mkdir -p "${pkgdir}/usr/bin"
    ln -s "/usr/share/scrcpy/scrcpy" "${pkgdir}/usr/bin/scrcpy"
}
