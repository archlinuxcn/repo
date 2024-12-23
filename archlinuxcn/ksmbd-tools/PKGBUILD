# Maintainer: Leonidas P. <jpegxguy at outlook dot com>

pkgname=ksmbd-tools
pkgver=3.5.3
pkgrel=1
pkgdesc="Userspace tools for the ksmbd kernel SMB server"
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url="https://github.com/cifsd-team/ksmbd-tools"
license=('GPL2')
depends=('KSMBD-MODULE' 'libnl')
provides=('samba')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=("2b0a9c117d8e66f1e9ad819f1a1925af2f54e3940cf19f67eba86b2ee9171d4d")

build() {
	cd "${pkgname}-${pkgver}"
	./autogen.sh
	./configure --prefix=/usr --sbindir=/usr/bin --libexecdir=/usr/lib/${pkgname} --sysconfdir=/etc --with-rundir=/run
	make
}

package() {
	cd "${pkgname}-${pkgver}"
	make DESTDIR="${pkgdir}" install
}
