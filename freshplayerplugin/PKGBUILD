# Maintainer: WorMzy Tykashi <wormzy.tykashi@gmail.com>
# Contributor: Jack L. Frost <fbt@fleshless.org>
# Contributor: Corelli <corelli AT sent DOT com>
# Contributor: BartÅ‚omiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: intelfx <intelfx100 [at] gmail [dot] com>
# Contributor: Behem0th <grantipak@gmail.com> 
# Contributor: zman0900 <zman0900@gmail.com>

pkgname=freshplayerplugin
pkgver=0.3.9
pkgrel=2
pkgdesc='PPAPI-host NPAPI-plugin adapter.'
arch=('i686' 'x86_64')
url='https://github.com/i-rinat/freshplayerplugin'
license=('MIT')
depends=('alsa-lib' 'cairo' 'ffmpeg' 'freetype2' 'glib2' 'icu' 'jack'
         'libevent' 'libgl' 'libsoxr' 'libva' 'libvdpau' 'libx11'
         'libxcursor' 'libxrandr' 'libxrender' 'openssl' 'pango'
         'v4l-utils' 'pepper-flash')
makedepends=('libdrm' 'cmake' 'ragel')
source=(${pkgname}-${pkgver}.tar.gz::"${url}/archive/v${pkgver}.tar.gz"
        "use-AV-prefixed-macros.patch")
sha1sums=('fc7ba6b860a126de15a6f26c2835a437774161e0'
          '02bee874ade2aa8d679fd593618254e1b9f703c3')

prepare() {
  cd "${pkgname}-${pkgver}"
  patch -p1 -i "${srcdir}/use-AV-prefixed-macros.patch"
}

build() {
  cd "${pkgname}-${pkgver}"

  cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
  make
}

package() {
  cd "${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install

  install -Dm644 data/freshwrapper.conf.example "${pkgdir}/usr/share/${pkgname}/freshwrapper.conf.example"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
