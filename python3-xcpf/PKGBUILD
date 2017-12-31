#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2017.12
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2017.12.tar.xz
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2017.12.tar.xz.sig
)
sha512sums=(
  4ce2fdfd84f39122b0b7248de05cadf582df8bc3b3aa56fa2ee965c1a97eba2428f5d572a09c6d7e28f0a0fda61917fb8658325433091e1024e234b841379a5a
  636796e4a1e5aae2c1a7e1f9cfd2255b7e27d7b3a4286c018b0f0995fe051ba8c48c0ea156e67ca9fa1bff504a2bd2d042468ff4cdd4c8211cf1fe5b0660df2f
)
md5sums=(
  18f5923da9f1c37ae9331c4685e606e4
  d1f45a564e006ec7ebd710506e1b2670
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
