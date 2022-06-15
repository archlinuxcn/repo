# Maintainer: Joe Baker < JoeBlakeB at protonmail dot com >

pkgname=ttf-twemoji
pkgver=14.0.2
pkgrel=1
_fedrel=1.fc37
pkgdesc="Twitter Emoji for everyone."
url="https://github.com/twitter/twemoji"
arch=(any)
license=('CCPL' 'MIT' 'Apache')
depends=('fontconfig')
provides=('emoji-font')
install="$pkgname.install"
source=("https://kojipkgs.fedoraproject.org/packages/twitter-twemoji-fonts/${pkgver}/${_fedrel}/noarch/twitter-twemoji-fonts-${pkgver}-${_fedrel}.noarch.rpm"
        "75-twemoji.conf")
sha256sums=('d65c31e96cdbefd4d5e463806a620afb3e938f488220eb1f851889a746c0adbc'
            'a77a7775557efc1c17781c0fc35a0f7ec5ccd58f233573f8875032fb8575680e')

package() {
    install -Dm644 usr/share/fonts/twemoji/Twemoji.ttf \
      "${pkgdir}/usr/share/fonts/twemoji/twemoji.ttf"
    install -Dm644 -t "$pkgdir/usr/share/fontconfig/conf.avail" 75-twemoji.conf
    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
      usr/share/licenses/twitter-twemoji-fonts/LICENSE{,-{BUILD,GRAPHICS}}
}
