# Maintainer: SY Zhang <lastavengers@archlinuxcn.org>
# Contributor: Shen Miren <dickeny@gmail.com>
# Contributor: renyuneyun <renyuneyun@gmail.com>

pkgname=mentohust
pkgver=0.3.1
pkgrel=5
pkgdesc="A Ruijie and Cernet supplicant"
arch=('i686' 'x86_64')
url="https://code.google.com/archive/p/mentohust/"
license=('GPL')
depends=('libpcap')
optdepends=('libnotify')
conflicts=('mentohust-git')
provides=()
backup=('etc/mentohust.conf')
install=$pkgname.install
source=("https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/mentohust/${pkgname}-${pkgver}.tar.gz"
		"${pkgname}.service")
	
sha256sums=('e7d15008487d1130c90037581f8243ac145d0114006a08e3f0ac00751b2e1c6a'
            '1a6bacff66f9469f3b3d81772c5b989cbb75f323c64c7aa7478c58199e322db4')


build() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	./configure --prefix=/usr
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	make
	make install DESTDIR="${pkgdir}"
	cd -

	# install systemd service
	install -D -m 755 "${srcdir}/${pkgname}.service" "${pkgdir}/usr/lib/systemd/system/${pkgname}.service"
}
