# Maintainer: jason ryan <jasonwryan@gmail.com>
# Contributor:  Bartłomiej Piotrowski <nospam@bpiotrowwski.pl>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: evr <evanroman at gmail>
# Contributor: Luiz Ribeiro <luizribeiro@gmail.com>

pkgname=mpdscribble
pkgver=0.22
pkgrel=12
pkgdesc='MPD client which submits track info to {Libre,Last}.fm'
url='http://mpd.wikia.com/wiki/Client:Mpdscribble'
arch=('i686' 'x86_64' 'armv6h')
license=('GPL')
depends=('libsoup' 'glib2' 'libmpdclient')
install=$pkgname.install
source=(http://www.musicpd.org/download/${pkgname}/${pkgver}/${pkgname}-${pkgver}.tar.bz2
        service)
md5sums=('652ee927b797e9a4cef45494e77047db'
         'a57d7d3d41b37fb23b45835aa0cfc325')

prepare() {
  sed 's:multi-user.target:default.target:;:User=%i:d' service > user.service
}

build() {
  cd ${pkgname}-"${pkgver}"

  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --with-http-client=soup

  make
}

package() {
  cd ${pkgname}-"${pkgver}"

  make DESTDIR="${pkgdir}" install

  install -Dm644 "${srcdir}"/service \
    "${pkgdir}"/usr/lib/systemd/system/mpdscribble@.service
  install -Dm644 "${srcdir}"/user.service \
    "${pkgdir}"/usr/lib/systemd/user/mpdscribble.service

  # default config is really an example
  install -D -m644 "${pkgdir}"/etc/mpdscribble.conf \
    "${pkgdir}"/usr/share/mpdscribble/mpdscribble.conf.example
  rm -f "${pkgdir}"/etc/mpdscribble.conf

  install -d "${pkgdir}"/var/cache/mpdscribble
  touch "${pkgdir}"/var/cache/mpdscribble/mpdscribble.cache
}

# vim:set ts=2 sw=2 et:
