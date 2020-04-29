# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=ariang-allinone
pkgver=1.1.5
pkgrel=2
pkgdesc="A modern web frontend making aria2 easier to use (all-in-one version)"
arch=('any')
url="https://github.com/mayswind/AriaNg"
license=('MIT')
depends=('bash')
makedepends=('git' 'nvm')
source=("$url/archive/1.1.5.tar.gz"
        "$pkgname.desktop"
        "$pkgname.sh")
sha512sums=('ca41d9012ba5fcec5efbdae2d670064e08f4a2949087b3c4b5a62c9375060834d02f13451f3371695835258b13d1380b7142e25203556b2153850b2b32c927c2'
            '135e1c1a2316228277e7019619285be2a43d0ad93191d7273dfdb6087566727c6037e9686fa87a13426136cd721b221c8732f4ff761af04cfa12468d8bf4ec3b'
            '2fa24e140565396feb0b502476b1de6e83fae1d77316c64167653cf460fe4e39b6159fd7c11ae1d242b5372a01527fcaef55d735fe9392569da1af8b60cdf9db')

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
