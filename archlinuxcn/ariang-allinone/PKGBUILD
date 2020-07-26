# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=ariang-allinone
pkgver=1.1.6
pkgrel=1
pkgdesc="A modern web frontend making aria2 easier to use (all-in-one version)"
arch=('any')
url="https://github.com/mayswind/AriaNg"
license=('MIT')
depends=('xdg-utils')
makedepends=('git' 'nvm')
source=("$url/archive/$pkgver.tar.gz"
        "$pkgname.desktop"
        "$pkgname.sh")
sha256sums=('832b951120dc6974c7104fd6ee5887f3b1f9a467b2c6fc2c0257340e9123c82c'
            '37ddfc79173070226c053a6e4efcae5113162e152a3d472ceb2408b886311a5a'
            'c6c617a9bc32885b8f89c8b7120b67f98f6df52e141db6cfd24ffcd89435ec6a')

build() {
    cd "AriaNg-$pkgver"
    source /usr/share/nvm/init-nvm.sh
    nvm install 8.17.0
    npm install --devDependencies
    node_modules/gulp/bin/gulp.js clean build-bundle
}

package() {
    cd "AriaNg-$pkgver"
    install -Dm 644 "src/favicon.png" "$pkgdir/usr/share/icons/hicolor/32x32/apps/$pkgname.png"
    install -Dm 644 "dist/index.html" "$pkgdir/usr/share/$pkgname/index.html"
    install -Dm 644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm 644 "$srcdir/$pkgname.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"
    install -Dm 755 "$srcdir/$pkgname.sh" "$pkgdir/usr/bin/$pkgname"
}
