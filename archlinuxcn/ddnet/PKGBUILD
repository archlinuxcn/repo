# Maintainer: Rafael Fontenelle <rafaelff@gnome.org>
# Maintainer: Edgar Luque <git@edgarluque.com>

pkgname=ddnet
pkgver=15.5.1
pkgrel=1
pkgdesc="A Teeworlds modification with a unique cooperative gameplay."
arch=('x86_64')
url="https://ddnet.tw"
license=('custom:BSD' 'CCPL:by-nc-sa')
depends=('freetype2' 'opusfile' 'curl' 'glew' 'wavpack' 'pnglite' 'ffmpeg' 'libnotify' 'miniupnpc' 'sqlite' 'mariadb-libs')
makedepends=('cmake' 'ninja' 'python')
checkdepends=('gmock')
optdepends=('ddnet-skins: A collection with more than 500 custom tee skins.'
            'ddnet-maps-git: All the maps used on the official DDNet Servers.')
backup=('usr/share/ddnet/data/autoexec_server.cfg')
source=("https://ddnet.tw/downloads/DDNet-$pkgver.tar.xz"
        "ddnet-server.service" "ddnet-sysusers.conf" "ddnet-tmpfiles.conf")
sha256sums=('455ffe30b05a497e552e5d0de05a45e503d185b90d808431e4f53a1c1bb280e7'
            '9377a9d7c87abae166c8fa98cd79a61c74482f80f80bc930ae043349e9a84965'
            '70034f237270b38bf312238a26cfd322e212ca5714bfea4ae91e80c639ce8738'
            '043452f4de3c86d903973009bb3e59b3492a6669b86d0b1410e59a1476a87369')

build() {
    mkdir -p build
    cd build
    cmake ../DDNet-$pkgver          \
        -DCMAKE_BUILD_TYPE=Release  \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DAUTOUPDATE=OFF            \
        -DANTIBOT=ON                \
        -DVIDEORECORDER=ON          \
        -DUPNP=ON                   \
        -DMYSQL=ON                  \
        -GNinja
    ninja
}

check() {
    ninja run_tests -C build
}

package() {
    DESTDIR="$pkgdir" ninja install -C build
    install -vDm644 DDNet-$pkgver/license.txt      "$pkgdir/usr/share/licenses/$pkgname/license.txt"
    install -vDm644 "$srcdir/ddnet-server.service" "$pkgdir/usr/lib/systemd/system/ddnet-server.service"
    install -vDm644 "$srcdir/ddnet-sysusers.conf"  "$pkgdir/usr/lib/sysusers.d/ddnet.conf"
    install -vDm644 "$srcdir/ddnet-tmpfiles.conf"  "$pkgdir/usr/lib/tmpfiles.d/ddnet.conf"
    sed -i "$pkgdir/usr/share/ddnet/data/autoexec_server.cfg" \
        -e '/sv_test_cmds/s/1/0/' \
        -e 's/myServerconfig.cfg/autoexec_server_maps.cfg/'
}
