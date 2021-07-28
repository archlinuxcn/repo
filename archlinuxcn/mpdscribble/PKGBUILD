# Maintainer: jason ryan <jasonwryan@gmail.com>
# Contributor:  Bartłomiej Piotrowski <nospam@bpiotrowwski.pl>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: evr <evanroman at gmail>
# Contributor: Luiz Ribeiro <luizribeiro@gmail.com>

pkgname=mpdscribble
pkgver=0.23
pkgrel=5
pkgdesc='MPD client which submits track info to {Libre,Last}.fm'
url='https://www.musicpd.org/clients/mpdscribble/'
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
license=('GPL')
depends=('curl' 'libmpdclient')
makedepends=('boost' 'systemd' 'meson' 'ninja')
install=$pkgname.install
source=("https://www.musicpd.org/download/${pkgname}/${pkgver}/${pkgname}-${pkgver}.tar.xz"{,.sig})
validpgpkeys=('0392335A78083894A4301C43236E8A58C6DB4512') # Max Kellermann <max@musicpd.org>
sha256sums=('a3387ed9140eb2fca1ccaf9f9d2d9b5a6326a72c9bcd4119429790c534fec668'
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
  cd ${pkgname}-"${pkgver}"
  DESTDIR="${pkgdir}" meson install -C build

  install -Dm644 build/systemd/system/mpdscribble.service \
    "${pkgdir}"/usr/lib/systemd/system/mpdscribble@.service
  install -Dm644 build/systemd/user/mpdscribble.service \
    "${pkgdir}"/usr/lib/systemd/user/mpdscribble.service

  # example config
  install -Dm644 doc/mpdscribble.conf \
    "${pkgdir}"/usr/share/mpdscribble/mpdscribble.conf.example
  rm -r "${pkgdir}"/etc

  install -d "${pkgdir}"/var/cache/mpdscribble
    touch "${pkgdir}"/var/cache/mpdscribble/mpdscribble.cache
}

# vim:set ts=2 sw=2 et:
