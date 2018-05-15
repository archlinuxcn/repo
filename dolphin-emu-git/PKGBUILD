# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Lightning <sgsdxzy@gmail.com>

pkgbase=dolphin-emu-git
pkgname=('dolphin-emu-git' 'dolphin-emu-cli-git' 'dolphin-emu-wx-git')
pkgver=5.0.r7139.ad836b9071
pkgrel=1
pkgdesc='A GameCube / Wii / Triforce emulator'
arch=('x86_64')
url='http://www.dolphin-emu.org/'
license=('GPL')
depends=('alsa-lib' 'bluez-libs' 'enet' 'gcc-libs' 'gdk-pixbuf2' 'glib2'
         'glibc' 'hidapi' 'libevdev' 'libgl' 'libpng' 'libpulse' 'libsm'
         'libx11' 'libxi' 'libxrandr' 'libxxf86vm' 'lzo' 'mbedtls' 'miniupnpc'
         'qt5-base' 'sfml' 'zlib'
         'libavcodec.so' 'libavformat.so' 'libavutil.so' 'libcurl.so'
         'libswscale.so' 'libudev.so' 'libusb-1.0.so')
makedepends=('cairo' 'cmake' 'git' 'gtk2' 'pango')
optdepends=('pulseaudio: PulseAudio backend')
options=('!emptydirs')
source=('dolphin-emu::git+https://github.com/dolphin-emu/dolphin.git')
sha256sums=('SKIP')

pkgver() {
  cd dolphin-emu

  git describe | sed 's/-/.r/; s/-g/./'
}

prepare() {
  cd dolphin-emu

  if [[ -d build ]]; then
    rm -rf build
  fi
  mkdir build
}

build() {
  cd dolphin-emu/build

  cmake .. \
    -DCMAKE_INSTALL_PREFIX='/usr' \
    -DENABLE_QT2='TRUE' \
    -DUSE_SHARED_ENET='TRUE' \
    -DDISTRIBUTOR='aur.archlinux.org'
  make
}

package_dolphin-emu-git() {
  provides=('dolphin-emu')
  conflicts=('dolphin-emu')

  cd dolphin-emu/build

  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/bin/dolphin-emu-{nogui,wx}

  install -Dm 644 ../Data/51-usb-device.rules -t "${pkgdir}"/usr/lib/udev/rules.d/
}

package_dolphin-emu-cli-git() {
  depends=('dolphin-emu-git')

  cd dolphin-emu/build

  install -dm 755 "${pkgdir}"/usr/bin
  install -m 755 Binaries/dolphin-emu-nogui "${pkgdir}"/usr/bin/dolphin-emu-cli
}

package_dolphin-emu-wx-git() {
  depends=('cairo' 'dolphin-emu-git' 'gtk2' 'pango')

  cd dolphin-emu/build

  install -dm 755 "${pkgdir}"/usr/bin
  install -m 755 Binaries/dolphin-emu-wx "${pkgdir}"/usr/bin/
}

# vim: ts=2 sw=2 et:
