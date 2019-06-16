# Maintainer: Rafael Fontenelle <rafaelff@gnome.org>
# Maintainer: Ryozuki <ryo@ryozuki.xyz>

pkgname=ddnet
pkgver=12.5
pkgrel=2
pkgdesc="A Teeworlds modification with a unique cooperative gameplay."
arch=('x86_64')
url="https://ddnet.tw"
license=('custom:BSD' 'CCPL:by-nc-sa')
depends=('sdl2' 'freetype2' 'opusfile' 'curl' 'glew' 'wavpack' 'libwebsockets' 'pnglite')
makedepends=('cmake' 'ninja' 'python' 'imagemagick' 'gendesk')
checkdepends=('gtest')
optdepends=('ddnet-skins: A collection with more than 700 custom tee skins.'
            'ddnet-maps-git: All the maps used on the official DDNet Servers.')
source=("https://ddnet.tw/downloads/DDNet-$pkgver.tar.xz")
sha256sums=('d407c024e082142d26198370b7b53f9e09cb3ba9d291272c8717d2c98d750874')

# Set 1 to enable MySQL support and add dependencies
_enable_mysql=0

if [ $_enable_mysql -eq 1 ]; then
    depends+=('mysql-connector-c++')
    makedepends+=('boost')
    _mysql_opt="-DMYSQL=ON"
fi

prepare() {
    [ -d build ] && rm -rf build; mkdir build
    [ -d prep ]  && rm -rf prep;  mkdir prep
    cd prep

      # Extract icons in .png from .ico (name must be lowercase)
    convert ../DDNet-$pkgver/other/icons/DDNet-Server.ico ddnet-server.png

      # Generate the server .desktop file
    gendesk --pkgname="DDNet-Server" --name="DDNet Server"          \
            --pkgdesc="DDNet Server" --terminal=true                \
            --icon="ddnet-server"    --categories="Game;ArcadeGame" \
            --exec='sh -c "cd /usr/share/ddnet/data && DDNet-Server"'

      # Create icon files' structure, for installing in package(). How:
      # For each png file, check its dimensions (e.g. 128 x 128) using
      # the output of 'file' command. Then double-check the 's' as a
      # number, then install it into  a "size/filename.png" notation
    for f in ddnet-server-?.png; do
        s=$(file $f | cut -d' ' -f5)
        if [ ! -z "${s##*[!0-9]*}" ]; then
            install -Dm644 $f ${s}x${s}/apps/${f/-[0-9]/}
            rm $f
        fi
    done
}

build() {
    cd build
    cmake ../DDNet-$pkgver          \
        -DCMAKE_BUILD_TYPE=Release  \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DWEBSOCKETS=ON             \
        -DAUTOUPDATE=OFF            \
        -GNinja                     \
        $_mysql_opt
    ninja
}

check() {
    ninja run_tests -C build
}

package() {
    DESTDIR="$pkgdir" ninja install -C build

      # Install desktop files and folder
    install -dvm755 "$pkgdir/usr/share/applications/"
    install -vm644 prep/DDNet-Server.desktop "$pkgdir/usr/share/applications/"

      # Install icon files and folders
    for f in $(find prep -type f -name '*.png'); do
        install -Dvm644 $f "$pkgdir/usr/share/icons/hicolor"/${f/prep\/}
    done

      # Install license file
    install -dm755 "$pkgdir/usr/share/licenses/$pkgname/"
    install -vm644 DDNet-$pkgver/license.txt  "$pkgdir/usr/share/licenses/$pkgname/"
}
