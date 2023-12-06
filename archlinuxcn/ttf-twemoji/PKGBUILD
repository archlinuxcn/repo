# Maintainer: Joe Baker < Joe at JoeBlakeB dot com >

pkgname=ttf-twemoji
pkgver=15.0.2
pkgrel=1
_build_date=2023-12-05_16-23
_build_commit=2d23f3f22a191769b5bcc2757cacdf66fff85dca
pkgdesc="Truetype builds of Twemoji; Twitter Color Emoji for everyone."
url="https://git.sr.ht/~whynothugo/twemoji.ttf"
arch=(any)
license=('CCPL' 'Apache')
provides=('emoji-font')
install="$pkgname.install"
ttfFile="Twemoji-$pkgver.ttf"
source=("https://artefacts.whynothugo.nl/twemoji.ttf/${_build_date}/$ttfFile"
        "75-twemoji.conf"
        "https://raw.githubusercontent.com/jdecked/twemoji/v${pkgver}/LICENSE-GRAPHICS"
        "LICENSE-BUILD::https://git.sr.ht/~whynothugo/twemoji.ttf/blob/${_build_commit}/LICENCE")
sha256sums=('0a348feb7bceb00b584867bdfdef4dc7dcd1cddc60eba1d433a9c474600a0da0'
            'a77a7775557efc1c17781c0fc35a0f7ec5ccd58f233573f8875032fb8575680e'
            'SKIP'
            'SKIP')

package() {
    install -Dm644 "$srcdir/Twemoji-$pkgver.ttf" \
      "${pkgdir}/usr/share/fonts/twemoji/twemoji.ttf"
    install -Dm644 -t "$pkgdir/usr/share/fontconfig/conf.avail" "$srcdir/75-twemoji.conf"
    install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" ${srcdir}/LICENSE*
}
