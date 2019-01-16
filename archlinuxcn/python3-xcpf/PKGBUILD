#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2018.12
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2018.12.tar.xz
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2018.12.tar.xz.sig
)
sha512sums=(
  33a93c6b3adb5ebaf678159ad8d58314f26f7db2764b147024c61912f839148e00384c2ec79a7c1b884fc951e36c93537d6350affa6af170af0f23c11ed6fe30
  50071c1814606e446b704cedfed1f1bea637d8966f13065eb4ca0ba5f2e2ab8ebe82b2a824a40d0e8506e1acb6980e10804edf321f6e860d54a74e2b8ef85e3a
)
md5sums=(
  96fa5965a647784377c4c89219e98606
  988cc5f206cd6715abcf163e2904e5d0
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
