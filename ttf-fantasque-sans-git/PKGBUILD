# Maintainer: Parantapa Bhattacharya <pb at parantapa dot net>
pkgname=ttf-fantasque-sans-git
pkgver=1.6.5.r117.85142fe
pkgrel=1
pkgdesc="A font family with a great monospaced variant for programmers."
arch=('any')
url="https://github.com/belluzj/fantasque-sans"
license=('SIL OPEN FONT LICENSE Version 1.1')
depends=('fontconfig' 'xorg-font-utils')
makedepends=('git' 'fontforge' 'ttfautohint' 'sfnt2woff' 'ttf2eot')
install=$pkgname.install
source=(repo::git+https://github.com/belluzj/fantasque-sans.git)
md5sums=('SKIP')

pkgver() {
    local p1 p2 p3

    cd "$srcdir/repo"
    p1="$(grep -P '^version' pkg.sh | cut -d '=' -f 2 | tr -d "'")"
    p2="$(git rev-list --count HEAD)"
    p3="$(git rev-parse --short HEAD)"
    printf "%s.r%s.%s" "$p1" "$p2" "$p3"
}

build() {
    cd "$srcdir/repo"
    make
}

package() {
    install -d "${pkgdir}/usr/share/fonts/TTF"
    cp -dpr --no-preserve=ownership "${srcdir}/repo/"*.ttf "${pkgdir}/usr/share/fonts/TTF"
}
