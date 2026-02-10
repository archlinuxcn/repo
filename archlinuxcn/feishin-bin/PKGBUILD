# Maintainer: jason _d_ nader _a_ proton _d_ me
# Submitter: exu <aur _a_ frm01 _d_ net>

pkgname=feishin-bin
pkgdesc='A player for your self-hosted music server'
pkgver=1.5.0
pkgrel=1
arch=('x86_64' 'aarch64')
url='https://github.com/jeffvli/feishin'
license=('GPL3')
optdepends=('mpv: Alternative audio backend')
provides=("${pkgname%-bin}")
conflicts=("${pkgname%-bin}")
source=("feishin.desktop")
source_x86_64=("${pkgname}-${pkgver}-${CARCH}.tar.xz::https://github.com/jeffvli/feishin/releases/download/v${pkgver//_/-}/Feishin-linux-x64.tar.xz")
source_aarch64=("${pkgname}-${pkgver}-${CARCH}.tar.xz::https://github.com/jeffvli/feishin/releases/download/v${pkgver//_/-}/Feishin-linux-arm64.tar.xz")
sha256sums=('818f9700176bc3fbb3a00a1e6e41c933114f2a6029c8143a88239c5b9fc5c194')
sha256sums_x86_64=('f88f5d3c0e3969df86ac5d92334742b5e025349462e7f75f1daf4e0522bef42f')
sha256sums_aarch64=('b1fdff4f92cd3ca8758b95c48b62982b9dcd96b9c8d54afd0085b41c59a70edb')

package() {
  # create target file structure
  mkdir -p "$pkgdir/usr/bin"
  mkdir -p "$pkgdir/usr/share/"{feishin,pixmaps,applications}
  # extract files to target
  tar -xf "${pkgname}-${pkgver}-${CARCH}.tar.xz" -C "$pkgdir/usr/share/feishin" --strip-components=1
  # install icon
  install -Dm644 "$pkgdir/usr/share/feishin/resources/assets/icons/icon.png" "$pkgdir/usr/share/pixmaps/org.jeffvli.feishin.png"
  # symlink executable to "/usr/bin/feishin"
  ln -s /usr/share/feishin/feishin "${pkgdir}/usr/bin/feishin"
  # install desktop entry
  install -Dm644 feishin.desktop "$pkgdir/usr/share/applications/"
}
