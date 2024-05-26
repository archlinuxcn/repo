# Contributor: Gesh <gesh@gesh.uni.cx>
# Maintainer: Stefan Gehr <stefan@gehr.xyz>

pkgname=papis
pkgver=0.13
pkgrel=6
pkgdesc="Command-line document and bibliography manager"
arch=('any')
url="https://github.com/papis/papis"
license=('GPL-3.0-or-later')
depends=('python'
    'python-arxiv2bib'
    'python-beautifulsoup4'
    'python-bibtexparser'
    'python-click'
    'python-colorama'
    'python-doi'
    'python-dominate'
    'python-filetype'
    'python-habanero'
    'python-isbnlib'
    'python-lxml'
    'python-prompt_toolkit'
    'python-pygments'
    'python-pyparsing'
    'python-requests'
    'python-slugify'
    'python-stevedore'
    'python-tqdm'
    'python-typing_extensions'
    'python-yaml'
)
optdepends=(
    'fzf: fzf picker'
    'papis-rofi: integration with rofi'
    'papis-zotero: imports from zotero'
    'pdfjs: pdf reader in the web app'
    'python-chardet: improved encoding autodetection when scraping'
    'python-jinja: jinja formatting'
    'python-papis-scihub: imports from scihub'
    'python-markdownify: convert zenodo imports to markdown'
    'python-whoosh: whoosh database backend'
    'python-docutils: for papis.sphinx_ext (used by some plugins)'
    'python-sphinx: for papis.sphinx_ext (used by some plugins)'
    'python-sphinx-click: for papis.sphinx_ext (used by some plugins)'
    'python-pytest: for papis.testing (used by some plugins)'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-wheel'

    'python-setuptools'
)
checkdepends=(
    'python-pytest'
    'python-pytest-cov'
    # These are optional -- if they're not installed, papis will automatically
    # skip these tests -- and are only necessary if you intend to use the
    # optdeps as well
    'python-jinja'
    'python-markdownify'
    'python-whoosh'
)

source=("${pkgname}-${pkgver}::${url}/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=('efff09aeaaacf170ef5c01170f1c856dbe09566096deb7ae649bfe755d58f225467241464e4b4bf8f36c25898fc7e9f689358073ab45e81d651defd127729af3')

build() {
  cd "${pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

check() {
  cd "${pkgname}-${pkgver}"
  python -m pytest papis tests \
    -k 'not (test_config.py and test_get_configuration) and not (test_arxiv.py and test_general)'
}

package() {
  cd "${pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
}

# vim:set ts=2 sw=2 et:
