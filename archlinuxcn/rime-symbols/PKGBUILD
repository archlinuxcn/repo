# Maintainer: fkxxyz <fkxxyz@163.com>

pkgname=rime-symbols
pkgver=1.0.0
pkgrel=1
pkgdesc="Chinese to symbols support for rime"
arch=('any')
url="https://github.com/fkxxyz/rime-symbols"
license=('LGPL')
source=(https://github.com/fkxxyz/rime-symbols/releases/download/${pkgver}/rime-symbols-release.tar.xz)
sha512sums=('f71ac2e04e5c28be81d8f6726f8a3f07fb7c5d72231f2e7ff9458e9d84e4c01747d5032795e8b4c9ee10e53455cf19d47a541b5ea9db67ff2ffe4a6b57a94d18')

package() {
  cd ${srcdir}
  install -Dm644 opencc/* -t "$pkgdir"/usr/share/rime-data/opencc/
}

