#Maintainer: Xyne <gro xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2021.12
pkgrel=3
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
  0e8f0a2b64c6ad6326ecadb8e4c30420fd8d22ffe149ed0548cb6ceec8619acaf9f15b5cb485fc2e96e436eee29b45775b8187e9c7828157ffae967b9e9040bf
)
md5sums=(
  9aa0bec60b5706d9e3c2bd45dd69091f
  4fe01a5258f5bc39058f8803a7a918c3
)
validpgpkeys=('D89FAAEB4CECAFD199A2F5E612C6F735F7A9A519')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
