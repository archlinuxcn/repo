# Maintainer: exu <aur _a_ frm01 _d_ net>

pkgname=feishin-bin
pkgdesc='Rewrite of Sonixd'
pkgver=0.7.1
pkgrel=2
arch=('x86_64' 'aarch64')
url='https://github.com/jeffvli/feishin'
license=('GPL3')
optdepends=('mpv: Alternative audio backend')
provides=("${pkgname%-bin}")
conflicts=("${pkgname%-bin}")
_filename=Feishin-${pkgver//_/-}-linux
source=("feishin.desktop")
source_x86_64=("https://github.com/jeffvli/feishin/releases/download/v${pkgver//_/-}/${_filename}-x64.tar.xz")
source_aarch64=("https://github.com/jeffvli/feishin/releases/download/v${pkgver//_/-}/${_filename}-arm64.tar.xz")
sha256sums=('ef112b1a9ef80d8bf27f721fdbb12de0a195da4e464dbf27282503ba398bef8d')
sha256sums_x86_64=('e5274bc638bede1060c4555f0076f7ca131ca3e032c88a61403f246e85f0c7d7')
sha256sums_aarch64=('f0ac75d8a5f5ad3074ed62d58da6e0cdd45e4a50312b58f3dcd7ab2bbf7ac6df')

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
