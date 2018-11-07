# Maintainer: Stephan Springer <buzo+arch@Lini.de>
# Contributor: wenLiangcan <boxeed at gmail dot com>
# Contributor: hexchain <i at hexchain.org>

pkgname=electronic-wechat
pkgver=2.2.1
pkgrel=1
pkgdesc="A better WeChat client"
arch=('x86_64')
url='https://github.com/kooritea/electronic-wechat'
license=('custom')
depends=('electron' 'python' 'nodejs' 'hicolor-icon-theme')
optdepends=('libappindicator-gtk3: fix broken tray icon in KDE')
makedepends=('git' 'npm' 'python2' 'imagemagick')
source=(
    "$pkgname-$pkgver.tar.gz::https://github.com/kooritea/electronic-wechat/archive/v$pkgver.tar.gz"
    'electronic-wechat.desktop'
    'electronic-wechat.sh'
)
sha256sums=('f78ca4e94753f09a243a20e17fa4866fd565b9a671d43f565797f10bf15e91b5'
            '56c0db46c3b9fc31ac16265d0346ef47a6422392607bcce954e0f550894475be'
            '10696031537d5d749b1d8914829057d73aaccb788263b4df8bc5ff7ed7939bff')

prepare() {
    cd "$pkgname-$pkgver"
    # remove Electron bundle
    sed -i '/"electron\(-packager\)*":/d' package.json
}

build() {
    cd "$pkgname-$pkgver"
    PYTHON=/usr/bin/python2 npm install
    # npm run build:linux64
}

package() {
    install -Dm644 electronic-wechat.desktop -t "$pkgdir/usr/share/applications"

    cd "$pkgname-$pkgver"
    install -Dm644 LICENSE.md "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 assets/icon.png "$pkgdir/usr/share/icons/hicolor/512x512/apps/electronic-wechat.png"

    for size in 16 24 32 48 64 72 128 256; do
        target="$pkgdir/usr/share/icons/hicolor/${size}x${size}/apps"
        mkdir -p $target
        convert assets/icon.png -resize ${size}x${size} "$target/$pkgname.png"
    done
    rm -rf scripts
    mkdir -p "$pkgdir/usr/lib/$pkgname"
    cp -r --no-preserve='ownership' -- * "$pkgdir/usr/lib/$pkgname"
    install -Dm755 "$srcdir/electronic-wechat.sh" "$pkgdir/usr/bin/electronic-wechat"
}
