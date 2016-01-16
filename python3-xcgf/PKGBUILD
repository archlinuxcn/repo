#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcgf
pkgver=2016.1
pkgrel=1
pkgdesc='Xyne'"'"'s common generic functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcgf"
depends=(python3)
source=(
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2016.1.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2016.1.tar.xz.sig
)
sha512sums=(
  4d86be832673983a839aae5bcac7315857149c7af3171192028c7ba6aba62269ecc891023d50aaa2ce863630429464acca08c39dd77e175b9f35d6721a9f344c
  413c1c7a698cfde9345005e008c5242417c4e53d9cc042563afd70801107d55e91596e8358f9bc0d52541389821f16221c127c3ce5eb9f8cf2f3a5fb3f8276bd
)
md5sums=(
  70bb25ddf31bc0c37901349e75deead4
  ec474312517d478ebf508fb172baebc7
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
