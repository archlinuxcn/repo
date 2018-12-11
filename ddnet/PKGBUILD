# Maintainer: Rafael Fontenelle <rafaelff@gnome.org>

pkgname=ddnet
pkgver=11.5.1
pkgrel=1
pkgdesc="DDraceNetwork, a mod of Teeworlds"
arch=('x86_64')
url="https://ddnet.tw"
license=('custom:BSD' 'CCPL:by-nc-sa')
depends=('sdl2' 'freetype2' 'opusfile' 'curl' 'glew' 'wavpack')
makedepends=('cmake' 'python')
checkdepends=('gtest')
optdepends=('ddnet-skins: more skins for your tee'
            'ddnet-maps-git: have all DDNet maps available offline')
provides=('teeworlds-ddnet')
conflicts=('teeworlds-ddnet')
replaces=('teeworlds-ddnet')
source=("https://ddnet.tw/downloads/DDNet-$pkgver.tar.xz"
        'ddnet.desktop' 'ddnet-server.desktop'
        'DDNet.png' 'DDNet-Server.png')
sha256sums=('df789b045d4ff3c6375a9b62ce0828b556fe5f44dba5951fd278125291bf4f7e'
            'c60de83f47b5981e79dc0d028c1fe239c898f6319653b94bb74e578cf699a216'
            'fc8c27e129f92c5dddf96a079306a2439c8cc14d4b8ce719c5fa2f59aceee367'
            '1dc83efd9fdab2597fc4d41358628422a9550d4d23b60d273f2f30cf7b76dfaa'
            'e4083f1c40569146caabd21b8f24fdd7862e2f3040552e9c6a260df603249274')

build() {
    [ -d build ] && rm -rf build
    mkdir build

    cd build
    cmake ../DDNet-$pkgver        \
      -DCMAKE_BUILD_TYPE=Release  \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DAUTOUPDATE=OFF
    make all tools
}

check() {
    make -k run_tests -C build
}

package() {
    make install DESTDIR="$pkgdir" -C build

      # Install desktop and icon files
    install -d -m755 "$pkgdir/usr/share/applications/"
    install -d -m755 "$pkgdir/usr/share/pixmaps/"
    install -m644 ddnet.desktop        "$pkgdir/usr/share/applications/"
    install -m644 ddnet-server.desktop "$pkgdir/usr/share/applications/"
    install -m644 DDNet.png            "$pkgdir/usr/share/pixmaps/"
    install -m644 DDNet-Server.png     "$pkgdir/usr/share/pixmaps/"

      # Install license files
    install -d -m755 "$pkgdir/usr/share/licenses/$pkgname/"
    install -Dm644 DDNet-$pkgver/license.txt  "$pkgdir/usr/share/licenses/$pkgname/"
}
