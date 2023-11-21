# Maintainer: Gyara <laxect39@gmail.com>

pkgname=beancount-language-server
pkgver=1.3.1
pkgrel=1
pkgdesc="A Language Server Protocol (LSP) for beancount files"
arch=('any')
url="https://github.com/polarmutex/${pkgname}"
license=('MIT')
depends=('beancount')
makedepends=('cargo')
source=(https://github.com/polarmutex/${pkgname}/archive/v${pkgver//_/-}.tar.gz)
sha512sums=('e93b658483d9b942b9db19f0627d7c2171e6a223f06aa2cc8fbf50c63eb7a94a4a3aae62efe7a75d29b5910302b4ccd483edda5c507594d5275eb5f49f611aac')

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    cargo build --release --target-dir=target
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    install -Dm755 "target/release/$pkgname" "$pkgdir/usr/bin/$pkgname"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
