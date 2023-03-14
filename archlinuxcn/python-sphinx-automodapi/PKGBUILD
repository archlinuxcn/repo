# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-sphinx-automodapi
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}" "python-${_pyname}-doc")
pkgver=0.15.0
pkgrel=1
pkgdesc="Sphinx extension for generating API documentation."
arch=('any')
url="https://sphinx-automodapi.readthedocs.io"
license=('BSD')
makedepends=('python-setuptools-scm'
             'python-wheel'
             'python-build'
             'python-installer'
             'python-sphinx'
             'python-sphinx_rtd_theme')
checkdepends=('python-pytest' 'graphviz') # sphinx already in makedepends
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('fd5871e054df7f3e299dde959afffa849f4d01c6eac274c366b06472afcb06aa')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    msg "Building Docs"
    PYTHONPATH="../build/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    #ln -rs ${srcdir}/${_pyname}-${pkgver}/${_pyname/-/_}*egg-info \
    #    build/lib/${_pyname/-/_}-${pkgver}-py$(get_pyver .).egg-info
    #PYTHONPATH="build/lib" pytest ${_pyname/-/_} || warning "Tests failed"
    pytest || warning "Tests failed" # -vv --color=yes
}

package_python-sphinx-automodapi() {
    depends=('python-sphinx>=2')
    optdepends=('python-sphinx-automodapi-doc: Documentation for sphinx-automodapi')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-sphinx-automodapi-doc() {
    pkgdesc="Documentation for sphinx-automodapi"
    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../LICENSE.rst
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
