# Maintainer: envolution
# Contributor: Max Bruckner (FSMaxB)
# shellcheck shell=bash disable=SC2034,SC2154
pkgname=mecab-ipadic
pkgver=2.7.0_20070801
pkgrel=4
pkgdesc="IPA dictionary for mecab"
arch=('any')
url="https://taku910.github.io/mecab"
depends=('mecab')
license=(GPL-2.0-only)
#source=("$pkgname-${pkgver/_/-}.tar.gz::https://drive.google.com/uc?id=0B4y35FiV1wh7MWVlSDBCSXZMTXM&export=download")
_tag="2fd29256c6d5e1b10211cac838069ee9ede8c77a"
source=("$pkgname::git+https://github.com/taku910/mecab.git#tag=${_tag}")
md5sums=('5e33399fd830b3c3f66cd4b5c366c989')

build() {
  cd "$pkgname/$pkgname"
  ./configure --prefix=/usr --with-charset=utf-8
  # change hardcoded mecab installation path
  sed -i 's!libexec/mecab!lib/mecab!g' config.status
  make
}

package() {
  cd "$pkgname/$pkgname"
  make DESTDIR="$pkgdir/" install
}
# vim:set ts=2 sw=2 et:
