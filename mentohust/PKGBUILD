# Contributor: Shen Miren <dickeny@gmail.com>
pkgname=mentohust
pkgver=0.3.1
pkgrel=3
pkgdesc="A Ruijie and Cernet supplicant"
arch=('i686' 'x86_64')
url="http://mentohust.googlecode.com"
license=('GPL')
makedepends=('libpcap')
optdepends=('libnotify')
conflicts=()
provides=()
backup=('etc/mentohust.conf')
install=$pkgname.install
source=(http://mentohust.googlecode.com/files/${pkgname}-${pkgver}.tar.gz
        ${pkgname}_rc.sh)
	
md5sums=('c7033ba8d8e75294924ed03f4b7b0c45'
         '52b1286fb644bcc6d9d742cb7da23a24')

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    ./configure --prefix=/usr
    make || return 1
    make install DESTDIR="${pkgdir}" || return 1

    # install rc script
    install -D -m 755 "${srcdir}/${pkgname}_rc.sh" "${pkgdir}/etc/rc.d/$pkgname"
}

