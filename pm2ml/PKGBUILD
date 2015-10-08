#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=pm2ml
pkgver=2015
pkgrel=1
pkgdesc='Generate metalinks for downloading Pacman packages and databases.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/pm2ml"
depends=(python3 pyalpm python3-xcpf)
optdepends=('aria2: ppl script support.' 'reflector: Reflector support' 'python3-aur: AUR support')
backup=(etc/ppl.conf)
source=(
  http://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2015.tar.xz
  http://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2015.tar.xz.sig
)
sha512sums=(
  4e0156530dbca0445467d9dbe735a212f63270633d55bc4a90fbe178ada1f1fb5bdcca96bd2670e49af5d524857260f2eaddf1e45a2c810341f9936a302d2a65
  19e6aa18e4c1b2c1415b9955f7e5fa30eb3dd9bc1ecf6b2471abdac17490c428759a6508c11cfacf685da4a5207508b386d1f66dad1a2441209ae390564b0c80
)
md5sums=(
  bd539b69766524c51e405da7e9ed58d3
  fb3aa1014501e29236fc6fb2b9312af0
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
