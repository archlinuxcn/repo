# Maintainer: Orville Q. Song <orville@anislet.dev>
# Contributor: Howard Cheung <mail@h-cheung.cf>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=fcitx5-pinyin-zhwiki-rime
_reponame=fcitx5-pinyin-zhwiki
pkgver=20221120
_converterver=0.2.4
pkgrel=1
pkgdesc="Fcitx 5 Pinyin Dictionary from zh.wikipedia.org for rime"
arch=('any')
url="https://github.com/felixonmars/fcitx5-pinyin-zhwiki"
license=('GFDL' 'CCPL:by-sa')
makedepends=('libime' 'opencc' 'pypinyin')
source=("https://github.com/felixonmars/${_reponame}/archive/$_converterver/$pkgname-$_converterver.tar.gz"
        "https://dumps.wikimedia.org/zhwiki/$pkgver/zhwiki-$pkgver-all-titles-in-ns0.gz")
md5sums=('d929f18b1b0019da22010f0aa7bdb671'
         'b9db183ee1aac09fdc0b1696db96f564')

prepare() {
  cd ${_reponame}-$_converterver
  cp ../zhwiki-$pkgver-all-titles-in-ns0.gz ./
}

build() {
  cd ${_reponame}-$_converterver
  make VERSION=$pkgver zhwiki.dict.yaml
}

package() {
  cd ${_reponame}-$_converterver
  make VERSION=$pkgver DESTDIR="$pkgdir" install_rime_dict
}
