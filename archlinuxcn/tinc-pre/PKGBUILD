# Maintainer: hexchain <i at hexchain dot org>

pkgname=tinc-pre
pkgver=1.1pre17
pkgrel=2
pkgdesc="VPN (Virtual Private Network) daemon (Pre-release)"
arch=(i686 x86_64 armv7h armv6h)
url="http://www.tinc-vpn.org/"
license=('GPL')
depends=('lzo' 'zlib' 'openssl' 'miniupnpc')
makedepends=('git' 'autoconf')
optdepends=('python2' 'wxpython: gui support')
provides=('tinc-pre' 'tinc-pre-systemd')
conflicts=('tinc' 'tinc-pre-systemd')
source=("git+https://github.com/gsliepen/tinc.git#tag=release-$pkgver")
sha256sums=('SKIP')

build() {
    cd "$srcdir/tinc"

    export GIT_COMMITTER_NAME="Builder" GIT_COMMITTER_EMAIL="builder@builder.local"
    git cherry-pick 2b0aeec02d64bb4724da9ff1dbc19b7d35d7c904
    git cherry-pick f8190b7233871b5b47c3fc8846731d1bbdef78a5
    git cherry-pick f3ba50ed3d14749b7c1ef100d2a49ac30d3b3853
    unset GIT_COMMITTER_EMAIL GIT_COMMITTER_NAME

    autoreconf -fsi
    ./configure \
        --prefix=/usr \
        --sbindir=/usr/bin \
        --sysconfdir=/etc \
        --localstatedir=/var \
        --with-systemd=/usr/lib/systemd/system \
        --enable-miniupnpc
    make
}

package() {
    cd "$srcdir/tinc"
    make DESTDIR="$pkgdir" install

    mkdir -p "$pkgdir/etc/tinc/"
    mkdir -p "$pkgdir/usr/share/doc/tinc-pre/"
    cp -rv --no-preserve='ownership' "doc/sample-config/" "$pkgdir/usr/share/doc/tinc-pre/"
    install -Dm644 "bash_completion.d/tinc" -t "$pkgdir/usr/share/bash-completion/completions/"
}
