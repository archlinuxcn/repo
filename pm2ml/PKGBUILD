#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=pm2ml
pkgver=2015.11.21
pkgrel=1
pkgdesc='Generate metalinks for downloading Pacman packages and databases.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/pm2ml"
depends=(python3 pyalpm python3-xcpf)
optdepends=('python3-aur: AUR support' 'reflector: Reflector support' 'aria2: ppl script support.')
backup=(etc/ppl.conf)
source=(
  http://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2015.11.21.tar.xz
  http://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2015.11.21.tar.xz.sig
)
sha512sums=(
  67f8d73626a6ba0f1998759f09ded81f78eeb121f8180abdb4ef0331a0aa523b0230f62882aea67e48c3dbf9511123b5a254b49aeaf3914e5ac032bf08adff4c
  51f8330f6a4a184426e522058dd689c0aaffafb66602130a9a0d164bc63e25f752f250a5d399880626ef68ce5adb9841874883a8f9b4f6aa7172a66cd0808a0d
)
md5sums=(
  720d8f40dd922fc7544c5c0670351363
  8e6eb8ac1560e51d3580b47765819ee2
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
