# Maintainer: darkgeem <darkgeem at pyrokinesis dot fr>

_name=owega
pkgname="python-$_name"
pkgver=5.18.1
pkgrel=1
pkgdesc="TUI / CLI interface for conversing with GPT models (from OpenAI and +)"
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
# source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
source=("https://files.pythonhosted.org/packages/b1/c0/13234b859770aed2e109608aee82550c7fad92683a3417847299e91d282d/owega-5.18.1.tar.gz")
b2sums=('3a00ca4693d9b0a5a1c4df484ccef5ebe29dc52f78921a7bcb0d82f54a124d661678a2eb8d94dba94196414a31032422a3af33678fb11e75c195e50858ff82fd')

build() {
    cd "$srcdir/$_name-$pkgver"
	export PYTHONDONTWRITEBYTECODE=
	export PYTHONPYCACHEPREFIX=
    python setup.py build
}

package() {
    cd "$srcdir/$_name-$pkgver"
	export PYTHONDONTWRITEBYTECODE=
	export PYTHONPYCACHEPREFIX=
    python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
