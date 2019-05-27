# Maintainer: Daurnimator <daurnimator@archlinux.org>
# Contributer: Bjorn Neergaard (neersighted) <bjorn@neersighted.com>
# Contributer: Peter Sutton (foxxy) <foxxy@foxdogstudios.com>

pkgname=ngrok
pkgver=2.3.29
pkgrel=1
pkgdesc='A tunneling, reverse proxy for developing and understanding networked, HTTP services'
url='https://ngrok.com'
license=('custom')
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
source_i686=("https://bin.equinox.io/a/6i2VnqLBZqg/ngrok-${pkgver}-linux-386")
sha256sums_i686=('c0859f783e66a661dc1490e0cec95dfcce0ae77deaf0aa1838613afcbd8f9451')
source_x86_64=("https://bin.equinox.io/a/6ws4BqFTLXR/ngrok-${pkgver}-linux-amd64")
sha256sums_x86_64=('625e85af6d366be4cc54ba296a6e66d3311b99db36e6ea5fe7f88941874daabb')
source_armv7h=("https://bin.equinox.io/a/3Qx4EX7AtXt/ngrok-${pkgver}-linux-arm")
sha256sums_armv7h=('8a2ec453b407bb0983d22819f3b76044100870888cc976fbf76ced18e6f66fa7')
source_aarch64=("https://bin.equinox.io/a/7qbe9PkG69E/ngrok-${pkgver}-linux-arm64")
sha256sums_aarch64=('c49a9c95dc0128e8129f9b7291b5049a45d13f27bb309ca8af59e498f98b97d0')

package() {
  cd "${srcdir}"

  # Install the program.
  install -Dm755 ngrok-${pkgver}-linux-* "${pkgdir}/usr/bin/ngrok"
}

# vim: ft=sh ts=2 sw=2 et
