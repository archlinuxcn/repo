# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-sphinx_design
_pname=${pkgbase#python-}
_pyname=${_pname/_/-}
pkgname=("python-${_pname}" "python-${_pname}-doc")
pkgver=0.6.1
pkgrel=1
pkgdesc="A sphinx extension for designing beautiful, screen-size responsive web components"
arch=('any')
url="https://sphinx-design.readthedocs.io"
license=('MIT')
makedepends=('python-flit-core'
             'python-wheel'
             'python-build'
             'python-installer'
             'python-myst-parser')  # sphinx required by myst-parser
#checkdepends=('python-pytest'
checkdepends=('python-pytest-regressions')  # myst-parser already in makedepends
#source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
#source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pname}/${_pname}-${pkgver}.tar.gz")
source=("${_pyname}-${pkgver}.tar.gz::https://github.com/executablebooks/sphinx-design/archive/refs/tags/v${pkgver}.tar.gz"
        'Makefile')
md5sums=('99841868d97ee1709cd34487e5896733'
         'a6aa4bc42b138d75f938065a0994c3e1')

prepare() {
    cd ${srcdir}/${_pyname}-${pkgver}

    ln -s ${srcdir}/Makefile docs
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    msg "Building Docs"
    mkdir -p dist/lib
    bsdtar -xpf dist/${_pyname/-/_}-${pkgver}-py3-none-any.whl -C dist/lib
    PYTHONPATH="../dist/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count
#   nosetests #|| warning "Tests failed"
}

package_python-sphinx_design() {
    depends=('python-sphinx')
    optdepends=('pre-commit: code-style'
                'python-myst-parser: rtd'
                'python-sphinx-furo: theme-furo'
                'python-sphinx_rtd_theme: theme-rtd'
                'python-sphinx-book-theme: theme-sbt'
                'python-pydata-sphinx-theme: theme-pydata'
                'python-sphinx_design-doc: Documentation for sphinx_design')
    provides=("python-sphinx-design=${pkgver}")
    conflicts=('python-sphinx-design')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-sphinx_design-doc() {
    pkgdesc="Documentation for sphinx_design"
    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -D -m644 ../../LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
