# Maintainer: Felix Yan <felixonmars@archlinux.org>

pkgname=fcitx5-pinyin-zhwiki
pkgver=20200501
pkgrel=1
pkgdesc="Fcitx 5 Pinyin Dictionary from zh.wikipedia.org"
arch=('any')
url="https://github.com/felixonmars/fcitx5-pinyin-zhwiki"
license=('GFDL' 'CCPL:by-sa')
makedepends=('libime' 'opencc' 'pypinyin')
source=("https://github.com/felixonmars/fcitx5-pinyin-zhwiki/archive/0.1/$pkgname-0.1.tar.gz"
        https://dumps.wikimedia.org/zhwiki/$pkgver/zhwiki-$pkgver-all-titles-in-ns0.gz)
md5sums=('1863f0d556a777c05bb573eebe809494'
         '4d2ee3cf2637abe67bf1332465f57f45')

prepare() {
  cd $pkgname-0.1
  cp ../zhwiki-$pkgver-all-titles-in-ns0.gz ./
}

build() {
  cd $pkgname-0.1
  make FILENAME=zhwiki-$pkgver-all-titles-in-ns0
}

package() {
  cd $pkgname-0.1
  make DESTDIR="$pkgdir" install
}
