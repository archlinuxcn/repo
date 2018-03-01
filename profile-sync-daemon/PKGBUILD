# Maintainer: graysky <graysky AT archlinux DOT us>

pkgname='profile-sync-daemon'
pkgver=6.33
pkgrel=1
pkgdesc='Syncs browser profiles to tmpfs reducing SSD/HDD calls and speeding-up browsers.'
arch=('any')
url='https://github.com/graysky2/profile-sync-daemon'
license=('MIT')
depends=('procps-ng' 'rsync' 'systemd' 'findutils')
conflicts=('firefox-sync' 'goanysync' 'go-anysync-git' 'iceweasel-sync'
'tmpfs-store' 'tmpfs-sync' 'user-profile-sync-daemon')
source=($pkgname-$pkgver.tar.gz::https://github.com/graysky2/$pkgname/archive/v$pkgver.tar.gz)
install=psd.install
sha256sums=('ab76f310cbae28123dac12e7c415b08f4849ada1b1092bd063f57fbd7a28fa37')

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
