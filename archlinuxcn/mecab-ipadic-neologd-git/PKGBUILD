# Maintainer: Yuanji <self@gimo.me>
pkgname=mecab-ipadic-neologd-git
_pkgname=mecab-ipadic-neologd
pkgver=r20191028
pkgrel=1
pkgdesc="Neologism dictionary for MeCab"
arch=('any')
url="https://github.com/neologd/mecab-ipadic-neologd"
license=('Apache')
depends=('mecab' 'mecab-ipadic')
source=("git+https://github.com/neologd/mecab-ipadic-neologd.git")
makedepends=('git')
sha512sums=('SKIP')

prepare() {
    cd "$srcdir/${_pkgname}"
    # change hardcoded mecab libexecdir.
    sed -i 's!`${MECAB_PATH}-config --libexecdir`!${MECAB_DIC_DIR%/dic}!g' libexec/make-mecab-ipadic-neologd.sh
}

pkgver() {
    cd "$srcdir/${_pkgname}"
    printf "r%s" "$(git log -1 --format=%cd --date=format:%Y%m%d)"
}

package() {
    cd "$srcdir/${_pkgname}"
    ./bin/install-mecab-ipadic-neologd -p "$pkgdir$(mecab-config --dicdir)/${_pkgname}" -n -u -y
}
