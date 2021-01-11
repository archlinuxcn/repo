# Maintainer: Sasasu <su@sasasu.me>
pkgname=fly-cli
pkgver=v6.7.2
pkgrel=4
pkgdesc="A command line interface for Concourse CI"
arch=("x86_64")
url="https://github.com/concourse/concourse/tree/master/fly"
license=('Apache-2.0')
makedepends=("go")
conflicts=("concourse-fly" "concourse-fly-bin" "concourse-fly-git")
source=("https://github.com/concourse/concourse/archive/$pkgver.tar.gz")
sha256sums=('c57852dc9cc56b0b671179ae89f3ffe20090b1b2c80b43179125e6e2bdf1302c')

build() {
  cd concourse-${pkgver:1}/fly
  go build -o ../../fly -ldflags="-X github.com/concourse/concourse.Version=${pkgver}"
}

package() {
  install -Dm755 fly "${pkgdir}/usr/bin/fly"
}
