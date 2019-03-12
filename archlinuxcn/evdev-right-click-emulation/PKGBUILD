# Maintainer: Peter Cai <peter@typeblog.net>

_commit=0ce9a594ea8f97b5eff77cd14642340aa40791df # Commit in PeterCxy/evdev-right-click-emulation
_date=20190312 # Update this with the commit ID
pkgname=evdev-right-click-emulation
pkgver=20190312.${_commit:0:6}
pkgrel=1
pkgdesc="Implement Long-Press-to-Right-Click on Touchscreen Linux Device with Xorg or Wayland"
arch=(x86_64)
license=('WTFPL')
depends=(libevdev)
makedepends=(gcc make git)
url='https://git.angry.im/PeterCxy/evdev-right-click-emulation'
install=$pkgname.install
source=(
  "${pkgname}::git+https://git.angry.im/PeterCxy/evdev-right-click-emulation#commit=${_commit}"
  "evdev-rce.conf"
  "evdev-rce.service"
)
sha1sums=('SKIP'
          'd2fe3eaca1d47f416fb93d9472f17f81b48cba41'
          '6c6cd2a3610bc20760fcd3ef43e49c9d0455ec12')

build() {
  cd ${srcdir}/${pkgname}
  make all
}

package() {
  install -D -m755 ${srcdir}/${pkgname}/out/evdev-rce -t ${pkgdir}/usr/bin/
  install -D -m644 ${srcdir}/evdev-rce.conf -t ${pkgdir}/etc/
  install -D -m644 ${srcdir}/evdev-rce.service -t ${pkgdir}/usr/lib/systemd/system/
}
