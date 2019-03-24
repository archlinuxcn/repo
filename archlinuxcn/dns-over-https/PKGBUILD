# Maintainer: Sherlock Holo <sherlockya(at)gmail.com>
# Contributors: Ariel AxionL <i [at] axionl [dot] me>

pkgbase='dns-over-https'
pkgname=('dns-over-https-client' 'dns-over-https-server')
pkgver=2.0.0
pkgrel=1
pkgdesc="Client and server software to query DNS over HTTPS, using Google DNS-over-HTTPS protocol"
url="https://github.com/m13253/dns-over-https"
arch=('x86_64' 'i686' 'armv7h')
license=('MIT')
makedepends=('go' 'git')

source=("$url/archive/v$pkgver.tar.gz")

sha256sums=('f8b8b33e9e2e31c73554785cc5ce825d0a69ecd80182ceff0766e4974c7c5290')

build() {
    mkdir -p ${srcdir}/go/src
    export GOPATH="${srcdir}/go"

    cd ${srcdir}/${pkgbase}-${pkgver}
    sed -i 's/\/local//g' systemd/doh-client.service
    sed -i 's/\/local//g' systemd/doh-server.service

    go mod download
    
    # build client
    go build -gcflags "all=-trimpath=${PWD}" -asmflags "all=-trimpath=${PWD}" -ldflags "-w -s -extldflags ${LDFLAGS}" -v -o client ./doh-client
    
    # build server
    go build -gcflags "all=-trimpath=${PWD}" -asmflags "all=-trimpath=${PWD}" -ldflags "-w -s -extldflags ${LDFLAGS}" -v -o server ./doh-server

    # clean build cache
    chmod 777 -R $GOPATH/pkg/mod
    rm -rf $GOPATH/pkg/mod
}

package_dns-over-https-client() {
    # Backup and conflicts
    backup=('etc/dns-over-https/doh-client.conf')
    conflicts=('dns-over-https' 'dns-over-https-client-git')
    provides=('dns-over-https-client')

    # Install binary
    install -Dm755 ${srcdir}/${pkgbase}-${pkgver}/client ${pkgdir}/usr/bin/doh-client

    # Install others
    cd ${srcdir}/${pkgbase}-${pkgver}
    install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
    install -Dm644 doh-client/doh-client.conf ${pkgdir}/etc/dns-over-https/doh-client.conf
    install -Dm644 systemd/doh-client.service ${pkgdir}/usr/lib/systemd/system/doh-client.service
    install -Dm755 NetworkManager/dispatcher.d/doh-client ${pkgdir}/etc/NetworkManager/dispatcher.d/doh-client
}

package_dns-over-https-server() {
    # Backup and conflicts
    optdepends=('dns-over-https-client')
    backup=('etc/dns-over-https/doh-server.conf')
    conflicts=('dns-over-https-server-git')
    provides=('dns-over-https-server')
    replaces=('dns-over-https')

    # Install binary
    install -Dm755 ${srcdir}/${pkgbase}-${pkgver}/server ${pkgdir}/usr/bin/doh-server

    # Install others
    cd ${srcdir}/${pkgbase}-${pkgver}
    install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
    install -Dm644 doh-server/doh-server.conf ${pkgdir}/etc/dns-over-https/doh-server.conf
    install -Dm644 systemd/doh-server.service ${pkgdir}/usr/lib/systemd/system/doh-server.service
    install -Dm755 NetworkManager/dispatcher.d/doh-server ${pkgdir}/etc/NetworkManager/dispatcher.d/doh-server
}
# vim:set ts=4 sw=4 et:
