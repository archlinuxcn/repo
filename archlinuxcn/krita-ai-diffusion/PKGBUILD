# Maintainer: Roald Clark <roaldclark@gmail.com>

pkgname=krita-ai-diffusion
pkgver=1.28.0
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
sha256sums=('f73f18eb45cb79e1022fff153639e8abd9d912ff06fa983e4fccab8af3f52ef6'
            'ea9504979bc5f4341d2ee2083a660a6d980be47493b710398ea618918c121f91')

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

build() {
    cd "$srcdir/$pkgname-$pkgver"
    source .venv/bin/activate
    python scripts/package.py
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

package() {
    cd "$srcdir/$pkgname-$pkgver"/scripts/.package
    install -d -m 755 "$pkgdir"/usr/share/krita/pykrita/
    cp -r {ai_diffusion,ai_diffusion.desktop} "$pkgdir"/usr/share/krita/pykrita/
    install -D -m 644 ai_diffusion/ai_diffusion.action -t "$pkgdir"/usr/share/krita/actions/
}
