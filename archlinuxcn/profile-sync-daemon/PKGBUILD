# Maintainer: graysky <graysky AT archlinux DOT us>

pkgname='profile-sync-daemon'
pkgver=6.35
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
sha256sums=('1b38fd65b4f54f58640d94f67a28a525018158818b22b65fc164dbe4a064a341')

build() {
  cd "$pkgname-$pkgver"
  make
}

package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
  install -Dm644 MIT "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
