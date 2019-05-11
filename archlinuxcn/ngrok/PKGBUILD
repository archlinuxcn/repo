# Maintainer: Daurnimator <daurnimator@archlinux.org>
# Contributer: Bjorn Neergaard (neersighted) <bjorn@neersighted.com>
# Contributer: Peter Sutton (foxxy) <foxxy@foxdogstudios.com>

pkgname=ngrok
pkgver=2.3.28
pkgrel=1
pkgdesc='A tunneling, reverse proxy for developing and understanding networked, HTTP services'
url='https://ngrok.com'
license=('custom')
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
source_i686=("https://bin.equinox.io/a/dpxvrSQ9kZB/ngrok-${pkgver}-linux-386")
sha256sums_i686=('5e33bdd702520a2755a704cb82131e30c19032c25390b8d482a255f6d38920e3')
source_x86_64=("https://bin.equinox.io/a/3aXmZyUY9WX/ngrok-${pkgver}-linux-amd64")
sha256sums_x86_64=('322711ddb3853043a70f733199334620957dec45d75ada207ad9054e9784d39c')
source_armv7h=("https://bin.equinox.io/a/fpM8PBiufCd/ngrok-${pkgver}-linux-arm")
sha256sums_armv7h=('60c4bff1464d887ac8756ea7eb95985b433ecc30b083df326947c49fed3b41e1')
source_aarch64=("https://bin.equinox.io/a/gv7JbBxaJ2r/ngrok-${pkgver}-linux-arm64")
sha256sums_aarch64=('a820db95ce6d570f7221312de879342b95b44dd3b18b2b4dfc331f9d55a62d3a')

package() {
  cd "${srcdir}"

  # Install the program.
  install -Dm755 ngrok-${pkgver}-linux-* "${pkgdir}/usr/bin/ngrok"
}

# vim: ft=sh ts=2 sw=2 et
