#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2017.5
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2017.5.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2017.5.tar.xz.sig
)
sha512sums=(
  58199220df893c28551889431d1f6af6630600aefe7b7206615dcbd2444d1d845fd1d720eb0c5d524a8aa41ae14a90dcf942c6952ed58151dfd887f5132ebc37
  02582f804fe2f9d06ea9d189c7eb1d6ad6b380fc3370d01ec768cf5ddaf7de3fccf5ef499254c4d33cce6b242a1982518d398641ecfee2508b6e453a27b8aa5f
)
md5sums=(
  5570c2c5e2c00c45592569aa2db814cb
  1cb07afec6e920699d8206579111e668
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
