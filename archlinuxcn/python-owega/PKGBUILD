# Maintainer: darkgeem <darkgeem at pyrokinesis dot fr>

_name=owega
pkgname="python-$_name"
pkgver=5.14.0
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
    'python-setuptools'
)
makedepends=('python-setuptools')
optdepends=(
    'python-rich: fancy output print for TUI'
    'python-pygame: for TTS audio output'
    'python-markdownify: for better webpage handling (get_page function)'
    'python-tiktoken: better token estimation'
)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
b2sums=('22007b2ac340b327b8f5516f62d21f755f1c5e632e65c0d8582cecf0deb2037ba3f3a17d8bd759836bea5330ad261a0856ecaacb05aa9e8fb76f325195d7383c')

build() {
    cd "$srcdir/$_name-$pkgver"
    python setup.py build
}

package() {
    cd "$srcdir/$_name-$pkgver"
    python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
