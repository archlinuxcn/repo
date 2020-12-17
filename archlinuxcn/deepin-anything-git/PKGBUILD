# Maintainer: DingYuan Zhang <justforlxz@gmail.com>

pkgbase=deepin-anything-git
pkgname=(deepin-anything-git deepin-anything-dkms-git)
pkgver=0.1.0.r4.g1340200
_extramodules=extramodules-ARCH
pkgrel=4
pkgdesc="Deepin Anything file search tool"
arch=('x86_64')
url="https://github.com/linuxdeepin/deepin-anything"
license=('GPL3')
makedepends=('git' 'dtkcore-git' 'udisks2-qt5')
source=("$pkgbase::git://github.com/linuxdeepin/deepin-anything"
        deepin-anything-server.sysusers)
sha512sums=('SKIP'
            '0ff6a6de1fbfb0c33eaac511b989da321a9e43ece92708af88aee34ad1a05e55572713b1290bc2705d70b91dc7bec4fb4abd3dc664a0abe01de27d88bd9e9c85')

pkgver() {
    cd $pkgbase
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd $pkgbase
  sed -i 's|^systemd_service.path.*|systemd_service.path = /usr/lib/systemd/system|' server/monitor/src/src.pro server/tool/tool.pro
}

build() {
	cd $pkgbase
  make VERSION=$pkgver
}

package_deepin-anything-dkms-git() {
  depends=('dkms')
  provides=('DEEPIN-ANYTHING-MODULE' 'deepin-anything')
  conflicts=('DEEPIN-ANYTHING-MODULE' 'deepin-anything')

  cd $pkgbase
  install -dm 755 "$pkgdir"/usr/src
  cp -r kernelmod "$pkgdir"/usr/src/deepin-anything-$pkgver
  install -m644 debian/deepin-anything-dkms.dkms "$pkgdir"/usr/src/deepin-anything-$pkgver/dkms.conf
}

package_deepin-anything-git() {
  depends=('DEEPIN-ANYTHING-MODULE' 'dtkcore-git' 'udisks2-qt5')
  groups=('deepin-git')

  cd $pkgbase
  make VERSION=$pkgver DESTDIR="$pkgdir" install
  rm -r "$pkgdir"/usr/src

  mv "$pkgdir"/etc/dbus-1/system.d "$pkgdir"/usr/share/dbus-1/system.d

  install -Dm644 ../deepin-anything-server.sysusers "$pkgdir/usr/lib/sysusers.d/deepin-anything-server.conf"
}
