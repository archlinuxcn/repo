#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcgf
pkgver=2017
pkgrel=1
pkgdesc='Xyne'"'"'s common generic functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcgf"
depends=(python3)
source=(
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2017.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2017.tar.xz.sig
)
sha512sums=(
  fd0fe28ddc5450257483e8394549552e60c25266a6cfb33670e88b3cb31c2cd840628f3cf16a1b02c390e34ce5c45c09d0cc86434135948f4f2c8fb80ab7e46c
  7e1e4e62681ea483886497e0e6b7b58f6f6d817d823a373f9ec75799603169621696e7b565514eead4e2cea86d57002ffc78f82aceeda17cf22df7a1eb7f374e
)
md5sums=(
  37ef9d4a150e427d09312f1808ecc92a
  625b82d71091df346297ef75eea87ba3
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
