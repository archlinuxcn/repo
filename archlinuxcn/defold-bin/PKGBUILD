# Maintainer: Asakura Mizu <asakuramizu111@gmail.com>
_sha1=a9247e38b24ba1c1ed5913c4049d9a4083a314a7
_channel=editor-alpha
pkgname=defold-bin
pkgver=1.9.8.a9247e3
pkgrel=1
epoch=
pkgdesc='Defold is a completely free to use game engine for development of desktop, mobile and web games.'
arch=('x86_64')
url='https://defold.com/'
license=('custom')
groups=()
depends=('glu')
optdepends=()
provides=('defold')
conflicts=('defold')
replaces=('defold')
options=('!strip')
source=("${pkgname}-${pkgver}-${pkgrel}.tar.gz::https://d.defold.com/archive/${_channel}/${_sha1}/${_channel}/editor2/Defold-x86_64-linux.tar.gz"
        'https://github.com/defold/defold/raw/refs/heads/dev/LICENSE.txt'
        'Defold.desktop')
sha256sums=('1c29973cbfd395635305a3f9c752f83419577dbc6fc32ebdb2fcdeb49c3935e3'
            'be6e9921ba01445d200ba3dc09b5cab149a58d57a76ca98376b52af87d817a7a'
            '5c92dc2b1cf4acc81f26b6848c3bb3ee812158e80a15fb1e7f5585362acb20f2')

package() {
    cd "$srcdir"

    bsdtar -xf Defold/packages/defold-${_sha1}.jar --strip-components 2 icons/document.iconset

    install -Dm644 LICENSE.txt -t "$pkgdir/usr/share/licenses/$pkgname"
    install -Dm644 Defold.desktop -t "$pkgdir/usr/share/applications"
    install -Dm644 icon_16x16.png "$pkgdir/usr/share/icons/hicolor/16x16/apps/defold.png"
    install -Dm644 icon_16x16@2x.png "$pkgdir/usr/share/icons/hicolor/32x32/apps/defold.png"
    install -Dm644 icon_32x32@2x.png "$pkgdir/usr/share/icons/hicolor/64x64/apps/defold.png"
    install -Dm644 icon_128x128.png "$pkgdir/usr/share/icons/hicolor/128x128/apps/defold.png"
    install -Dm644 icon_256x256.png "$pkgdir/usr/share/icons/hicolor/256x256/apps/defold.png"
    install -Dm644 icon_256x256@2x.png "$pkgdir/usr/share/icons/hicolor/512x512/apps/defold.png"

    mkdir -p "$pkgdir/opt"
    cp -r Defold "$pkgdir/opt"
}
