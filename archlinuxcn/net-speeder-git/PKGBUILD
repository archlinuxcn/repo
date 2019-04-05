# Maintainer: Dct Mei <dctxmei@gmail.com>
pkgname=net-speeder-git
pkgver=20160303
pkgrel=1
pkgdesc="A program to speed up single thread download upon long delay and unstable network"
arch=('x86_64')
url="https://github.com/snooda/net-speeder"
license=('GPL')
depends=("libnet" "libpcap")
makedepends=("git")
provides=('net-speeder')
conflicts=('net-speeder')
source=("git+https://github.com/snooda/net-speeder.git"
        "net-speeder.service")
sha512sums=('SKIP'
            '4c49ae81c1480f4ea2fffbb32b45a8a4ece2c730e250c1c7efadfebf22a94a488982c557a47f13b51091cc7f06b147de4b09208940f1a11c7e8176162f3c2914')

prepare() {
    git -C net-speeder log -1 --format='%cd' --date=short | tr -d -- '-'
}

build() {
    cd net-speeder
    bash build.sh
    #bash build.sh -DCOOKED
}

package() {
    install -Dm755 "$srcdir"/net-speeder/net_speeder "$pkgdir"/usr/bin/net-speeder
    install -Dm644 "$srcdir"/net-speeder.service "$pkgdir"/usr/lib/systemd/system/net-speeder@.service
}
