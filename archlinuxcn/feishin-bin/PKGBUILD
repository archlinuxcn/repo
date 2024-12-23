# Maintainer: exu <aur _a_ frm01 _d_ net>

pkgname=feishin-bin
pkgdesc='Rewrite of Sonixd'
pkgver=0.12.1
pkgrel=1
arch=('x86_64' 'aarch64')
url='https://github.com/jeffvli/feishin'
license=('GPL3')
optdepends=('mpv: Alternative audio backend')
provides=("${pkgname%-bin}")
conflicts=("${pkgname%-bin}")
_filename=Feishin-${pkgver//_/-}-linux
source=("feishin.desktop")
source_x86_64=("https://github.com/jeffvli/feishin/releases/download/v${pkgver//_/-}/${_filename}-x64.tar.xz")
source_aarch64=("https://github.com/jeffvli/feishin/releases/download/v${pkgver//_/-}/${_filename}-arm64.tar.xz")
sha256sums=('ef112b1a9ef80d8bf27f721fdbb12de0a195da4e464dbf27282503ba398bef8d')
sha256sums_x86_64=('9c16c7256c3a8c1939a15ccf5aa5ce7d9e88cd94ad7948b389fe674e9b47d6bc')
sha256sums_aarch64=('39d32a2890920b0646f1d0c97508bd19318360a44ad64ab2a3c160eddea19dd5')

package() {
  # create target file structure
  mkdir -p "$pkgdir/usr/bin"
  mkdir -p "$pkgdir/usr/share/"{feishin,pixmaps,applications}
  # HACK rename package correctly
  if [ $CARCH == "x86_64" ]; then
    mv ${_filename}-x64.tar.xz ${_filename}-$CARCH.tar.xz
  elif [ $CARCH == "aarch64" ]; then
    mv ${_filename}-arm64.tar.xz ${_filename}-$CARCH.tar.xz
  fi
  # extract files to target
  tar -xf ${_filename}-$CARCH.tar.xz -C "$pkgdir/usr/share/feishin" --strip-components=1
  # install icon
  install -Dm644 "$pkgdir/usr/share/feishin/resources/assets/icons/icon.png" "$pkgdir/usr/share/pixmaps/${pkgname%-bin}.png"
  # symlink executable to "/usr/bin/feishin"
  ln -s /usr/share/feishin/feishin "${pkgdir}/usr/bin/feishin"
  # install desktop entry
  install -Dm644 feishin.desktop "$pkgdir/usr/share/applications/"
}
