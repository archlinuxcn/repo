# Maintainer: Håvard Pettersson <mail@haavard.me>
# Contributor: Ivan Shapovalov <intelfx100 at gmail dot com>

_pkgname=libfilteraudio
pkgname=libfilteraudio-git
pkgver=r92.612c5a1
pkgrel=1
pkgdesc="An easy to use audio filtering library made from webrtc code"
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h')
url="https://github.com/irungentoo/filter_audio"
license=('BSD')
makedepends=('git')
depends=('glibc')
provides=("${_pkgname}" 'filter_audio')
conflicts=("${_pkgname}" 'filter_audio')
source=(
    "${_pkgname}::git+https://github.com/irungentoo/libfilteraudio.git"
    'LICENSE'
)
sha512sums=('SKIP'
            'ab7ea75c03fab3dfc5d452f04a38b42783f646c2e0acaf8494628bfdf6f83e4b04d470e019385de3e89dd57eb8ef6d02daa6256d4ff311cc66f3999b694ef143')

pkgver() {
    cd ${_pkgname}
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    cd ${_pkgname}
    make
}

package() {
    cd ${_pkgname}
    make DESTDIR="$pkgdir" PREFIX="/usr" install
    install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
