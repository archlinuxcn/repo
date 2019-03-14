# Maintainer: Daurnimator <daurnimator@archlinux.org>
# Contributer: Bjorn Neergaard (neersighted) <bjorn@neersighted.com>
# Contributer: Peter Sutton (foxxy) <foxxy@foxdogstudios.com>

pkgname=ngrok
pkgver=2.3.17
pkgrel=1
pkgdesc='A tunneling, reverse proxy for developing and understanding networked, HTTP services'
url='https://ngrok.com'
license=('Apache')
source_i686=("https://bin.equinox.io/a/g4YHJQ1Yenm/ngrok-${pkgver}-linux-386")
source_x86_64=("https://bin.equinox.io/a/hd8X5RLv5sC/ngrok-${pkgver}-linux-amd64")
source_armv7h=("https://bin.equinox.io/a/kFCaZM9xSKH/ngrok-${pkgver}-linux-arm")
source_aarch64=("https://bin.equinox.io/a/ePe8gXb9Bru/ngrok-${pkgver}-linux-arm64")
sha256sums_i686=('d3f55d09a286a823cf5011b59dc22f51a9292a5cdb5d215b4b88cbbc99ae62e0')
sha256sums_x86_64=('ba3d167d8573da3f9f7f5fa3608125e96a3977330b32b62b68296482adca2d4f')
sha256sums_armv7h=('c704c945dadbaac9218702c30025052d437f63230e53b2ea3fa98017f7149c19')
sha256sums_aarch64=('0ccc6a53f4b4aace3235a3b06fc578dffadf01bc9e1a758f6d0c313fac12c934')
arch=('i686' 'x86_64' 'armv7h' 'aarch64')

package() {
  cd "${srcdir}"

  # Install the program.
  install -Dm755 ngrok-${pkgver}-linux-* "${pkgdir}/usr/bin/ngrok"
}

# vim: ft=sh ts=2 sw=2 et
