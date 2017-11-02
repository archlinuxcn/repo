#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2017.11.1
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2017.11.1.tar.xz
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2017.11.1.tar.xz.sig
)
sha512sums=(
  b8ba9a98ef4e3bad63eb2ed28cccbb1caef1ad031e488462df2ed921f4cd5da5ac79faaa1ac27fe46a89847d8c7fd33d90dea12a4314763406f877d0396e8677
  19ab14acffffebff0d14bdce4dc4a616d1aedb85ffad9849ad8ab16fccb0bf900a716625fe8f3fee17e38db291afbc3daeb7bc22ac1a9977f9dcc98a04ca2a7d
)
md5sums=(
  e69370043bad6d09a7b78dec936149bb
  79c22167840ce7b5af24ca9bd6646c2d
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
