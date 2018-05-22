# Maintainer: Rafael Fontenelle <rafaelff@gnome.org>

pkgname=ddnet
pkgver=11.1.8
pkgrel=1
pkgdesc="DDraceNetwork, a mod of Teeworlds"
arch=('x86_64')
url="https://ddnet.tw"
license=('custom:BSD' 'CCPL:by-nc-sa')
depends=('alsa-lib' 'sdl2' 'freetype2' 'opusfile' 'curl' 'glew' 'wavpack')
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
sha256sums=('f8116f074d19fbd953ebd8fa204c63d5665a20120a6c71f81e793fb78e1243c2'
            'fc8c27e129f92c5dddf96a079306a2439c8cc14d4b8ce719c5fa2f59aceee367'
            'fc8c27e129f92c5dddf96a079306a2439c8cc14d4b8ce719c5fa2f59aceee367'
            '1dc83efd9fdab2597fc4d41358628422a9550d4d23b60d273f2f30cf7b76dfaa'
            'e4083f1c40569146caabd21b8f24fdd7862e2f3040552e9c6a260df603249274')

build() {
    [ -d build ] && rm -rf build
    mkdir build

    cd build
    cmake ../DDNet-$pkgver -DCMAKE_BUILD_TYPE=Release
    make all tools
}

check() {
    cd build
    make -k run_tests
}

package() {
    cd build

      # Install DDNet client/server binaries
    install -d -m755 "$pkgdir/usr/bin"
    install -m755 DDNet                "$pkgdir/usr/bin/"
    install -m755 DDNet-Server         "$pkgdir/usr/bin/"

      # Install extra tools
    install -d -m755 "$pkgdir/usr/share/ddnet/tools/"
    install -m755 config_retrieve      "$pkgdir/usr/share/ddnet/tools/"
    install -m755 config_store         "$pkgdir/usr/share/ddnet/tools/"
    install -m755 confusables          "$pkgdir/usr/share/ddnet/tools/"
    install -m755 crapnet              "$pkgdir/usr/share/ddnet/tools/"
    install -m755 dilate               "$pkgdir/usr/share/ddnet/tools/"
    install -m755 dummy_map            "$pkgdir/usr/share/ddnet/tools/"
    install -m755 fake_server          "$pkgdir/usr/share/ddnet/tools/"
    install -m755 map_diff             "$pkgdir/usr/share/ddnet/tools/"
    install -m755 map_extract          "$pkgdir/usr/share/ddnet/tools/"
    install -m755 map_replace_image    "$pkgdir/usr/share/ddnet/tools/"
    install -m755 map_resave           "$pkgdir/usr/share/ddnet/tools/"
    install -m755 map_version          "$pkgdir/usr/share/ddnet/tools/"
    install -m755 packetgen            "$pkgdir/usr/share/ddnet/tools/"
    install -m755 tileset_borderadd    "$pkgdir/usr/share/ddnet/tools/"
    install -m755 tileset_borderfix    "$pkgdir/usr/share/ddnet/tools/"
    install -m755 tileset_borderrem    "$pkgdir/usr/share/ddnet/tools/"
    install -m755 tileset_borderset    "$pkgdir/usr/share/ddnet/tools/"
    install -m755 uuid                 "$pkgdir/usr/share/ddnet/tools/"

      # Install data files
    install -d -m755 "$pkgdir/usr/share/ddnet/data/"
    cp -r data/* "$pkgdir/usr/share/ddnet/data/"
    rm -rf "$pkgdir/usr/share/ddnet/data/languages/scripts/"

      # Install desktop and icon files
    install -d -m755 "$pkgdir/usr/share/applications/"
    install -d -m755 "$pkgdir/usr/share/pixmaps/"
    install -m644 "$srcdir/ddnet.desktop"        "$pkgdir/usr/share/applications/"
    install -m644 "$srcdir/ddnet-server.desktop" "$pkgdir/usr/share/applications/"
    install -m644 "$srcdir/DDNet.png"            "$pkgdir/usr/share/pixmaps/"
    install -m644 "$srcdir/DDNet-Server.png"     "$pkgdir/usr/share/pixmaps/"

      # Install license files
    install -Dm644 ../DDNet-$pkgver/license.txt "$pkgdir/usr/share/licenses/$pkgname/license.txt"
}
