# Maintainer: graysky <graysky AT archlinux DOT us>

pkgname='anything-sync-daemon'
pkgver=5.83
pkgrel=1
pkgdesc='Offload anything to RAM (tmpfs) for speed and wear reduction.'
arch=('any')
url='https://github.com/graysky2/anything-sync-daemon'
license=('MIT')
depends=('procps-ng' 'rsync')
optdepends=('bash-completion: for tab completions under bash')
conflicts=('monitorix-sync-daemon' 'user-profile-sync-daemon' 'goanysync' 'goanysync-git' 'tmpfs-store' 'tmpfs-sync')
source=("http://repo-ck.com/source/$pkgname/$pkgname-$pkgver.tar.xz")
backup=('etc/asd.conf')
install=asd.install
sha256sums=('d8547cdd7e5bb3cba7ced89f40c86ea52d4a3e5dd740c625c46f5656fac46ea2')

build() {
  cd "$pkgname-$pkgver"
  make
}

package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install-systemd-all
  install -Dm644 MIT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
