# Maintainer: Alad Wenter <https://github.com/AladW>
pkgname=aurutils
pkgver=2.3.7
pkgrel=1
pkgdesc='helper tools for the arch user repository'
url='https://github.com/AladW/aurutils'
arch=('any')
license=('custom:ISC')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz"
        "$pkgname-$pkgver.tar.gz.signify::$url/releases/download/$pkgver/$pkgver.tar.gz.sig")
depends=('git' 'jq' 'expac' 'diffstat' 'pacutils' 'wget')
makedepends=('git' 'signify')
optdepends=('bash-completion: bash completion'
            'devtools: aur-chroot'
            'vifm: build file interaction')
sha256sums=('bae2f7211cb80626f260e1ebcb2c061751407a03f1ab8898bc80182888502bef'
            'SKIP')
_validsignifykey='RWQawitEue1JU2SxUyRD8LXP8m36QsbaHOkKfvZBfhj00EXBYiDZilp0'

prepare() {
    cat >aurutils-23.pub <<EOF
untrusted comment: signify public key
$_validsignifykey
EOF
    signify -V -p aurutils-23.pub -m "$pkgname-$pkgver".tar.gz \
            -x "$pkgname-$pkgver".tar.gz.signify
}

build() {
    cd "$pkgname-$pkgver"
    make
}

package() {
    cd "$pkgname-$pkgver"
    make DESTDIR="$pkgdir" install
}
