#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcgf
pkgver=2016
pkgrel=1
pkgdesc='Xyne'"'"'s common generic functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcgf"
depends=(python3)
source=(
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2016.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2016.tar.xz.sig
)
sha512sums=(
  4eb3ad9ce7329661bf2649680fb1070ecce9df46ce692bd62a0031f776a5a6d876a14c0cef5e910c713eae1d05780a315fcb7ad11a3c51496e7dea599950a0fa
  6c6dc02430d4a2767424ccf431f8e2ebed4695d9b8832b33fc3ba73e1bbf3d41b2963c15784e3ef7ab30131c4608efde2f3a16631a01e69fef7d6fc8b639c64c
)
md5sums=(
  2e9c0d94a8507791cf1b7faf19674398
  83a728c6f6bc7ff5233088227bbeecbb
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
