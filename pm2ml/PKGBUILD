#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=pm2ml
pkgver=2015.11.15
pkgrel=1
pkgdesc='Generate metalinks for downloading Pacman packages and databases.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/pm2ml"
depends=(python3 pyalpm python3-xcpf)
optdepends=('reflector: Reflector support' 'python3-aur: AUR support' 'aria2: ppl script support.')
backup=(etc/ppl.conf)
source=(
  http://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2015.11.15.tar.xz
  http://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2015.11.15.tar.xz.sig
)
sha512sums=(
  ebb8664ecbb343edfca3ee91cc94bceddfe6d3c7eb52d7dd3ba664e8427ee7363e7cb6ff959479872760b4e716c291bc2e2c2f0c0c67ac73a652b4942f7a2d56
  9b78b61690728ce73f94fea602a7c6ce399803f98f218d1085f3aec68da07387fa5342589c980401bc17f00485e76f8b15ff5a9539970eaae7593bbeb86fd9c1
)
md5sums=(
  029365f6c3cbb9e25b70569cfe10a414
  36a53d9a16e8b7cd4f4beceedff1b444
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
  install -Dm755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
  for foo_ in ppl pplsyu ppls; do
    install -Dm755 "$foo_" "$pkgdir/usr/bin/$foo_"
  done
  install -Dm644 "ppl.conf" "$pkgdir/etc/ppl.conf"
}

# vim: set ts=2 sw=2 et:
