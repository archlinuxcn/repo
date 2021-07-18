#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=pm2ml
pkgver=2021
pkgrel=1
pkgdesc='Generate metalinks for downloading Pacman packages and databases.'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/pm2ml"
depends=(pyalpm python3 python3-xcgf python3-xcpf)
optdepends=('aria2: ppl script support.' 'python3-aur: AUR support' 'reflector: Reflector support')
backup=(etc/ppl.conf)
source=(
  https://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2021.tar.xz
  https://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2021.tar.xz.sig
)
sha512sums=(
  4b1a71bf9c3ddfbff31eb9281ef26b7621af016affee5093bd287af7b040e3a17d5f47def85e2e271bbe3517056b620264e32df44fff47377936a1b55c987f95
  3fffbcf71dea1de40bee51072dc4c47c6bc29be41dad5adb73c2c4dd773b156f8e152e59c7d9cd814607bb38bf4d2a95d16ad5457cb8a38cb41024e49728c5eb
)
md5sums=(
  b7ca183dd3a25473d67136cff52eba83
  da162781b02adf0726a19a3d8bd5b3cc
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
