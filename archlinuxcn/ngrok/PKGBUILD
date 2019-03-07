# Maintainer: Daurnimator <daurnimator@archlinux.org>
# Contributer: Bjorn Neergaard (neersighted) <bjorn@neersighted.com>
# Contributer: Peter Sutton (foxxy) <foxxy@foxdogstudios.com>

pkgname=ngrok
pkgver=2.3.13
pkgrel=1
pkgdesc='A tunneling, reverse proxy for developing and understanding networked, HTTP services'
url='https://ngrok.com'
license=('Apache')
source_i686=("ngrok::https://bin.equinox.io/a/g1Nmu3VU8Kn/ngrok-2.3.13-linux-386")
source_x86_64=("ngrok::https://bin.equinox.io/a/drE1eZCsw6j/ngrok-2.3.13-linux-amd64")
source_armv7h=("ngrok::https://bin.equinox.io/a/5XGo58kqfJR/ngrok-2.3.13-linux-arm")
source_aarch64=("ngrok::https://bin.equinox.io/a/5YHWzLSugFS/ngrok-2.3.13-linux-arm64")
sha256sums_i686=('0cebad9e55e00529e805b6dd5beb3889d3b6be954540a47928de6c940ae08790')
sha256sums_x86_64=('6428d172b4e0a1e2f7316e9340bf074cc2823b78d2b5be3e2e33fb33be7b4329')
sha256sums_armv7h=('8618c74377c8aabb5a93a1df4fa3cd4147ca4b535737e73cb7de661046834700')
sha256sums_aarch64=('097328db5f503e1e9a6fc3bba717f602f73212816f30d0fa4df46f29a662d622')
arch=('i686' 'x86_64' 'armv7h' 'aarch64')

package() {
  cd "${srcdir}"

  # Install the program.
  install -Dm755 ngrok  "${pkgdir}/usr/bin/ngrok"
}

# vim: ft=sh ts=2 sw=2 et
