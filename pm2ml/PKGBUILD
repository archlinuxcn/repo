#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=pm2ml
pkgver=2015.10.16
pkgrel=1
pkgdesc='Generate metalinks for downloading Pacman packages and databases.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/pm2ml"
depends=(python3 pyalpm python3-xcpf)
optdepends=('reflector: Reflector support' 'python3-aur: AUR support' 'aria2: ppl script support.')
backup=(etc/ppl.conf)
source=(
  http://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2015.10.16.tar.xz
  http://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2015.10.16.tar.xz.sig
)
sha512sums=(
  670ce0d62f9ab69cceb8c44b8539e1e5f38fa0e989f559728c46dfafb3da3e818700d8cbcd960e0db94a9dfeea85123dab2e3ebcca6c64f99b11dc360b51d657
  08841e44dd30ed5589748a43ea6c897cc630252b40c52dd3954c3d4a7d91db2c3e53d499bd65d87a7f5e15756af8924998cefb8d0e126b4951dc97bd2efe93a1
)
md5sums=(
  887f9f037f67602fcd42e3e6d8c3c7ab
  4fc009a1f037ab9a65a1252f5c3226e8
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
