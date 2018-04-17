#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2018
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2018.tar.xz
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2018.tar.xz.sig
)
sha512sums=(
  a1c7a58ad6f8578361e07b52c41ff4a3d818648c4f325d02b512e4318f8972c46486a71d491025704361cf5bca932e96048ed30030a6bcc8f8c6d6a5fce13636
  b2fca71262b10b0c5c02b1325cf3fd9b7bfd544cdce613520e189aed44c88d1ab06408fb9ae2ca55f91028e895481660b2a76b86dd26b4eec3f4a27871888878
)
md5sums=(
  2afbb9dd0458a9e35259f6266dd859e2
  6d549460cb243036bf547c3af8c729db
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
