# Maintainer: graysky <graysky AT archlinux DOT us>

pkgname='profile-sync-daemon'
pkgver=6.34
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
sha256sums=('aad8f134738bac025b1d12aa175858e99690775eca5c277070b08ecdddfbde6c')

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
