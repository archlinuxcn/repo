#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2016.4.5.3
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2016.4.5.3.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2016.4.5.3.tar.xz.sig
)
sha512sums=(
  f89e3d047854b490163b9005717964bb14e3ddfc85eb8fa8269d927fdd7ef79f761b4d96d4ebfee2b80c82db058d4cb20cd732e6616ffef3b34bc23358a25a8f
  43cc2bc7bdfdac07cbd2ec767e7a961853eb20644691978d7f02cbbf47d3c3f0f8f11820c9e4850c696547fb91c4c4dbf37904fc9ee2adadc090827b9433296f
)
md5sums=(
  3c8d82e61cd7e2bb994256f76657f60f
  8885d640ffcde7ea84f086679223d862
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
