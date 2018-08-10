# Contributor: Andrew Rabert <draje@nullsum.net>

pkgname=scrcpy
pkgver=1.3
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
sha256sums=('e0e157341f6c052dc2e50ee6e912cf94df0bdda039759f19abb1eece37345f75'
            '0f9a5a217f33f0ed7a1498ceb3c0cccf31c53533893aa952e674c1571d2740c1')

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
