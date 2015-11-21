#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2015.11.21
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(python3 pyalpm)
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.11.21.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2015.11.21.tar.xz.sig
)
sha512sums=(
  6ce813857d26568a1ba8de81ab59ff5312b7089391f969ecf5beb102208b2d97fe4d269e8cb2b45c252f15405c02d352ec4f41540c32701c6a088f439879bb45
  ddbd9698cf12ee4197370d5f5a7a98916b4cd24406d5d64404ebdc02b94113ab3ed4a1422eff6ec3f2d9f248878c8127c54a352811931c091bfa3d089dbaf792
)
md5sums=(
  acc032d3711b293b1526654f73cdd148
  69fd3ac626d7f6af2486268ff4edbc44
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
