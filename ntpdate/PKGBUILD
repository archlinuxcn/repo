# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: Sébastien Luttringer <seblu@aur.archlinux.org>

pkgname=ntpdate
_pkgname=ntp
_pkgver=4.2.8p1
pkgver=${_pkgver/p/.p}
pkgrel=1
pkgdesc='Client for the Network Time Protocol (NTP)'
url='http://www.ntp.org/'
license=('custom')
arch=('i686' 'x86_64')
makedepends=('perl-html-parser')
depends=('openssl')
conflicts=('ntp' 'ntpdate-dev')
backup=('etc/conf.d/ntpdate.conf')
source=("http://archive.ntp.org/ntp4/${_pkgname}-${_pkgver}.tar.gz"
        "${pkgname}.conf"
        "${pkgname}.service"
        "restore-html2man.patch")
sha256sums=('948274b88f1ed002d867ced6aaefdfd0999668b11285ac2b3a67ff2629d59d88'
            '1ddbf0f51e030c6ec48d50e1b0eb6682f2d51567fbbb8fdd695a0e38a6036fd7'
            '2267e19120de4a73703ed0d83a4a0088309600ce3fed88c3c17a950fa0c1aa85'
            '59571e06242a224c7cacaec7395b7fd25078ab469abb035ea0eb6fbecab8fd65')

prepare() {
  cd "${srcdir}/${_pkgname}-${_pkgver}"
  patch -p1 -i "../restore-html2man.patch"
  cp -f "scripts/deprecated/html2man.in" "scripts/"
}

build() {
  cd "${srcdir}/${_pkgname}-${_pkgver}"
  ./configure --prefix=/usr --libexecdir=/usr/lib
  make
  # Convert the html page to man page
  cd "html"
  "../scripts/html2man"
}

package() {
  install -m 755 -d "${pkgdir}/etc/conf.d"
  install -m 644 -t "${pkgdir}/etc/conf.d" "${pkgname}.conf"
  install -m 755 -d "${pkgdir}/usr/lib/systemd/system"
  install -m 644 -t "${pkgdir}/usr/lib/systemd/system" "${pkgname}.service"

  cd "${srcdir}/${_pkgname}-${_pkgver}"
  install -m 755 -d "${pkgdir}/usr/bin"
  install -m 755 -t "${pkgdir}/usr/bin" "${pkgname}/${pkgname}"
  install -m 755 -d "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" "COPYRIGHT"
  install -m 755 -d "${pkgdir}/usr/share/man/man1"
  install -m 644 -t "${pkgdir}/usr/share/man/man1" "html/man/man1/ntpdate.1"
}

