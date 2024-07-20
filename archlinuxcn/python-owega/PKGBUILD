# Maintainer: darkgeem <darkgeem at pyrokinesis dot fr>

_name=owega
pkgname="python-$_name"
pkgver=5.13.0
pkgrel=1
pkgdesc="TUI / CLI interface for conversing with GPT models (from OpenAI)"
arch=('any')
url="https://pypi.org/project/owega/"
license=('custom:DGPL-1.0')
depends=(
    'python'
    'python-beautifulsoup4'
    'python-editor'
    'python-json5'
    'python-lxml'
    'python-openai'
    'python-prompt_toolkit'
    'python-requests'
    'python-tiktoken'
    'python-setuptools'
)
makedepends=('python-setuptools')
optdepends=(
    'python-rich: fancy output print for TUI'
    'python-pygame: for TTS audio output'
    'python-markdownify: for better webpage handling (get_page function)'
)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
b2sums=('ee40a58ef1ed7afaf802e8f28507b43beffb347c39315f797925c496435ec466d600aab37aa9fed76caf4fb9461328c109d76662237b7f4310e11eef2e2caa8f')

build() {
    cd "$srcdir/$_name-$pkgver"
    python setup.py build
}

package() {
    cd "$srcdir/$_name-$pkgver"
    python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
