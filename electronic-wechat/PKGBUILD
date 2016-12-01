# Contributor: wenLiangcan <boxeed at gmail dot com>
# Maintainer: hexchain <i at hexchain.org>

pkgname=electronic-wechat
pkgver=1.4.0
pkgrel=1
pkgdesc="A better WeChat client"
arch=('x86_64')
url="https://github.com/geeeeeeeeek/electronic-wechat"
license=('custom')
depends=('electron')
makedepends=('git' 'npm' 'imagemagick')
source=(
    "git+https://github.com/geeeeeeeeek/electronic-wechat.git#tag=v${pkgver}"
    electronic-wechat.desktop.in
    'remove-bundle-electron.patch'
    'electronic-wechat.sh.in'
)

prepare() {
    cd "$srcdir"
    sed "s|@@VERSION@@|$pkgver|" electronic-wechat.desktop.in > electronic-wechat.desktop

    cd "$srcdir/$pkgname"
    patch -p1 < "$srcdir/remove-bundle-electron.patch"
}

build() {
    cd "$srcdir/$pkgname"
    npm install
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

    cd "$srcdir/$pkgname/"
    rm -rf scripts
    mkdir -p "$pkgdir/usr/lib/$pkgname/"
    cp -rv --no-preserve='ownership' -- * "$pkgdir/usr/lib/$pkgname/"
    install -Dm755 "$srcdir/electronic-wechat.sh.in" "$pkgdir/usr/bin/electronic-wechat"
}

sha256sums=('SKIP'
            '192d2b31d8faa30142cffecb56352198a316e62b88703f5d3216acdcf76f6730'
            'fe5e738390b7f638d2aa6e98ed2212b4de9964ddbcee4a380a7079eb06330427'
            '52b5c50a43f3a92e58d06f568152ed3d06d46318dc98dcbb10497f24f0353245')
