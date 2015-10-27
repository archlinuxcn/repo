# Maintainer: Hexchain Tong <i at hexchain dot org>

pkgname=tinc-pre
pkgver=1.1pre11
pkgrel=4
pkgdesc="VPN (Virtual Private Network) daemon (Pre-release)"
arch=(i686 x86_64)
url="http://www.tinc-vpn.org/"
license=('GPL')
depends=('lzo2' 'openssl')
optdepends=('wxpython: gui support')
provides=('tinc-pre' 'tinc-pre-systemd')
conflicts=('tinc' 'tinc-pre-systemd')
install="${pkgname}.install"
source=(http://www.tinc-vpn.org/packages/tinc-$pkgver.tar.gz
        tincd.service
        tincd@.service)

build() {
    cd "$srcdir/tinc-$pkgver"

    ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --sbindir=/usr/bin
    make
}

package() {
    cd "$srcdir/tinc-$pkgver"
    make DESTDIR="$pkgdir" install

    mkdir -p "$pkgdir/etc/tinc/"
    install -Dm644 "$srcdir/tinc-$pkgver/doc/sample-config.tar.gz" -t "$pkgdir/usr/share/doc/tinc-pre/"

    install -Dm644 "$srcdir/tincd.service" -t "$pkgdir/usr/lib/systemd/system"
    install -Dm644 "$srcdir/tincd@.service" -t "$pkgdir/usr/lib/systemd/system"

    sed -i 's,#!/usr/bin/env python,#!/usr/bin/env python2,' "$pkgdir/usr/bin/tinc-gui"
}

sha256sums=('942594563d3aef926a2d04e9ece90c16daf1c700e99e3b91ff749e8377fbf757'
            '35d76d63e0403550bf68632603cf6e51352f6b85f0269853af875f6b434fb9e1'
            '4783faab2589ba67dc6fceb2e37a736914cc5afc2f741aadf990e027f0b957f2')
