# Maintainer: Wellington <wellingtonwallace@gmail.com>
pkgname=pulseeffects
pkgver=4.3.1
pkgrel=1
pkgdesc="Audio Effects for Pulseaudio Applications"
arch=(any)
url="https://github.com/wwmm/pulseeffects"
license=('GPL3')
depends=(gtk3 gtkmm3 glibmm libpulse gstreamer gst-plugins-good gst-plugins-bad
        lilv boost-libs libsigc++ libsndfile libsamplerate zita-convolver
        libebur128)
optdepends=('calf: limiter, compressor exciter, bass enhancer and others'
            'zam-plugins: maximizer'
            'rubberband: pitch shifting'
            'mda.lv2: loudness')
makedepends=('meson' 'boost' 'itstool')
options=(!emptydirs)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/wwmm/pulseeffects/archive/v$pkgver.tar.gz")
sha256sums=('78c0a69d0959fb42e0982fba6f8e5c02cdb2ad41b8475e2a863b83428f7b4c07')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  # Remove any potential residual build files
  rm -rf _build
  meson _build --prefix=/usr --buildtype=release
}

package() {
  cd "$srcdir/$pkgname-$pkgver/_build"
  env DESTDIR="$pkgdir" ninja install
}

# vim:set ts=2 sw=2 et:
