# Maintainer: Daurnimator <daurnimator@archlinux.org>
# Contributer: Bjorn Neergaard (neersighted) <bjorn@neersighted.com>
# Contributer: Peter Sutton (foxxy) <foxxy@foxdogstudios.com>

pkgname=ngrok
pkgver=2.3.30
pkgrel=1
pkgdesc='A tunneling, reverse proxy for developing and understanding networked, HTTP services'
url='https://ngrok.com'
license=('custom')
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
source_i686=("https://bin.equinox.io/a/k5XA32QkfJ4/ngrok-${pkgver}-linux-386")
sha256sums_i686=('fb45b70df5c12e063e9e9ba81ddef86e261a48a79730f0cec31021171b1ee980')
source_x86_64=("https://bin.equinox.io/a/bfqGAdcUmQ4/ngrok-${pkgver}-linux-amd64")
sha256sums_x86_64=('15611b39e8883e187cdb975206dbd613e8c7893a69f5fc1bc14236c8ab3b7c54')
source_armv7h=("https://bin.equinox.io/a/mWvWHen8MrX/ngrok-${pkgver}-linux-arm")
sha256sums_armv7h=('3609466804119bf85f6c65dd931b07f0cc92abb65873fe6e1514813c8f74d808')
source_aarch64=("https://bin.equinox.io/a/37vpM1dJrX4/ngrok-${pkgver}-linux-arm64")
sha256sums_aarch64=('54c75a00f0e44007750c150311bca09435cba7bfd1df11327fdd906a8a9f4dfd')

package() {
  cd "${srcdir}"

  # Install the program.
  install -Dm755 ngrok-${pkgver}-linux-* "${pkgdir}/usr/bin/ngrok"
}

# vim: ft=sh ts=2 sw=2 et
