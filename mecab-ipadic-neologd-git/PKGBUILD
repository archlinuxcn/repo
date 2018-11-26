# Maintainer: Gimo <self@gimo.me>
pkgname=mecab-ipadic-neologd-git
pkgver=r20180921
pkgrel=5
pkgdesc="Neologism dictionary for MeCab"
arch=('any')
url="https://github.com/neologd/mecab-ipadic-neologd"
license=('Apache')
depends=('mecab' 'mecab-ipadic')
makedepends=('git')

prepare() {
    git clone --single-branch --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git "$srcdir/${pkgname%-git}"
    cd "$srcdir/${pkgname%-git}"
    # change hardcoded mecab libexecdir.
    sed -i 's!`${MECAB_PATH}-config --libexecdir`!${MECAB_DIC_DIR%/dic}!g' libexec/make-mecab-ipadic-neologd.sh
}

pkgver() {
    cd "$srcdir/${pkgname%-git}"
    printf "r%s" "$(git log -1 --format=%cd --date=format:%Y%m%d)"
}

package() {
    cd "$srcdir/${pkgname%-git}"
    ./bin/install-mecab-ipadic-neologd -p "$pkgdir$(mecab-config --dicdir)/${pkgname%-git}" -n -u -y
}
