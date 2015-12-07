#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcgf
pkgver=2015.12
pkgrel=1
pkgdesc='Xyne'"'"'s common generic functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcgf"
depends=(python3)
source=(
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2015.12.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcgf/src/python3-xcgf-2015.12.tar.xz.sig
)
sha512sums=(
  38b0caffe58383f8fa8f258e69ceea636c24b47cda71a0855fc01b3f7dc32d0e0f5e2da4fe461f385653d5d169542e0af3e754bb197ec29021f0a4d065f58c61
  0255c40c6c078f6437923a6a86a3e7bfc9b92ddedded7cb0341f233f64b246b56095777e6187e3528a4d5b767ef62ef9b9fc522675b7ac05e7d450bce01cd90e
)
md5sums=(
  12fb01bc514f5766f226c1ebbcd9ccac
  6eef4efb355188c832cc6e72a09c37b6
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
