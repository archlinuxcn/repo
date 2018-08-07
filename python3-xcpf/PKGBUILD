#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2018.8
pkgrel=3
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2018.8.tar.xz
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2018.8.tar.xz.sig
)
sha512sums=(
  a30ac5fe6cd20ebcdfc9108457dc0cebf3535d0ca77add364ff54425165c7c6bff4ad2e1edc2d11585eeba84658dcbe9d15bbc6239169767cab44dc17973fd5b
  bd851394c208962bc1613b60e9a49fbc3e218e26f871d837e33dbdbf83b3fb7735e24cc6ba8b6fc474fa31ad05a5cf4767c29e8e296bb129cf07ea938bb6ef6c
)
md5sums=(
  be42efa0b26d7f528777ab34befb90f6
  1505694779a1687826fee320cd3d75a0
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
