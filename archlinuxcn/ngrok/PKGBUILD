# Maintainer: Daurnimator <daurnimator@archlinux.org>
# Contributer: Bjorn Neergaard (neersighted) <bjorn@neersighted.com>
# Contributer: Peter Sutton (foxxy) <foxxy@foxdogstudios.com>

pkgname=ngrok
pkgver=2.3.18
pkgrel=1
pkgdesc='A tunneling, reverse proxy for developing and understanding networked, HTTP services'
url='https://ngrok.com'
license=('custom')
source_i686=("https://bin.equinox.io/a/jqJ2Vvh67gW/ngrok-${pkgver}-linux-386")
source_x86_64=("https://bin.equinox.io/a/ik4d9aurG9/ngrok-${pkgver}-linux-amd64")
source_armv7h=("https://bin.equinox.io/a/c2KRZoJ5cb6/ngrok-${pkgver}-linux-arm")
source_aarch64=("https://bin.equinox.io/a/b2NBP9tpq2E/ngrok-${pkgver}-linux-arm64")
sha256sums_i686=('2bebb8f39a3c19ca03eaf786b97c92876216d2297046e85271478edef2cd6404')
sha256sums_x86_64=('75e19c343a208bf0e2d3b613d2fa3ce67abbf25c04a1d6be670598a4c25c1694')
sha256sums_armv7h=('af4cdb9f116104921d7fbeeac9124e545a45495b3623b2b46da996400c305d9c')
sha256sums_aarch64=('9e5fa5b83dc65803291b59867c664085de248a4adb3d415c4dbba1dae90a0aaf')
arch=('i686' 'x86_64' 'armv7h' 'aarch64')

package() {
  cd "${srcdir}"

  # Install the program.
  install -Dm755 ngrok-${pkgver}-linux-* "${pkgdir}/usr/bin/ngrok"
}

# vim: ft=sh ts=2 sw=2 et
