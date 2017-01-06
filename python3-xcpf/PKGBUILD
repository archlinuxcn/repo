#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2017
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2017.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2017.tar.xz.sig
)
sha512sums=(
  e9896bd58232ad4664ac238c43d6939cc7f3385958c26b0e3cfadf9fb382e7e1c6c28097c6fe8d8dd5a8107012e13b3f2e609bbd7a70dfff24d283840856a28f
  c9507152e1d2b66a5560a7a82404c23a5d1f4731cf1b826a69f33068de063f4571defc301046b52becc18ecbc05510d1c68916ef0c63cf4059f96e98a900b1ac
)
md5sums=(
  52fc784491685654fb5b6312d0e7aa63
  56e632b46210fbd2a0b60c055634d999
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
