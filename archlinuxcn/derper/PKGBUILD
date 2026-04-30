# Maintainer:    Jun Ouyang <ouyangjun1999@gmail.com>
# Co-Maintainer: Takase <takase1121@proton.me>

pkgname=derper
pkgver=1.96.4
pkgrel=1

pkgdesc='Tailscale runs DERP relay servers to help connect your nodes.'
url='https://github.com/tailscale/tailscale'
arch=('x86_64' 'aarch64')
license=('BSD-3-Clause')

depends=('glibc')
makedepends=('go' 'git')

options=(!lto)
backup=('etc/conf.d/derper')


source=("derper-v$pkgver.tar.gz::https://github.com/tailscale/tailscale/archive/v$pkgver.tar.gz"
        derper.service
        derper.conf)

sha256sums=('57b70731af7ae0ed167519924905fd032ddd8559a65bc8a3329d9da495f0feb2'
            '2547fa9f0bfb250507d5edfef3bb6304835c9de2c061386a89543eebf16a8bc8'
            'ecaebd5f1fb0853464afeece438269303e8590aec8689554516036575deabcfc')

build() {
  cd tailscale-$pkgver
  go build -buildmode=pie -ldflags "-linkmode external \"-extldflags=$LDFLAGS\"" ./cmd/derper
}

package() {
  install -Dm644 derper.service "$pkgdir"/usr/lib/systemd/system/derper.service
  install -Dm644 derper.conf "${pkgdir}"/etc/conf.d/derper

  cd tailscale-$pkgver
  install -Dm755 -t "$pkgdir"/usr/bin derper
}
