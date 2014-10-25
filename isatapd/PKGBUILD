# Contributor: Philanecros Heliostein <philanecros@gmail.com>
# Maintainer: xgdgsc<xgdgsc@gmail.com>

pkgname="isatapd"
pkgver="0.9.7"
pkgrel=3
pkgdesc="Creates and maintains an ISATAP tunnel (rfc5214) in Linux."
arch=("i686" "x86_64")
url="http://www.saschahlusiak.de/linux/isatap.htm"
license=('GPL')
conflicts=('')
source=("http://www.saschahlusiak.de/linux/${pkgname}-${pkgver}.tar.gz" "isatapd@.service")
md5sums=("79f13a360b9a14cb0afcdf7a2af9c6de" "ea68b108ceac25c5b07dc14780ed1f53")

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure --prefix=/usr
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}/" install || return 1
  mkdir -p "${pkgdir}/usr/lib/systemd/system"
  install -m644 "${srcdir}/${pkgname}@.service" "${pkgdir}/usr/lib/systemd/system"
  mkdir -p "${pkgdir}"/usr/bin
  mv "${pkgdir}"/usr/sbin/isatapd "${pkgdir}"/usr/bin/
  rm -rf "${pkgdir}"/usr/sbin/
}
