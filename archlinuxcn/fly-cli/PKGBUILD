# Maintainer: Sasasu <su@sasasu.me>
pkgname=fly-cli
pkgver=v7.8.0
pkgrel=14
pkgdesc="A command line interface for Concourse CI"
arch=("x86_64")
url="https://github.com/concourse/concourse/tree/master/fly"
license=('Apache-2.0')
makedepends=("go")
conflicts=("concourse-fly" "concourse-fly-bin" "concourse-fly-git")
source=("https://github.com/concourse/concourse/archive/$pkgver.tar.gz")
sha256sums=('bbbd05f6144411427ddebb9f821419365c95fdbd3d95bf05c098e44a50e0abe6')

build() {
  cd concourse-${pkgver:1}/fly
  go build -o ../../fly -ldflags="-X github.com/concourse/concourse.Version=${pkgver}"
}

package() {
  install -Dm755 fly "${pkgdir}/usr/bin/fly"
}
