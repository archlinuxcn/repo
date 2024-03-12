# Maintainer: RealStickman <mrc+aur@frm01.net>

pkgname=feishin-bin
pkgdesc='Rewrite of Sonixd'
pkgver=0.6.0
pkgrel=1
arch=('x86_64' 'aarch64')
url='https://github.com/jeffvli/feishin'
license=('GPL3')
depends=('mpv') # TODO check node requirements
provides=("${pkgname%-bin}")
conflicts=("${pkgname%-bin}")
_filename=Feishin-${pkgver//_/-}-linux
source=("feishin.desktop")
source_x86_64=("https://github.com/jeffvli/feishin/releases/download/v${pkgver//_/-}/${_filename}-x64.tar.xz")
source_aarch64=("https://github.com/jeffvli/feishin/releases/download/v${pkgver//_/-}/${_filename}-arm64.tar.xz")
sha256sums=('ef112b1a9ef80d8bf27f721fdbb12de0a195da4e464dbf27282503ba398bef8d')
sha256sums_x86_64=('1c2266798e94e66340f54e985ecc924a5be7646c4859562c837fa5e16d3ce408')
sha256sums_aarch64=('63bf90f924e83d21919a454fa39734df94e2db33c15036ab4fbefd7a8b45ce1a')

package() {
    # create target file structure
    mkdir -p "$pkgdir/usr/bin"
    mkdir -p "$pkgdir/usr/share/"{feishin,pixmaps,applications}
    # HACK rename package correctly
    if [ $CARCH == "x86_64" ]; then
        mv ${_filename}-x64.tar.xz ${_filename}-$CARCH.tar.xz
    elif [ $CARCH == "aarch64" ]; then
        mv ${_filename}-arm64.tar.xz ${_filename}-$CARCH.tar.xz
    fi
    # extract files to target
    tar -xf ${_filename}-$CARCH.tar.xz -C "$pkgdir/usr/share/feishin" --strip-components=1
    # install icon
    install -Dm644 "$pkgdir/usr/share/feishin/resources/assets/icons/icon.png" "$pkgdir/usr/share/pixmaps/${pkgname%-bin}.png"
    # symlink executable to "/usr/bin/feishin"
    ln -s /usr/share/feishin/feishin "${pkgdir}/usr/bin/feishin"
    # install desktop entry
    install -Dm644 feishin.desktop "$pkgdir/usr/share/applications/"
}
