# Maintainer: Gesh <gesh@gesh.uni.cx>

pkgname='python-citeproc-py'
_module='citeproc-py'
pkgver='0.8.2'
pkgrel=1
pkgdesc="Citations and bibliography formatter"
url="https://github.com/brechtm/citeproc-py"
depends=('python' 'python-lxml')
checkdepends=('python-nose')
makedepends=(
    'git'
    'python-setuptools'
    'python-build' 'python-installer' 'python-wheel'
    'rnc2rng'
)
license=('BSD-2-Clause-Views')
arch=('any')
source=("$pkgname::git+${url}.git#tag=v$pkgver")
sha256sums=('c4ace67054888cdaecaf282c6cf05ea6784b6f02c400c34d312cf7b609a5dd9a'
            'SKIP'
            'SKIP')

declare -A _submods
_submods['citeproc/data/schema']='schema'
source+=(schema::git+https://github.com/citation-style-language/schema.git)
_submods['citeproc/data/locales']='locales'
source+=(locales::git+https://github.com/citation-style-language/locales.git)

prepare() {
    cd "$pkgname"

    if ! sha256sum -c \
        <<< '304b09a991a593fc142db1932f38da252e2a8f0eef4cb5887ed9f5c6cafcb5e1  .gitmodules'
    then
        msg "$pkgname-$pkgver/.gitmodules differs from expectation"
        msg 'Check it against the submodule list in PKGBUILD'
        exit 1
    fi

    git submodule init
    for _mod in "${_submods[@]}"; do
        git config submodule."$_mod".url "$srcdir/${_submods[$_mod]}"
    done
    # See https://bugs.archlinux.org/task/76255 for why this is safe
    git -c protocol.file.allow=always submodule update
}

build() {
    cd "$pkgname"
    python -m build --wheel --no-isolation
}

check() {
    cd "$pkgname"
    nosetests
}

package() {
    cd "$pkgname"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/"$pkgname"/
}
