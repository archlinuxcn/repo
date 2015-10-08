#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2015.10.6
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(python3 pyalpm)
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.10.6.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.10.6.tar.xz.sig
)
sha512sums=(
  ca6e0126451ad8160c9a63c4341783f095d0109ac466b08c3f7a25a0d78d1d653a0e4e9b4d345a210f784cf6d1fd4d115b820af5a40873f2b5e1540f23699922
  4d435d86042a27004c40ef112205ffa3f1e6eebf6e6587c07960a723cafc99b7d22d1c152e1888c19c1848feb2b59566aeb33fbfbb7ea19695a27344fcf1b470
)
md5sums=(
  f438ea980db92cb498d4f61ddec92edb
  6e32f1eb14163c05035d8ea725b4c6a4
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
