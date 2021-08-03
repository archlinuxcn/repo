#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=pm2ml
pkgver=2021.8
pkgrel=1
pkgdesc='Generate metalinks for downloading Pacman packages and databases.'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/pm2ml"
depends=(pyalpm python3 python3-xcgf python3-xcpf)
optdepends=('aria2: ppl script support.' 'python3-aur: AUR support' 'reflector: Reflector support')
backup=(etc/ppl.conf)
source=(
  https://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2021.8.tar.xz
  https://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2021.8.tar.xz.sig
)
sha512sums=(
  6a593adbdc19a9dd1d605225308bce059432cd6f3d8bd693da7f5d8bff030317a1782c3256ac9ed570eeae2c1f17bd06fd1eea385225dfef1d2309c2afc7c013
  be88634fcea925c7bf1493e2c5a70edf891953b6ae5fbda0bd681fa1a1c37a2685976366c315bd047794243dc99fc64a40fa81df1f49a6fa7412a0870a98b7bb
)
md5sums=(
  b12493ba6366a2f02d80a91900ae678f
  8261476347ab743ab1a0ca8ae08482cc
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
