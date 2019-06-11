# Maintainer: Xuanwo <xuanwo@archlinuxcn.org>
pkgname=makisu
pkgver=0.1.11
pkgrel=1
pkgdesc='Fast and flexible Docker image building tool, works in unprivileged containerized environments like Mesos and Kubernetes.'
depends=('glibc')
makedepends=('go' 'make' 'git')
arch=('x86_64')
url='https://github.com/uber/makisu'
license=('Apache')
provides=('makisu')
source=(makisu-${pkgver}.tar.gz::https://github.com/uber/makisu/archive/v${pkgver}.tar.gz)
sha256sums=('8d28948e0bf4f56693c836fd86d35e38c7a457206dd3f62386059f1741e4bac1')

build() {
  export GOPATH="$srcdir/build"
  export PATH=$GOPATH/bin:$PATH

  cd $pkgname-${pkgver}  

  BUILD_LDFLAGS="-X ${pkgname}/lib/utils.BuildHash=v${pkgver}"

  BUILD_LDFLAGS=$BUILD_LDFLAGS make bin/makisu/makisu
}

package() {
  # Install binary
  install -Dm755 "$srcdir/$pkgname-${pkgver}/bin/makisu/makisu" "$pkgdir/usr/bin/makisu"
}

# vim: ft=sh syn=sh et
