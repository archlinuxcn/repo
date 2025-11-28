# Maintainer: RocketDev <ma2014119@outlook.com>
# 如果需要拆包的话可以联系我
pkgname=python-iced-x86
pkgver=1.21.0
pkgrel=1
pkgdesc='Blazing fast and correct x86/x64 disassembler, assembler, decoder, encoder'
arch=('x86_64')
url='https://github.com/icedland/iced'
license=('MIT')
depends=(
    'python'
    'glibc'
    'gcc-libs'
)
makedepends=(
    'python-build'
    'python-setuptools'
    'python-installer'
    'python-wheel'
    'python-setuptools-rust'
    'python-sphinx'
)
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
b2sums=('2c5ed8a7fb2f797b18bedc39382ecf1c22dd704f61a0dc5f3c60b26e9125293598750047f8fae9c28a23b5ecda0e27e3865b7f5cab109238a84bc6a83cfd6f8c')

prepare() {
    # Use rust code in tar instead of downloaded
    cd "iced-$pkgver/src/rust/iced-x86-py"
    _sed_cmd='s|#path = "/abs/path/to/iced/src/rust/iced-x86"|path = "'$srcdir/iced-$pkgver/src/rust/iced-x86'"|'
    echo "Patching cargo toml with $_sed_cmd ..."
    sed -i "$_sed_cmd" Cargo.toml
    echo "Patching setup.py to keep symbols..."
    sed -i 's|, strip=Strip.All||' setup.py
}

build() {
    cd "iced-$pkgver/src/rust/iced-x86-py"
    python -m build --wheel --no-isolation
    python -m sphinx -b html docs docs/_build
}

package() {
    cd "iced-$pkgver/src/rust/iced-x86-py"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm0755 -d "$pkgdir/usr/share/doc/$pkgname"
    _b=docs/_build
    cp -r $_b/*.* $_b/_static $_b/src "$pkgdir/usr/share/doc/$pkgname"
    install -Dm0644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
