# Maintainer: Rafael Fontenelle <rafaelff@gnome.org>

pkgname=ddnet
pkgver=11.0.1
pkgrel=1
pkgdesc="DDraceNetwork, a mod of Teeworlds"
arch=('x86_64')
url="https://ddnet.tw"
license=('custom:BSD' 'cc-by-nc-sa-3.0')
depends=('alsa-lib' 'glu' 'sdl2' 'freetype2' 'opusfile' 'curl') #mariadb
makedepends=('cmake' 'imagemagick' 'gendesk' 'python' 'gtest')
optdepends=('ddnet-skins: more skins for your tee'
            'ddnet-maps-git: mainly important for a DDNet Server')
provides=('teeworlds-ddnet')
conflicts=('teeworlds-ddnet')
replaces=('teeworlds-ddnet')
source=("https://ddnet.tw/downloads/DDNet-$pkgver.tar.xz")
sha256sums=('d7a3419dc1bb8c9580c19d3ad627fe77071e31f7e84f8c8728e1e46ed7a15a61')

prepare() {
    [ -d build ] && rm -rf build
    mkdir build
    cd build

      # Client
    convert "../DDNet-$pkgver/other/icons/DDNet.ico" DDNet.png
    gendesk -f -n --pkgname "DDNet" --pkgdesc "$pkgdesc" \
        --name 'DDNet' --categories 'Game;ArcadeGame'

      # Server
      # Requires 'ddnet-maps-git' package for using DDNet maps
      # Requires a mysql-like database package for score/ranking
    convert "../DDNet-$pkgver/other/icons/DDNet-Server.ico" DDNet-Server.png
    gendesk -f -n --pkgname "DDNet-Server" --pkgdesc "DDNet Server"        \
        --name 'DDNet Server' --categories 'Game;ArcadeGame' --terminal=true \
        --exec='sh -c "cd /usr/share/ddnet/data && DDNet-Server"'
}

build() {
    cd build
    cmake ../DDNet-$pkgver -DCMAKE_BUILD_TYPE=Release #-DMYSQL=ON
    make all tools
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
    install -Dm644 DDNet.desktop        "$pkgdir/usr/share/applications/ddnet.desktop"
    install -Dm644 DDNet-Server.desktop "$pkgdir/usr/share/applications/ddnet-server.desktop"
    install -Dm644 DDNet-5.png          "$pkgdir/usr/share/pixmaps/DDNet.png"
    install -Dm644 DDNet-Server-8.png   "$pkgdir/usr/share/pixmaps/DDNet-Server.png"

      # Install license files
    install -Dm644 ../DDNet-$pkgver/license.txt "$pkgdir/usr/share/licenses/$pkgname/license.txt"
}
