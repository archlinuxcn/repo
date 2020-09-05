# Maintainer: jason ryan <jasonwryan@gmail.com>
# Contributor:  Bartłomiej Piotrowski <nospam@bpiotrowwski.pl>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: evr <evanroman at gmail>
# Contributor: Luiz Ribeiro <luizribeiro@gmail.com>

pkgname=mpdscribble
pkgver=0.23
pkgrel=1
pkgdesc='MPD client which submits track info to {Libre,Last}.fm'
url='https://github.com/MusicPlayerDaemon/mpdscribble'
arch=('any')
license=('GPL')
depends=('boost' 'libmpdclient')
makedepends=('meson' 'ninja')
install=$pkgname.install
source=(https://github.com/MusicPlayerDaemon/${pkgname}/archive/v${pkgver}.tar.gz
        service)
md5sums=('6b3b325c82f6b6eff38123960d7d91dc'
         'a57d7d3d41b37fb23b45835aa0cfc325')

prepare() {
  sed 's/multi-user.target/default.target/;/User=%i/d' service > user.service

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

  install -Dm644 systemd/system/mpdscribble.service.in \
    "${pkgdir}"/usr/lib/systemd/system/mpdscribble@.service
  install -Dm644 systemd/user/mpdscribble.service.in \
    "${pkgdir}"/usr/lib/systemd/user/mpdscribble.service

  # default config is really an example
  install -Dm644 doc/mpdscribble.conf \
    "${pkgdir}"/usr/share/mpdscribble/mpdscribble.conf.example
  rm -f "${pkgdir}"/etc/mpdscribble.conf
}

# vim:set ts=2 sw=2 et:
