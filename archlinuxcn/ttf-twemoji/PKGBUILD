# Maintainer: Joe Baker < Joe at JoeBlakeB dot com >

pkgname=ttf-twemoji
pkgver=16.0.1
pkgrel=1
pkgdesc="Truetype builds of Twemoji; Twitter Color Emoji for everyone."
url="https://github.com/jdecked/twemoji"
arch=(any)
license=('Apache-2.0 AND CC-BY-4.0')
provides=('emoji-font' 'twemoji-color-font')
install="$pkgname.install"
source=("https://github.com/JoeBlakeB/ttf-twemoji-aur/releases/download/${pkgver}/Twemoji-${pkgver}.ttf"
        "75-twemoji.conf"
        "https://raw.githubusercontent.com/jdecked/twemoji/v${pkgver}/LICENSE-GRAPHICS"
        "LICENSE-BUILD::https://github.com/JoeBlakeB/ttf-twemoji-aur/blob/${pkgver}/LICENSE")
sha256sums=('26f86e9ef5a37f6a115063f923a56071d7f0af16f193dfb13316f0b68f2b0493'
            'a77a7775557efc1c17781c0fc35a0f7ec5ccd58f233573f8875032fb8575680e'
            'SKIP'
            'SKIP')

package() {
    install -Dm644 "$srcdir/Twemoji-$pkgver.ttf" \
      "${pkgdir}/usr/share/fonts/twemoji/twemoji.ttf"
    install -Dm644 -t "$pkgdir/usr/share/fontconfig/conf.avail" "$srcdir/75-twemoji.conf"
    install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" ${srcdir}/LICENSE*
}
