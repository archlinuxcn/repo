# Maintainer: Daurnimator <daurnimator@archlinux.org>
# Contributer: Bjorn Neergaard (neersighted) <bjorn@neersighted.com>
# Contributer: Peter Sutton (foxxy) <foxxy@foxdogstudios.com>

pkgname=ngrok
pkgver=2.3.40
pkgrel=1
pkgdesc='A tunneling, reverse proxy for developing and understanding networked, HTTP services'
url='https://ngrok.com'
license=('custom')
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
source_i686=("https://bin.equinox.io/a/c4ZY6f7svn7/ngrok-2.3.40-linux-386")
sha256sums_i686=('1b645ff0abbb28ca7c0f6a2109653be2dc281860b582b4de6927fde12c99da26')
source_x86_64=("https://bin.equinox.io/a/b5PAmc6L9z2/ngrok-2.3.40-linux-amd64")
sha256sums_x86_64=('218d267cd1195334718bafac14bfdf1c19dc95dcf8a24aaa6a1383c21dc86e76')
source_armv7h=("https://bin.equinox.io/a/aRh9rdUAJyf/ngrok-2.3.40-linux-arm")
sha256sums_armv7h=('538a7431df141a929a250eaf6ed7afdcce817bcd8cfe60b61f4c6d7a289b1d1c')
source_aarch64=("https://bin.equinox.io/a/2gpRjDRBpJv/ngrok-2.3.40-linux-arm64")
sha256sums_aarch64=('dc7b4465ef95f6d04d1b1996111b3a2631e5f464d7dca7f4994f59ea4edbe21f')

package() {
  cd "${srcdir}"

  # Install the program.
  install -Dm755 ngrok-${pkgver}-linux-* "${pkgdir}/usr/bin/ngrok"
}

# vim: ft=sh ts=2 sw=2 et
