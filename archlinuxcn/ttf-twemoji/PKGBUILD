# Maintainer: Joe Baker < Joe at JoeBlakeB dot com >

pkgname=ttf-twemoji
pkgver=15.0.3
pkgrel=1
pkgdesc="Truetype builds of Twemoji; Twitter Color Emoji for everyone."
url="https://github.com/jdecked/twemoji"
arch=(any)
license=('CCPL' 'Apache')
provides=('emoji-font' 'twemoji-color-font')
install="$pkgname.install"
source=("https://github.com/JoeBlakeB/ttf-twemoji-aur/releases/download/${pkgver}/Twemoji-${pkgver}.ttf"
        "75-twemoji.conf"
        "https://raw.githubusercontent.com/jdecked/twemoji/v${pkgver}/LICENSE-GRAPHICS"
        "LICENSE-BUILD::https://github.com/JoeBlakeB/ttf-twemoji-aur/blob/${pkgver}/LICENSE")
sha256sums=('89dbdb4109ad94ced626305ea7758467e2aa26f26c4c943882fdbb8853245186'
            'a77a7775557efc1c17781c0fc35a0f7ec5ccd58f233573f8875032fb8575680e'
            'SKIP'
            'SKIP')

package() {
    install -Dm644 "$srcdir/Twemoji-$pkgver.ttf" \
      "${pkgdir}/usr/share/fonts/twemoji/twemoji.ttf"
    install -Dm644 -t "$pkgdir/usr/share/fontconfig/conf.avail" "$srcdir/75-twemoji.conf"
    install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" ${srcdir}/LICENSE*
}
