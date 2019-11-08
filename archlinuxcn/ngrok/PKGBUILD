# Maintainer: Daurnimator <daurnimator@archlinux.org>
# Contributer: Bjorn Neergaard (neersighted) <bjorn@neersighted.com>
# Contributer: Peter Sutton (foxxy) <foxxy@foxdogstudios.com>

pkgname=ngrok
pkgver=2.3.35
pkgrel=1
pkgdesc='A tunneling, reverse proxy for developing and understanding networked, HTTP services'
url='https://ngrok.com'
license=('custom')
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
source_i686=("https://bin.equinox.io/a/bjFaKy3TSAg/ngrok-${pkgver}-linux-386")
sha256sums_i686=('1fdd1c057c3c31044400ef6ade20ad3f10bce415ad33ccfb4bc2fd83bb36f62f')
source_x86_64=("https://bin.equinox.io/a/52fZaxjGg9n/ngrok-${pkgver}-linux-amd64")
sha256sums_x86_64=('b456608239cdf4b5119916c62a87640667d1cb1900c53faed89e3dacc1fe4679')
source_armv7h=("https://bin.equinox.io/a/2cUd5mRRjoF/ngrok-${pkgver}-linux-arm")
sha256sums_armv7h=('94d88311e9b2baea615d9fe7c6921ac0167040ec66aa0d0cbb856c027d617f1f')
source_aarch64=("https://bin.equinox.io/a/k2qx6ipHqpb/ngrok-${pkgver}-linux-arm64")
sha256sums_aarch64=('fd07f5c449f1c1444606bbc9d06fa6b649325ddf0b3e6dac6f32d785a886f170')

package() {
  cd "${srcdir}"

  # Install the program.
  install -Dm755 ngrok-${pkgver}-linux-* "${pkgdir}/usr/bin/ngrok"
}

# vim: ft=sh ts=2 sw=2 et
