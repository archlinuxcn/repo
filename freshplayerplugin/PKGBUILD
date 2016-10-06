# Maintainer: Jack L. Frost <fbt@fleshless.org>
# vim: expandtab sts=2
# Contributor: Corelli <corelli AT sent DOT com>
# Contributor: BartÅ‚omiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: intelfx <intelfx100 [at] gmail [dot] com>
# Contributor: Behem0th <grantipak@gmail.com> 
# Contributor: zman0900 <zman0900@gmail.com>

pkgname=freshplayerplugin
pkgver=0.3.6
pkgrel=1
pkgdesc='PPAPI-host NPAPI-plugin adapter.'
arch=( 'i686' 'x86_64' )
url='https://github.com/i-rinat/freshplayerplugin'
license=( 'MIT' )
depends=( 'pango' 'alsa-lib' 'freetype2' 'libevent' 'gtk3' 'libgl' 'v4l-utils' 'ffmpeg' 'icu' )
makedepends=( 'cmake' 'ragel' )
conflicts=( 'freshplayerplugin-git' )
install="${pkgname}.install"

source=(
  "${url}/archive/v${pkgver}.tar.gz"
  "${pkgname}.install"
)

optdepends=(
  'pepper-flash: for the necessary Pepper plugin'
)

build() {
  cd "${pkgname}-${pkgver}"

  cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DWITH_GTK=3
  make
}

package() {
  cd "${pkgname}-${pkgver}"

  make DESTDIR="${pkgdir}" install

  install -Dm644 data/freshwrapper.conf.example "${pkgdir}/usr/share/${pkgname}/freshwrapper.conf.example"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

sha1sums=('255dc4ad0dbad26ed92e1b7dbdd615e75096b05f'
          '331a3b3877249eaf1c3db917bde1dea6c4d374ab')
