# Maintainer: axionl <axionl@aosc.io>
pkgname=baidupcs-go-bin
pkgver=3.5.2
pkgrel=1
pkgdesc="The terminal utility for Baidu Network Disk (Golang Version)."
arch=('x86_64')
depends=()
conflicts=("baidupcs")
provides=("baidupcs")
url="https://github.com/iikira/BaiduPCS-Go"
license=("Apache")
source=("https://raw.githubusercontent.com/iikira/BaiduPCS-Go/master/LICENSE")
source_x86_64=("https://github.com/iikira/BaiduPCS-Go/releases/download/v$pkgver/BaiduPCS-Go-v$pkgver-linux-amd64.zip")

sha256sums=('ddadea2805326e3cb072a8b6769885fc1399475922e4c7d60f5e9f8e28c63e3d')
sha256sums_x86_64=('f6695b3f89c26c6fbacde99d034f660efb029204fa42e0f437016020ccb0b926')
package() {
    dir="$srcdir/BaiduPCS-Go-v$pkgver-linux-amd64"
    install -Dm755 $dir/BaiduPCS-Go ${pkgdir}/usr/bin/baidupcs
    install -Dm755 LICENSE ${pkgdir}/usr/share/licenses/baidupcs-go/LICENSE
    echo "README FILE: https://github.com/iikira/BaiduPCS-Go/blob/master/README.md"
}
