# Maintainer: graysky <graysky AT archlinux DOT us>

pkgname='profile-sync-daemon'
pkgver=6.32
pkgrel=2
pkgdesc='Syncs browser profiles to tmpfs reducing SSD/HDD calls and speeding-up browsers.'
arch=('any')
url='https://github.com/graysky2/profile-sync-daemon'
license=('MIT')
depends=('procps-ng' 'rsync' 'systemd' 'findutils')
conflicts=('firefox-sync' 'goanysync' 'go-anysync-git' 'iceweasel-sync'
'tmpfs-store' 'tmpfs-sync' 'user-profile-sync-daemon')
source=($pkgname-$pkgver.tar.gz::https://github.com/graysky2/$pkgname/archive/v$pkgver.tar.gz)
install=psd.install
sha256sums=('f61661f90259fcd0edd48d9f725290125674a08d743b860e5b2fcb3143a0c57d')

build() {
  cd "$pkgname-$pkgver"
  make
}

package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
  install -Dm644 MIT "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  rm -f "$pkgdir/usr/share/man/man1/psd-overlay-helper.1.gz"
}
