# Contributor: Andrew Rabert <draje@nullsum.net>

pkgname=scrcpy
pkgver=1.5
pkgrel=3
pkgdesc='Display and control your Android device'
arch=('i686' 'x86_64')
url='https://github.com/Genymobile/scrcpy'
license=('Apache')
depends=('ffmpeg' 'sdl2')
makedepends=('gcc' 'meson')
optdepends=('android-tools: required if adb is not already installed')
source=("https://github.com/Genymobile/scrcpy/archive/v${pkgver}-fixversion.tar.gz"
        "https://github.com/Genymobile/scrcpy/releases/download/v${pkgver}-fixversion/scrcpy-server-v${pkgver}.jar")
sha256sums=('79249fb0881c8de6af23ed58e2b31dc6738174d7e49c490ae6e7992f7b3ec2cd'
            'd97aab6f60294e33e7ff79c2856ad3e01f912892395131f4f337e9ece03c24de')

src_name="scrcpy-${pkgver}-fixversion"
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
