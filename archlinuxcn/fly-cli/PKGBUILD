# Maintainer: Sasasu <su@sasasu.me>
pkgname=fly-cli
pkgver=v6.7.3
pkgrel=4
pkgdesc="A command line interface for Concourse CI"
arch=("x86_64")
url="https://github.com/concourse/concourse/tree/master/fly"
license=('Apache-2.0')
makedepends=("go")
conflicts=("concourse-fly" "concourse-fly-bin" "concourse-fly-git")
source=("https://github.com/concourse/concourse/archive/$pkgver.tar.gz")
sha256sums=('2f739f23970668bf3225731920b479c22506ddaa6c72c19a5ea1b5766a8ad9fc')

build() {
  cd concourse-${pkgver:1}/fly
  go build -o ../../fly -ldflags="-X github.com/concourse/concourse.Version=${pkgver}"
}

package() {
  install -Dm755 fly "${pkgdir}/usr/bin/fly"
}
