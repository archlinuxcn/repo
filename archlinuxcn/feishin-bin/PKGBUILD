# Maintainer: jason _d_ nader _a_ proton _d_ me
# Submitter: exu <aur _a_ frm01 _d_ net>

pkgname=feishin-bin
pkgdesc='Rewrite of Sonixd'
pkgver=0.20.1
pkgrel=3
arch=('x86_64' 'aarch64')
url='https://github.com/jeffvli/feishin'
license=('GPL3')
optdepends=('mpv: Alternative audio backend')
provides=("${pkgname%-bin}")
conflicts=("${pkgname%-bin}")
source=("feishin.desktop")
source_x86_64=("${pkgname}-${pkgver}-${CARCH}.tar.xz::https://github.com/jeffvli/feishin/releases/download/v${pkgver//_/-}/Feishin-linux-x64.tar.xz")
source_aarch64=("${pkgname}-${pkgver}-${CARCH}.tar.xz::https://github.com/jeffvli/feishin/releases/download/v${pkgver//_/-}/Feishin-linux-arm64.tar.xz")
sha256sums=('ef112b1a9ef80d8bf27f721fdbb12de0a195da4e464dbf27282503ba398bef8d')
sha256sums_x86_64=('48fd0caf925396b0261da4ad71a5e5a54fdaf3f97bb4117aa8f286f2e55ebeb5')
sha256sums_aarch64=('9eb992f1f5bd9b9bdc1f53cb23e9972ff5d5df876a1001aeb8f7b6346ddb1d19')

package() {
  # create target file structure
  mkdir -p "$pkgdir/usr/bin"
  mkdir -p "$pkgdir/usr/share/"{feishin,pixmaps,applications}
  # extract files to target
  tar -xf "${pkgname}-${pkgver}-${CARCH}.tar.xz" -C "$pkgdir/usr/share/feishin" --strip-components=1
  # install icon
  install -Dm644 "$pkgdir/usr/share/feishin/resources/assets/icons/icon.png" "$pkgdir/usr/share/pixmaps/${pkgname%-bin}.png"
  # symlink executable to "/usr/bin/feishin"
  ln -s /usr/share/feishin/feishin "${pkgdir}/usr/bin/feishin"
  # install desktop entry
  install -Dm644 feishin.desktop "$pkgdir/usr/share/applications/"
}
