# Maintainer: Tomas Ostasevicius (aquarix) <t dot ostasevicius at gmail dot com>
pkgname=gitter
pkgver=3.0.3
pkgrel=1
pkgdesc='Where developers come to talk'
url='https://gitter.im'
license=('unknown')
arch=('x86_64')
depends=('libsystemd' 'desktop-file-utils' 'gconf')
makedepends=('tar' 'binutils')
source=("https://update.gitter.im/linux64/${pkgname}_${pkgver}_amd64.deb"
        gitter.sh)
noextract=("${pkgname}_${pkgver}_amd64.deb")
install='gitter.install'
md5sums=('fc8a0389e255c02556e19d8ef7238276'
         '4ee1a1a85d4fd6fbaf0a16ffefd7d84d')
options=(!strip)

prepare() {
  cd "$srcdir"
  ar x "${pkgname}_${pkgver}_amd64.deb"
}

package() {
  cd "$srcdir"
  tar -C "$pkgdir" -xf data.tar.gz
  mkdir -p "$pkgdir/opt/Gitter/lib"
  ln -sf /usr/lib64/libudev.so.1 "$pkgdir/opt/Gitter/lib/libudev.so.0"
  install -Dm755 "$srcdir/$pkgname.sh" "$pkgdir/usr/bin/$pkgname"
  RPM_BUILD_ROOT="$pkgdir" desktop-file-install "$pkgdir/opt/Gitter/linux64/gitter.desktop"
  sed -e 's#/opt/Gitter/linux64/Gitter#/usr/bin/gitter#' -i "$pkgdir/usr/share/applications/gitter.desktop"
}
