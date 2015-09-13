# Maintainer: Jack L. Frost <fbt@fleshless.org>
# vim: expandtab sts=2
# Contributor: Corelli <corelli AT sent DOT com>
# Contributor: BartÅ‚omiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: intelfx <intelfx100 [at] gmail [dot] com>
# Contributor: Behem0th <grantipak@gmail.com> 

pkgname=freshplayerplugin
pkgver=0.3.2
pkgrel=1
pkgdesc='PPAPI-host NPAPI-plugin adapter.'
arch=( 'i686' 'x86_64' )
url='https://github.com/i-rinat/freshplayerplugin'
license=( 'MIT' )
depends=( 'pango' 'alsa-lib' 'freetype2' 'libconfig' 'libevent' 'gtk2' 'libgl' 'v4l-utils' 'ffmpeg' )
makedepends=( 'cmake' 'ragel' )
conflicts=( 'freshplayerplugin-git' )
install="${pkgname}.install"

source=(
  "${url}/archive/v${pkgver}.tar.gz"
  "${pkgname}.install"
)

optdepends=(
  'chromium-pepper-flash: for the necessary Pepper plugin'
  'chromium-pepper-flash-standalone: for the necessary Pepper plugin'
  'google-chrome: for the necessary Pepper plugin'
  'google-chrome-beta: for the necessary Pepper plugin'
  'google-chrome-dev: for the necessary Pepper plugin'
)

build() {
  cd "${pkgname}-${pkgver}"
  cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
  make
}

package() {
  cd "${pkgname}-${pkgver}"
  install -d "${pkgdir}/usr/lib/mozilla/plugins"
  install -m644 libfreshwrapper-*.so "${pkgdir}/usr/lib/mozilla/plugins"
  install -Dm644 data/freshwrapper.conf.example "${pkgdir}/usr/share/${pkgname}/freshwrapper.conf.example"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

sha1sums=('eb8062e5f2d9e99792cd374182b4f9c26fe84ed5'
          '331a3b3877249eaf1c3db917bde1dea6c4d374ab')
