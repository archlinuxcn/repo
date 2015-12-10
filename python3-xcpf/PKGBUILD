#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2015.12.10
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python3)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.12.10.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.12.10.tar.xz.sig
)
sha512sums=(
  c45764e067964b09688e174a9ce496bfc6b8bf16c6003956982b46db2e1a04ef3c2deff3b1dbd3ac7b27e0f056ceeb31c1a956fcef1e4a13a59adf78a0d06cf6
  99a9a8894f91015b41153e7ae24aa74cc2745d4686ebca8465d874e44f875abfcae7b4555afb2f2777a0c9a5735c1b007e6b99d7a558a798e728c4d7013ff8a2
)
md5sums=(
  13c65d7e99c3c44f32d1affa69606cc4
  6c2171afa73a9731af0db3f69bf2a81d
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
