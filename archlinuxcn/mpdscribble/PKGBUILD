# Maintainer: jason ryan <jasonwryan@gmail.com>
# Contributor:  Bartłomiej Piotrowski <nospam@bpiotrowwski.pl>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: evr <evanroman at gmail>
# Contributor: Luiz Ribeiro <luizribeiro@gmail.com>

pkgname=mpdscribble
pkgver=0.25
pkgrel=1
pkgdesc='MPD client which submits track info to {Libre,Last}.fm'
url='https://www.musicpd.org/clients/mpdscribble/'
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
license=('GPL')
depends=('curl' 'libmpdclient')
makedepends=('boost' 'systemd' 'meson' 'ninja')
install="${pkgname}".install
source=(
  "https://www.musicpd.org/download/${pkgname}/${pkgver}/${pkgname}-${pkgver}.tar.xz"{,.sig}
  )
validpgpkeys=('0392335A78083894A4301C43236E8A58C6DB4512') # Max Kellermann <max@musicpd.org>
sha256sums=('20f89d945bf517c4d68bf77a77a359fdb13842ab1295e8d21eda79be2b5b35ce'
            'SKIP')

prepare() {
  cd "${pkgname}"-"${pkgver}"
  DESTDIR="${pkgdir}" meson build \
     --prefix=/usr \
     --sysconfdir=/etc
}

build() {
  cd "${pkgname}"-"${pkgver}"
  DESTDIR="${pkgdir}" meson build \
  --prefix=/usr \
  --buildtype=plain
  meson compile -C build
}

package() {
  cd "${pkgname}"-"${pkgver}"
  DESTDIR="${pkgdir}" meson install -C build

  install -Dm644 build/systemd/system/"${pkgname}".service \
    "${pkgdir}"/usr/lib/systemd/system/"${pkgname}"@.service
  install -Dm644 build/systemd/user/"${pkgname}".service \
    "${pkgdir}"/usr/lib/systemd/user/"${pkgname}".service

  # example config
  install -Dm644 doc/"${pkgname}".conf \
    "${pkgdir}"/usr/share/"${pkgname}"/"${pkgname}".conf.example
  rm -r "${pkgdir}"/etc

  install -d "${pkgdir}"/var/cache/"${pkgname}"
    touch "${pkgdir}"/var/cache/"${pkgname}"/"${pkgname}".cache
}

# vim:set ts=2 sw=2 et:
