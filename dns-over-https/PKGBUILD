# Maintainer: Sherlock-Holo <sherlockya@gmail.com>

pkgname=dns-over-https
#_pkgname=dns-over-https
pkgver=1.3.2
pkgrel=1
pkgdesc="Client and server software to query DNS over HTTPS, using Google DNS-over-HTTPS protocol"
url="https://github.com/m13253/dns-over-https"
arch=('x86_64' 'i686' 'armv7h')
license=('MIT')
depends=('glibc')
makedepends=('go' 'git')
source=("https://github.com/m13253/dns-over-https/archive/v$pkgver.tar.gz")
backup=('etc/dns-over-https/doh-client.conf'
        'etc/dns-over-https/doh-server.conf')
sha256sums=('acf936645acd494a3f5c2d2b8a4dffd858a0e4e18943ec699fea09b8bcf929f1')

prepare(){
        #mkdir -p $srcdir/gopath
        #export GOPATH=$srcdir/gopath
        cd $srcdir/$pkgname-$pkgver
        sed -i 's/\/usr\/local/${pkgdir}\/usr/g' Makefile
        sed -i 's/\/local//g' systemd/doh-client.service
        sed -i 's/\/local//g' systemd/doh-server.service
}

build(){
        cd $srcdir/$pkgname-$pkgver
        make
}

package(){
        cd $srcdir/$pkgname-$pkgver
        install -Dm755 doh-client/doh-client $pkgdir/usr/bin/doh-client
        install -Dm755 doh-server/doh-server $pkgdir/usr/bin/doh-server

        install -Dm644 doh-client/doh-client.conf $pkgdir/etc/dns-over-https/doh-client.conf
        install -Dm644 doh-server/doh-server.conf $pkgdir/etc/dns-over-https/doh-server.conf

        install -Dm644 systemd/doh-client.service $pkgdir/usr/lib/systemd/system/doh-client.service
        install -Dm644 systemd/doh-server.service $pkgdir/usr/lib/systemd/system/doh-server.service

        install -Dm755 NetworkManager/dispatcher.d/doh-client $pkgdir/etc/NetworkManager/dispatcher.d/doh-client
        install -Dm755 NetworkManager/dispatcher.d/doh-server $pkgdir/etc/NetworkManager/dispatcher.d/doh-server

        install -Dm644 LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE
}
