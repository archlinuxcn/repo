# Maintainer: Roald Clark <roaldclark@gmail.com>

pkgname=krita-ai-diffusion
pkgver=1.36.0
pkgrel=1
pkgdesc="A plugin to use generative AI in image painting and editing workflows from within Krita"
arch=('any')
url="https://github.com/Acly/krita-ai-diffusion"
license=('GPL-3.0-or-later')
depends=(
    'krita'
    'python-pyqt5'
    'python312' # Required to create a virtual environment (for server.py)
    'qt5-imageformats'
)
makedepends=(
    'git'
    'git-lfs'
)
checkdepends=(
    'openssl-1.1'
)
optdepends=(
    'python311: server.py will use python3.11 to create a virtual environment if python3.12 is not available'
)
install=krita-ai-diffusion.install
source=("${pkgname}::git+${url}.git#tag=v${pkgver}"
        "add-regex-to-requirements.patch")
sha256sums=('2e929b5e9454ed3f42e0a5e34c1a0a08b4b1411c5196ca097e65354f19e41df9'
            '3cdb6f448e78ae8bcfe4427d6a7b44a732b375366aa52dd4aaceb11f328edaf0')

# If `git lfs install` was run before, `makepkg` may error
# Set this env var to resolve
export GIT_LFS_SKIP_SMUDGE=1

prepare() {
    # The plugin itself will run inside Krita's embedded Python,
    # and only has access to the Python standard library and Qt5
    cd "${srcdir}/${pkgname}"
    patch -Np1 -i ../add-regex-to-requirements.patch
    git submodule update --init --recursive
    git lfs install --local
    git remote add network-origin "${url}.git"
    git lfs fetch network-origin
    git lfs checkout
    python3.12 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
}

build() {
    cd "${srcdir}/${pkgname}"
    source .venv/bin/activate
    python scripts/package.py
}

check() {
    cd "${srcdir}/${pkgname}"
    source .venv/bin/activate
    if [[ $(vercmp "${pkgver}" "1.21.0") -gt 0 ]]; then
        python scripts/download_models.py --minimal scripts/downloads
    else
        python scripts/download_models.py --minimal scripts/docker/downloads
    fi
    python -m pytest tests/test_server.py -vs --test-install
    python -m pytest tests -vs --ci
}

package() {
    cd "${srcdir}/${pkgname}"/scripts/.package
    install -d -m 755 "${pkgdir}"/usr/share/krita/pykrita/
    cp -r {ai_diffusion,ai_diffusion.desktop} "${pkgdir}"/usr/share/krita/pykrita/
    install -D -m 644 ai_diffusion/ai_diffusion.action -t "${pkgdir}"/usr/share/krita/actions/
}
