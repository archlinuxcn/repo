# Maintainer: Roald Clark <roaldclark@gmail.com>

pkgname=krita-ai-diffusion
pkgver=1.23.0
pkgrel=1
pkgdesc="A plugin to use generative AI in image painting and editing workflows from within Krita"
arch=('any')
url="https://github.com/Acly/krita-ai-diffusion"
license=('GPL-3.0-or-later')
depends=(
    'krita'
    'python-pyqt5'
    'python311' # Required to create a virtual environment (for server.py)
    'qt5-imageformats'
)
makedepends=('git')
checkdepends=('openssl-1.1')
install=krita-ai-diffusion.install
source=("${pkgname}-${pkgver}::git+${url}.git#tag=v${pkgver}"
        "add-regex-to-requirements.patch")
sha256sums=('c78cd0ebdf51e3f9711f048b26470fbb5e3df950af038724adb9f227bbc9e37a'
            '57bf33f43ec7181d3a507539eb9f14e7ff54d6fa3c729df98493bc171d1cee83')

prepare() {
    # The plugin itself will run inside Krita's embedded Python,
    # and only has access to the Python standard library and Qt5
    cd "$srcdir/$pkgname-$pkgver"
    patch -Np1 -i ../add-regex-to-requirements.patch
    git submodule update --init --recursive
    python3.11 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
}

check() {
    cd "$srcdir/$pkgname-$pkgver"
    source .venv/bin/activate
    if [[ $(vercmp "$pkgver" "1.21.0") -gt 0 ]]; then
        python scripts/download_models.py --minimal scripts/downloads
    else
        python scripts/download_models.py --minimal scripts/docker/downloads
    fi
    python -m pytest tests/test_server.py -vs --test-install
    python -m pytest tests -vs --ci
}

build() {
    cd "$srcdir/$pkgname-$pkgver"
    source .venv/bin/activate
    python scripts/package.py
}

package() {
    cd "$srcdir/$pkgname-$pkgver"/scripts/.package
    install -d -m 755 "$pkgdir"/usr/share/krita/pykrita/
    cp -r {ai_diffusion,ai_diffusion.desktop} "$pkgdir"/usr/share/krita/pykrita/
    install -D -m 644 ai_diffusion/ai_diffusion.action -t "$pkgdir"/usr/share/krita/actions/
}
