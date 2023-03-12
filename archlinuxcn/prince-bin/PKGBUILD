# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Maintainer: Yoan Blanc <yoan@dosimple.ch>
# Contributor: Harry Jeffery <harry|@|exec64|.|co|.|uk>
# Contributor: Chris Morgan <me@chrismorgan.info>

pkgname=prince-bin
pkgver=15.1
pkgrel=1
pkgdesc="Convert HTML documents to PDF with CSS"
arch=(x86_64 aarch64)
url='https://www.princexml.com/'
license=('custom')
depends=('ca-certificates-utils' 'fontconfig' 'libidn' 'libxml2')
provides=("${pkgname%-bin}" 'princexml')
conflicts=('sdlpop' 'princexml')
replaces=('princexml')
backup=("etc/${pkgname%-bin}/license.dat")
source=('prince.sh')
source_x86_64=("https://www.princexml.com/download/${pkgname%-bin}-$pkgver-linux-generic-x86_64.tar.gz")
source_aarch64=("https://www.princexml.com/download/${pkgname%-bin}-$pkgver-linux-generic-aarch64.tar.gz")
sha256sums=('a02a6159dd0ae8b2a2440c21ed370fd5057148cc6633214f8bc48228d23138fb')
sha256sums_x86_64=('ae6d0678a3daf220d70615b9d8635c8dad3d41bf9a614b6f15ac595051c4393c')
sha256sums_aarch64=('2b76b4f2231a2501fd5fff9c1b80ea75103d1fc2a2012ed27d0fc59cd898f7c9')

prepare() {
    cd "${pkgname%-bin}-$pkgver-linux-generic-$CARCH"
    mkdir -p "etc/${pkgname%-bin}"
    mv lib/prince/license/license.dat "etc/${pkgname%-bin}/"
    ln -sf "../../../../etc/${pkgname%-bin}/license.dat" lib/prince/license
    ln -sf "../../../../etc/ssl/certs/ca-certificates.crt" lib/prince/etc/curl-ca-bundle.crt
}

package() {
    cd "${pkgname%-bin}-$pkgver-linux-generic-$CARCH"
    install -Dm755 "../${source[0]}" "$pkgdir/usr/bin/${pkgname%-bin}"
    install -Dm644 -t "$pkgdir/usr/share/licenses/${pkgname%-bin}" LICENSE CREDITS
    install -Dm644 -t "$pkgdir/usr/share/doc/${pkgname%-bin}" README
    install -Dm644 -t "$pkgdir/etc/${pkgname%-bin}/" "etc/${pkgname%-bin}/license.dat"
    mkdir -p "$pkgdir/usr/lib/"
    cp -a lib/prince "$pkgdir/usr/lib/"
}
