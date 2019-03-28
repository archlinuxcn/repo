# Maintainer: Daurnimator <daurnimator@archlinux.org>
# Contributer: Bjorn Neergaard (neersighted) <bjorn@neersighted.com>
# Contributer: Peter Sutton (foxxy) <foxxy@foxdogstudios.com>

pkgname=ngrok
pkgver=2.3.25
pkgrel=1
pkgdesc='A tunneling, reverse proxy for developing and understanding networked, HTTP services'
url='https://ngrok.com'
license=('custom')
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
source_i686=("https://bin.equinox.io/a/6rcayxm949T/ngrok-${pkgver}-linux-386")
sha256sums_i686=('41adee8ffcf483de1be4225615d9b592ec24ff15e3d50f58b0300660d8c46eb7')
source_x86_64=("https://bin.equinox.io/a/64ZvMbAj5L3/ngrok-${pkgver}-linux-amd64")
sha256sums_x86_64=('679d174c2842f2e00e3e1b9475dced3bf11f1373cbe25e63d33acf1ef6971404')
source_armv7h=("https://bin.equinox.io/a/i9vig9gvwFw/ngrok-${pkgver}-linux-arm")
sha256sums_armv7h=('aff99ea51b67009d5dcf483fb96b984541e603d278eef95d7f92332cc2448e6f')
source_aarch64=("https://bin.equinox.io/a/2T4jD3XV7uS/ngrok-${pkgver}-linux-arm64")
sha256sums_aarch64=('5ca8d32a74e78e7d9678667134e6d8aba227ced7ba704d5d3e64e3c54a36f688')

package() {
  cd "${srcdir}"

  # Install the program.
  install -Dm755 ngrok-${pkgver}-linux-* "${pkgdir}/usr/bin/ngrok"
}

# vim: ft=sh ts=2 sw=2 et
