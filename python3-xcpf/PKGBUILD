#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2017.7
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2017.7.tar.xz
  http://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2017.7.tar.xz.sig
)
sha512sums=(
  daeb784c2b9eef61d685f20c3a2a49240bc887fb7dd25983064b53ed3341aed8de72ea93e5aa3c71846e3d48e00895d1acf417e0f31e21c9a466ece7a3fa4d90
  d4c76f3eec5a1b09bbae9991a508f3237a8cea83085e5298794b5a2bddecd08f086812c4da8c8166fd5afde265103afd78030a86b95115c6e252be9bd1eb2f29
)
md5sums=(
  3d9344bffe00e8dd966e9e830a431575
  f033a2897e01995f8753ffbb290d7095
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
