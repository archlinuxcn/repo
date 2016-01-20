#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2016
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2016.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2016.tar.xz.sig
)
sha512sums=(
  4f6bdc9b1b5a969aff318bf0c17580f959e928e4396917b22c2fb48d159ee3df01998704a3e124f6c9a911bb9274796e64047fbf1c493ce36e9f56ca7921af8d
  8eb433404fa33a6e640f6ef716a709959c65be701a111e93df5adf4e6516364e7bf6543e41bb074c982a92ef607536c20c9e235206ff3d8ecc4ab66e5b3e25af
)
md5sums=(
  175abf4e843f3077d33ecb8726ca34a9
  db8446db6e09e2c09cf170eccd8aaa1c
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
