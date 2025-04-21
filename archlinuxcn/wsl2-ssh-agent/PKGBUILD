# Maintainer: Zhong Lufan <lufanzhong@gmail.com>

# shellcheck shell=bash
# shellcheck disable=SC2034,SC2154,SC2164

pkgname=wsl2-ssh-agent
pkgver=0.9.5
pkgrel=1
pkgdesc="A bridge from WSL2 ssh client to Windows ssh-agent.exe service"
arch=('x86_64' 'aarch64')
url="https://github.com/mame/wsl2-ssh-agent"
license=('MIT')
makedepends=('go>=1.18')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/mame/wsl2-ssh-agent/archive/v${pkgver}.tar.gz")
sha256sums=('2ae63479180f126b023919775762ada36a9d16e5168736f1e63238123f35c7d7')

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
