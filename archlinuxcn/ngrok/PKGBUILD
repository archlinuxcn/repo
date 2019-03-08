# Maintainer: Daurnimator <daurnimator@archlinux.org>
# Contributer: Bjorn Neergaard (neersighted) <bjorn@neersighted.com>
# Contributer: Peter Sutton (foxxy) <foxxy@foxdogstudios.com>

pkgname=ngrok
pkgver=2.3.15
pkgrel=1
pkgdesc='A tunneling, reverse proxy for developing and understanding networked, HTTP services'
url='https://ngrok.com'
license=('Apache')
source_i686=("https://bin.equinox.io/a/69wy2ozvjqo/ngrok-${pkgver}-linux-386")
source_x86_64=("https://bin.equinox.io/a/7GwWiZuTWsF/ngrok-${pkgver}-linux-amd64")
source_armv7h=("https://bin.equinox.io/a/2vXJBm1a435/ngrok-${pkgver}-linux-arm")
source_aarch64=("https://bin.equinox.io/a/mkXQR3dwNn/ngrok-${pkgver}-linux-arm64")
sha256sums_i686=('8cf2e741074fb53074d2caa76b970aee72deffc33006d2d7fec309b9f55233ce')
sha256sums_x86_64=('597ff719093b702ebfe6afbfa051c8005afcf5fd6a300b1feb7f8be05457ccb9')
sha256sums_armv7h=('27886aeefbfd14d08d56f753bfce87b438cb53cf8ed9fc92a448090c9ed4390a')
sha256sums_aarch64=('9e82f5b0dcce429aa12453c5892dc2c1cbd91cbbbce038f1e3b0cafb895bd680')
arch=('i686' 'x86_64' 'armv7h' 'aarch64')

package() {
  cd "${srcdir}"

  # Install the program.
  install -Dm755 ngrok-${pkgver}-linux-* "${pkgdir}/usr/bin/ngrok"
}

# vim: ft=sh ts=2 sw=2 et
