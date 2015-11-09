#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=pm2ml
pkgver=2015.11.9
pkgrel=1
pkgdesc='Generate metalinks for downloading Pacman packages and databases.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/pm2ml"
depends=(python3 pyalpm python3-xcpf)
optdepends=('aria2: ppl script support.' 'reflector: Reflector support' 'python3-aur: AUR support')
backup=(etc/ppl.conf)
source=(
  http://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2015.11.9.tar.xz
  http://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2015.11.9.tar.xz.sig
)
sha512sums=(
  d91a087330498f26758acad2fa82ae2fd74241948cd19a707acb4482c9881f474af4833280fe43f117a0550463cd07a6514e2bbb2c3cda701daebf43b730b393
  0600fe695a6449c1735cb2f0f89321cd59530a5a767948c64450c4b190c9fb5183e9d7c9a9a052aefc491e688675d5fd1c0888856ee6a6717fee3e7f93f83c18
)
md5sums=(
  2f65ff8f1cce67fc7ad155ab930646d1
  803d06a86de6463981d46d8813035bfc
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
