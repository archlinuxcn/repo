# Maintainer: Zhong Lufan <lufanzhong@gmail.com>

# shellcheck shell=bash
# shellcheck disable=SC2034,SC2154,SC2164

pkgname=wsl2-ssh-agent
pkgver=0.9.6
pkgrel=1
pkgdesc="A bridge from WSL2 ssh client to Windows ssh-agent.exe service"
arch=('x86_64' 'aarch64')
url="https://github.com/mame/wsl2-ssh-agent"
license=('MIT')
makedepends=('go>=1.18')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/mame/wsl2-ssh-agent/archive/v${pkgver}.tar.gz")
sha256sums=('f8aa881bd477e9f12ed487dc325a79b50732b835c7d421fff80177f6ff9ade48')

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
