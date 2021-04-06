# Maintainer: Daurnimator <daurnimator@archlinux.org>
# Contributer: Bjorn Neergaard (neersighted) <bjorn@neersighted.com>
# Contributer: Peter Sutton (foxxy) <foxxy@foxdogstudios.com>

pkgname=ngrok
pkgver=2.3.38
pkgrel=1
pkgdesc='A tunneling, reverse proxy for developing and understanding networked, HTTP services'
url='https://ngrok.com'
license=('custom')
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
source_i686=("https://bin.equinox.io/a/dSNu6tQY6s7/ngrok-2.3.38-linux-386")
sha256sums_i686=('dd63ec2752303aa5f87718187d66391bdb686e6af60ad9bfc7e1154f92c0c899')
source_x86_64=("https://bin.equinox.io/a/2bHnBNUx6zB/ngrok-2.3.38-linux-amd64")
sha256sums_x86_64=('18e8c1da8d64658b0c7177517576bedd21d1d6dd9916216b8a1b5fd317b499ec')
source_armv7h=("https://bin.equinox.io/a/h37qTyEB1m/ngrok-2.3.38-linux-arm")
sha256sums_armv7h=('8c852eac84a198f2c953b23d918157010c8af65dcf098b14ee5ac9cf1d0814fa')
source_aarch64=("https://bin.equinox.io/a/8FNih6eeFm5/ngrok-2.3.38-linux-arm64")
sha256sums_aarch64=('b203ccb08439c90e0b23ab08dd7790aa9bb283a18e1ece7a741b5904c7265b3a')

package() {
  cd "${srcdir}"

  # Install the program.
  install -Dm755 ngrok-${pkgver}-linux-* "${pkgdir}/usr/bin/ngrok"
}

# vim: ft=sh ts=2 sw=2 et
