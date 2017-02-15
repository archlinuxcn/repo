# Contributor: wenLiangcan <boxeed at gmail dot com>
# Maintainer: hexchain <i at hexchain.org>

pkgname=electronic-wechat
pkgver=2.0rc1
pkgrel=1
pkgdesc="A better WeChat client"
arch=('x86_64')
url="https://github.com/geeeeeeeeek/electronic-wechat"
license=('custom')
depends=('electron')
makedepends=('git' 'npm' 'imagemagick')
source=(
    "git+https://github.com/geeeeeeeeek/electronic-wechat.git#tag=v2.0-rc1"
    'electronic-wechat.desktop'
    'remove-bundle-electron.patch'
    'electronic-wechat.sh'
)

prepare() {
    cd "$srcdir/$pkgname"
    patch -p1 < "$srcdir/remove-bundle-electron.patch"
}

build() {
    cd "$srcdir/$pkgname"
    npm install
    # npm run build:linux64
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
    cp -r --no-preserve='ownership' -- * "$pkgdir/usr/lib/$pkgname/"
    install -Dm755 "$srcdir/electronic-wechat.sh" "$pkgdir/usr/bin/electronic-wechat"
}

# package() {
#     cd "$srcdir"
#     install -Dm644 electronic-wechat.desktop -t "$pkgdir/usr/share/applications/"

#     cd "$srcdir/$pkgname"
#     install -Dm644 LICENSE.md "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
#     install -Dm644 assets/icon.png "$pkgdir/usr/share/icons/hicolor/512x512/apps/electronic-wechat.png"

#     for size in 16 24 32 48 64 72 128 256; do
#         target="$pkgdir/usr/share/icons/hicolor/${size}x${size}/apps/"
#         mkdir -p $target
#         convert assets/icon.png -resize ${size}x${size} "$target/$pkgname.png"
#     done

#     cd "$srcdir/$pkgname/dist/electronic-wechat-linux-x64/"
#     mkdir -p "$pkgdir/usr/lib/$pkgname/"
#     cp -rv --no-preserve='ownership' -- * "$pkgdir/usr/lib/$pkgname/"
#     # install -Dm755 "$srcdir/electronic-wechat.sh.in" "$pkgdir/usr/bin/electronic-wechat"
#     mkdir -p "$pkgdir/usr/bin"
#     ln -sf "/usr/lib/$pkgname/electronic-wechat" "$pkgdir/usr/bin/"
# }

sha256sums=('SKIP'
            '56c0db46c3b9fc31ac16265d0346ef47a6422392607bcce954e0f550894475be'
            'e6db14369ebd0071f9c9302aab0eed07fd4eff67375c522e03b3b6eb800f2891'
            'dddbd40a98fdfa47728fadaceda35a5ac38f59fd1be4fde2cbdaaf309d4e6bf1')
