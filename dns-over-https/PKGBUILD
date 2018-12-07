# Maintainer: Sherlock Holo <sherlockya(at)gmail.com>
# Contributors: Ariel AxionL <i [at] axionl [dot] me>

pkgbase='dns-over-https'
pkgname=('dns-over-https-client' 'dns-over-https-server')
pkgver=1.4.2
pkgrel=5
pkgdesc="Client and server software to query DNS over HTTPS, using Google DNS-over-HTTPS protocol"
url="https://github.com/m13253/dns-over-https"
arch=('x86_64' 'i686' 'armv7h')
license=('MIT')
depends=('bash')
makedepends=('go' 'git')

source=("$url/archive/v$pkgver.tar.gz")

sha256sums=('c3181a8cd20710f09cc6b6749da7f6c05fd1eb063a4c8d740b42e50dbddc045d')

prepare() {
    export GOPATH="${srcdir}/build"
    export BUILDPATH="${srcdir}/build/src/github.com/m13253"

    install -dm755 ${BUILDPATH}
    cp ${pkgbase}-${pkgver} ${BUILDPATH}/${pkgbase} -r
}

build() {
    export GOPATH="${srcdir}/build"
    export BUILDPATH="${srcdir}/build/src/github.com/m13253"

    cd ${srcdir}/${pkgbase}-${pkgver}
    sed -i 's/\/local//g' systemd/doh-client.service
    sed -i 's/\/local//g' systemd/doh-server.service

    cd ${BUILDPATH}/${pkgbase}/doh-client
    go get -v -gcflags "-trimpath $GOPATH/src"

    cd ${BUILDPATH}/${pkgbase}/doh-server
    go get -v -gcflags "-trimpath $GOPATH/src"
}

package_dns-over-https-client() {
    # Backup and conflicts
    backup=('etc/dns-over-https/doh-client.conf')
    conflicts=('dns-over-https' 'dns-over-https-client-git')
    provides=('dns-over-https-client')

    # Install binary
    install -Dm755 ${srcdir}/build/bin/doh-client ${pkgdir}/usr/bin/doh-client

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
    install -Dm755 ${srcdir}/build/bin/doh-server ${pkgdir}/usr/bin/doh-server

    # Install others
    cd ${srcdir}/${pkgbase}-${pkgver}
    install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
    install -Dm644 doh-server/doh-server.conf ${pkgdir}/etc/dns-over-https/doh-server.conf
    install -Dm644 systemd/doh-server.service ${pkgdir}/usr/lib/systemd/system/doh-server.service
    install -Dm755 NetworkManager/dispatcher.d/doh-server ${pkgdir}/etc/NetworkManager/dispatcher.d/doh-server
}
# vim:set ts=4 sw=4 et:
