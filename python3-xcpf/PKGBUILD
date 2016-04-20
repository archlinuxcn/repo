#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2016.4.5.2
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2016.4.5.2.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2016.4.5.2.tar.xz.sig
)
sha512sums=(
  4a8843397c49543be22cec9eb3b1bd17b91f468148a6bd94f7f7d04cb3e040234938982518d8ca7e4e8e0c2e8663af5cc65507997d7b6f3b96128a61beb28fa2
  ee9220b181c1b04795db095f4c7d66b93f18ab317162403879802328507bba0b8b29f8fbc03e215f65928228c9b88ff6823d41ac7a005689c1d9cc469f330055
)
md5sums=(
  ad195d947d6f7de23298446cb244bc8b
  d431dfc8a3b5a284f42c559a9caa1293
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
