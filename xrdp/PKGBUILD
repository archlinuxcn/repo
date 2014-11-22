# Maintainer: Tomasz Zok <tomasz.zok [at] gmail.com>
# Maintainer: techryda <techryda at silentdome dot com>
# Contributor: Mathias R. <pu154r@overlinux.org>
pkgname=xrdp
pkgver=0.6.1
pkgrel=1
pkgdesc="An open source remote desktop protocol (RDP) server"
url="http://xrdp.sourceforge.net/"
arch=('i686' 'x86_64' 'armv6h')
license=('GPL')
depends=('tigervnc')
source=("http://downloads.sourceforge.net/project/$pkgname/$pkgname/$pkgver/$pkgname-v$pkgver.tar.gz"
        'xrdp.service'
        'xrdp-sesman.service')
md5sums=('26099c6588943262023607c1b4e774d8'
         '0cb760b3e8a34f9bdf4daa871444d74c'
         '58eb44bdc7ca5bb436d6fd66826f9b0f')

prepare() {
    cd "${pkgname}-v${pkgver}"
    # Fix path in xrdp.sh file
    sed -i 's|/usr/local/sbin|/usr/bin|' instfiles/xrdp.sh
}

build() {
    cd "${pkgname}-v${pkgver}"
    ./bootstrap
    ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --sbindir=/usr/bin
    make
}

package() {
    cd "${pkgname}-v${pkgver}"
    make DESTDIR="$pkgdir" install
    cd ${pkgdir}
    # Install systemd service files
    mkdir -p usr/lib/systemd/system
    cp ${srcdir}/*.service usr/lib/systemd/system
}
