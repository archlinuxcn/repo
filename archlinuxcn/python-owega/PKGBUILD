# Maintainer: darkgeem <darkgeem at pyrokinesis dot fr>

_name=owega
pkgname="python-$_name"
pkgver=5.12.0
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
    'python-pygame'
    'python-requests'
    'python-tiktoken'
    'python-markdownify'
    'python-setuptools'
)
makedepends=('python-setuptools')
optdepends=('python-rich: fancy output print for TUI')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
b2sums=('8efdf38f00e9b68f2c6e0c4da809613a8884f463bd03dc1a4cc5a677bc1cd1d02b471d88052b81cae845c7dc5e293d616da8f6741db331b7df55f649af6f7106')

build() {
    cd "$srcdir/$_name-$pkgver"
    python setup.py build
}

package() {
    cd "$srcdir/$_name-$pkgver"
    python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
