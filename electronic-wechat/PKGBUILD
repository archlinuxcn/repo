# Contributor: wenLiangcan <boxeed at gmail dot com>
# Maintainer: hexchain <i at hexchain.org>

pkgname=electronic-wechat
pkgver=1.3.0
pkgrel=1
pkgdesc="A better WeChat client"
arch=('x86_64')
url="https://github.com/geeeeeeeeek/electronic-wechat"
license=('custom')
depends=('nss' 'gtk2' 'libnotify' 'libxtst' 'alsa-lib' 'gconf')
makedepends=('git' 'npm' 'imagemagick')
source=(
    "git+https://github.com/geeeeeeeeek/electronic-wechat.git#tag=v${pkgver}"
    electronic-wechat.desktop.in
)

prepare() {
    cd "$srcdir"
    sed "s|@@VERSION@@|$pkgver|" electronic-wechat.desktop.in > electronic-wechat.desktop
}

build() {
    cd "$srcdir/$pkgname"
    npm install
    npm run build:linux64
}

package() {
    cd "$srcdir"
    install -Dm644 electronic-wechat.desktop -t "$pkgdir/usr/share/applications/"

    cd "$srcdir/$pkgname"
    install -Dm644 LICENSE.md "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 assets/icon.png "$pkgdir/usr/share/icons/hicolor/512x512/apps/electronic-wechat.png"

    for size in 16 24 32 48 64 72 128 256; do
        target="$pkgdir/usr/share/icons/hicolor/${size}x${size}/apps/"
        mkdir -p $target
        convert assets/icon.png -resize ${size}x${size} "$target/$pkgname.png"
    done

    cd "$srcdir/$pkgname/dist/$pkgname-linux-x64/"
    mkdir -p "$pkgdir/usr/lib/$pkgname/"
    cp -rv --no-preserve='ownership' * "$pkgdir/usr/lib/$pkgname/"

    mkdir -p "$pkgdir/usr/bin/"
    ln -sf "/usr/lib/$pkgname/$pkgname" "$pkgdir/usr/bin/$pkgname"
}

sha256sums=('SKIP'
            '192d2b31d8faa30142cffecb56352198a316e62b88703f5d3216acdcf76f6730')
