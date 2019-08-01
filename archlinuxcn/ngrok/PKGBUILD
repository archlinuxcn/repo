# Maintainer: Daurnimator <daurnimator@archlinux.org>
# Contributer: Bjorn Neergaard (neersighted) <bjorn@neersighted.com>
# Contributer: Peter Sutton (foxxy) <foxxy@foxdogstudios.com>

pkgname=ngrok
pkgver=2.3.34
pkgrel=1
pkgdesc='A tunneling, reverse proxy for developing and understanding networked, HTTP services'
url='https://ngrok.com'
license=('custom')
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
source_i686=("https://bin.equinox.io/a/2KJo4QoH8nJ/ngrok-${pkgver}-linux-386")
sha256sums_i686=('d53ad1133c94a55a252d661e296f3311145f53869780c10b1cc7a22c73ed3785')
source_x86_64=("https://bin.equinox.io/a/9UwwoKW1ydz/ngrok-${pkgver}-linux-amd64")
sha256sums_x86_64=('6a002bb3d2a81babc0643f97784216a8fc7ccd99c26310225ef428eaef06ac89')
source_armv7h=("https://bin.equinox.io/a/e9rFBj8rYfy/ngrok-${pkgver}-linux-arm")
sha256sums_armv7h=('381121bd0601b02412448b20dc3b2d0af9c49cfa610a01e9c9b31aff6b42f4b9')
source_aarch64=("https://bin.equinox.io/a/mUYsz1xP8DD/ngrok-${pkgver}-linux-arm64")
sha256sums_aarch64=('55c88f80c0b42943cdf0aaf17c981fb340800145d37f55e2eea62c17d833bf6f')

package() {
  cd "${srcdir}"

  # Install the program.
  install -Dm755 ngrok-${pkgver}-linux-* "${pkgdir}/usr/bin/ngrok"
}

# vim: ft=sh ts=2 sw=2 et
