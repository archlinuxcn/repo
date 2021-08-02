#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2021
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2021.tar.xz
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2021.tar.xz.sig
)
sha512sums=(
  7ab6f6cc646546e9bc46d7062c76dc4da140e8baa2a623322208cf2c8342b66017abead8cc9f5a72378c9b40aaac8239413113cce41038582b05fd47e4b63ea6
  e1ac903b538559eb1ee74a8fc8ccd3a6bd44234445f0c00c9eaaded534fec0ff7f1085898f885619a5394ac68af320c4db41167b146a9990e4541fd9292a8c65
)
md5sums=(
  f46b2d3c7d39992bb3c40c21ddc08435
  3505f2c716a0210014bc32c05f378668
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
