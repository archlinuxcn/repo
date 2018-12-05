# Maintainer: Sherlock Holo <sherlockya(at)gmail.com>
pkgname=dns-over-https
_pkgver=1.4.2
pkgver=v$_pkgver
_pkgname=$pkgname
pkgrel=1
pkgdesc="Client and server software to query DNS over HTTPS, using Google DNS-over-HTTPS protocol"
url="https://github.com/m13253/dns-over-https"
arch=('i686' 'x86_64' 'armv7h')
license=('MIT')
depends=()
makedepends=('go' 'git')
source=("https://github.com/m13253/dns-over-https/archive/$pkgver.tar.gz")
backup=(
'etc/dns-over-https/doh-client.conf'
'etc/dns-over-https/doh-server.conf'
)
sha256sums=('c3181a8cd20710f09cc6b6749da7f6c05fd1eb063a4c8d740b42e50dbddc045d')

build() {
    mv $srcdir/$pkgname-$_pkgver $srcdir/$_pkgname

    rm -rf "$srcdir/go/src"

    mkdir -p "$srcdir/go/src"

    export GOPATH="$srcdir/go"

    mv "$srcdir/$_pkgname" "$srcdir/go/src/"

    cd "$srcdir/go/src/$_pkgname/"

    echo ":: Building binary"

    cd "$srcdir/go/src/$_pkgname/doh-client"
    go get -v \
            -gcflags "-trimpath $GOPATH/src"

    cd "$srcdir/go/src/$_pkgname/doh-server"
    go get -v \
            -gcflags "-trimpath $GOPATH/src"
    }

package() {
    find "$srcdir/go/bin/" -type f -executable | while read filename; do
        install -DT "$filename" "$pkgdir/usr/bin/$(basename $filename)"
    done

    cd $srcdir/go/src/$_pkgname
    install -Dm644 doh-client/doh-client.conf $pkgdir/etc/dns-over-https/doh-client.conf
    install -Dm644 doh-server/doh-server.conf $pkgdir/etc/dns-over-https/doh-server.conf

    install -Dm644 systemd/doh-client.service $pkgdir/usr/lib/systemd/system/doh-client.service
    install -Dm644 systemd/doh-server.service $pkgdir/usr/lib/systemd/system/doh-server.service

    install -Dm755 NetworkManager/dispatcher.d/doh-client $pkgdir/etc/NetworkManager/dispatcher.d/doh-client
    install -Dm755 NetworkManager/dispatcher.d/doh-server $pkgdir/etc/NetworkManager/dispatcher.d/doh-server
}
