# Maintainer: Peter Cai <peter@typeblog.net>

_commit=350939b8d2e95ed1be352f1ac734bdedf14e43c7 # Commit in PeterCxy/evdev-right-click-emulation
_date=20190313 # Update this with the commit ID
pkgname=evdev-right-click-emulation
pkgver=${_date}.${_commit:0:6}
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
          '38286fe398788a9909a98eb4c57c4444f8599c54'
          '47fd73fbd6a5c36932567ad11ac14246868b0d14')
backup=("etc/evdev-rce.conf")

build() {
  cd ${srcdir}/${pkgname}
  make all
}

package() {
  install -D -m755 ${srcdir}/${pkgname}/out/evdev-rce -t ${pkgdir}/usr/bin/
  install -D -m644 ${srcdir}/evdev-rce.conf -t ${pkgdir}/etc/
  install -D -m644 ${srcdir}/evdev-rce.service -t ${pkgdir}/usr/lib/systemd/system/
}
