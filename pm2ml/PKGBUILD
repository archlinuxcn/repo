#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=pm2ml
pkgver=2015.12
pkgrel=1
pkgdesc='Generate metalinks for downloading Pacman packages and databases.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/pm2ml"
depends=(python3 pyalpm python3-xcpf)
optdepends=('reflector: Reflector support' 'aria2: ppl script support.' 'python3-aur: AUR support')
backup=(etc/ppl.conf)
source=(
  http://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2015.12.tar.xz
  http://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2015.12.tar.xz.sig
)
sha512sums=(
  6431fb0bfd14b9edf878a8b2dd2c441775cdd485c8cffc5aa7cc8ea38d25a45b2ef4fe38b30bc1d7cf755549f2afe9e5440241a89ba6aa7c030b9f09e797bc53
  a2fddfcfc91cdd03fa2db5e3a070e48c40a2c3bb990958785abcc461bce0b8c8a01063aadb3db54b9c834899ebfbb64ef04ae90a4ccc84bec078da6b9495906e
)
md5sums=(
  6e2ad58e74b5ec72a4d4f68181dc4f3c
  fb3da181b96045f29187ce92645a1fa4
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
