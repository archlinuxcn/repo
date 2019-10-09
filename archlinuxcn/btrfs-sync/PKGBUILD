#Maintainer: InvisibleRasta <nicolast88[at]gmail[dot]com>
pkgname=btrfs-sync
pkgver=16
pkgrel=1
pkgdesc="Smart and easy sync of BTRFS snapshots, locally or through SSH."
arch=('any')
url="https://github.com/nachoparker/btrfs-sync"
license=('GPL3')
source=("git+https://github.com/nachoparker/${pkgname}.git")
md5sums=('SKIP')
depends=('btrfs-progs')
optdepends=(
	'openssh: for openssh support.'
	'pv: allows a user to see the progress of data through a pipeline.'
	'pbzip2: parallel bzip2 file compression.'
)
pkgver() {
  cd "$srcdir/$pkgname"
  printf "$(git rev-list --count HEAD)"
}

package() {
  cd "$srcdir/$pkgname"
  install -Dm 755 ${pkgname} "$pkgdir/usr/bin/${pkgname}"
}
