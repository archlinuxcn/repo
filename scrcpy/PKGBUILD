# Contributor: Andrew Rabert <draje@nullsum.net>

pkgname=scrcpy
pkgver=1.5
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
sha256sums=('9eef28d352d064320b8a2b9cc1000d478fb617a99807f2456a54af855b39ecf9'
            'c827f566172a5c5946e63b8378ac93d374dff9e229083e5cd9980df57536947b')

src_name="scrcpy-${pkgver}"
src_server="scrcpy-server-v${pkgver}.jar"

server_path='/usr/share/scrcpy/scrcpy-server.jar'

build() {
    cd "${src_name}"

    rm -rf build
    meson build --buildtype release --strip -Db_lto=true \
        -Dbuild_server=false \
        -Doverride_server_path="${server_path}"
    cd build
    ninja
}

package() {
    install -Dm 755 "${src_name}"/build/app/scrcpy "${pkgdir}"/usr/bin/scrcpy
    install -Dm 644 "${src_server}"                "${pkgdir}"/"${server_path}"
}
