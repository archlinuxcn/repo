# Quick tip:
# When developing this package
# Use `PKGEXT=".pkg.tar" makepkg` to build
# That way you don't have to wait for ~150MB to compress down to ~40MB.

# Maintainer: Zeke Sonxx <zeke@zekesonxx.com>
pkgname=moeditor-bin
pkgver=0.2.0_beta
pkgrel=1
epoch=
pkgdesc="All-purpose markdown editor based on Electrum"
arch=('x86_64')
url="https://github.com/Moeditor/Moeditor"
license=('GPL3')
groups=()
depends=('gtk2' 'libxss' 'libxtst' 'alsa-lib' 'nss' 'gconf')
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
# first one changes the _ to -, second one removes the -beta entirely.
source=("https://github.com/Moeditor/Moeditor/releases/download/v${pkgver//_/-}/moeditor_${pkgver//_beta/}-1_amd64.deb")
noextract=()
md5sums=('4db4405fd7516ce758e6a62aa2461d56')
sha512sums=('ce438ed54e98493e2443c7e432800196b06a4987415b1c9ee8a395f25af62f61d0a4f897744eebdc106e6652258250524303a914d0792406e782bba27e315ce1')
validpgpkeys=()

package() {
  bsdtar xf data.tar.xz
  mv usr "$pkgdir"

  # fix perms
  chown -R root:root "$pkgdir/usr"
  chmod 755 "$pkgdir/usr/bin/moeditor"
  chmod -R 755 "$pkgdir/usr/share/moeditor"
}
