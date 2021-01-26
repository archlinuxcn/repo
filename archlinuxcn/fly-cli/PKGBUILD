# Maintainer: Sasasu <su@sasasu.me>
pkgname=fly-cli
pkgver=v6.7.4
pkgrel=4
pkgdesc="A command line interface for Concourse CI"
arch=("x86_64")
url="https://github.com/concourse/concourse/tree/master/fly"
license=('Apache-2.0')
makedepends=("go")
conflicts=("concourse-fly" "concourse-fly-bin" "concourse-fly-git")
source=("https://github.com/concourse/concourse/archive/$pkgver.tar.gz")
sha256sums=('d8e95f7a38c7efab9450315b64250bb5c26baec9f49ae204a6dbce31c9a62244')

build() {
  cd concourse-${pkgver:1}/fly
  go build -o ../../fly -ldflags="-X github.com/concourse/concourse.Version=${pkgver}"
}

package() {
  install -Dm755 fly "${pkgdir}/usr/bin/fly"
}
