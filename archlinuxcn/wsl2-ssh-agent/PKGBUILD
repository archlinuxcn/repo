# Maintainer: Zhong Lufan <lufanzhong@gmail.com>

# shellcheck shell=bash
# shellcheck disable=SC2034,SC2154,SC2164

pkgname=wsl2-ssh-agent
pkgver=0.9.4
pkgrel=1
pkgdesc="A bridge from WSL2 ssh client to Windows ssh-agent.exe service"
arch=('x86_64' 'aarch64')
url="https://github.com/mame/wsl2-ssh-agent"
license=('MIT')
makedepends=('go>=1.18')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/mame/wsl2-ssh-agent/archive/v${pkgver}.tar.gz")
sha256sums=('cf4ee0788a6f194b2440ab3e2ee94fec1e629fb5ef5014d2d1596ff6719815c2')

build() {
  export GOPATH="$srcdir"/gopath
  export GOFLAGS="-mod=mod -modcacherw"

  cd "$srcdir/$pkgname-$pkgver"
  go build -o $pkgname
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  install -Dm 755 $pkgname "$pkgdir"/usr/bin/wsl2-ssh-agent
}
