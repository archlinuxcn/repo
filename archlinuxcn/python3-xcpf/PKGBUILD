#Maintainer: Xyne <gro xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2021.12
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="https://xyne.dev/projects/python3-xcpf"
depends=(pyalpm python-pyxdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  https://xyne.dev/projects/python3-xcpf/src/python3-xcpf-2021.12.tar.xz
  https://xyne.dev/projects/python3-xcpf/src/python3-xcpf-2021.12.tar.xz.sig
)
sha512sums=(
  adbc0d3174a7ed9371266a9b6a5f979ae3b1fff48954077418b89f7b4da11c9b30179715ce6b7e3aa070db2779cc96620d07476ace53e9858bf95aa8e9fd61e9
  d2fa3e8ef6fcb182190997dc5bffc901aba876c3412e0248a58a9e07dc2b11d175c3ac025e165ffeb1154e4549a3549075b55621f82d3403f53db4c11dc4d084
)
md5sums=(
  9aa0bec60b5706d9e3c2bd45dd69091f
  67a251236244f3f26375b4d3539aa33c
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
