# Contributor: Médéric Boquien <mboquien@free.fr>
# Maintainer: Médéric Boquien <mboquien@free.fr>
pkgname=python-astropy
pkgver=4.2
pkgrel=2
pkgdesc="A community python library for astronomy"
arch=('i686' 'x86_64')
url="http://www.astropy.org/"
license=('BSD')
depends=('python>=3.7' 'python-numpy>=1.17.0' 'cfitsio>=3.49' 'python-pyerfa>=1.7' 'expat>=2.2.9' 'wcslib>=7.3')
optdepends=('python-scipy: powers a variety of features in several modules'
            'python-h5py: reads/writes Table objects from/to HDF5 files'
            'python-beautifulsoup4: reads Table objects from HTML files'
            'python-html5lib: reads Table objects from HTML files using the pandas reader'
            'python-bleach: used to sanitize text when disabling HTML escaping in the Table HTML writer'
            'python-pyaml: reads/writes Table objects from/to the Enhanced CSV ASCII table format and to serialize mixins for various formats'
            'python-pandas: converts Table objects from/to pandas DataFrame objects'
            'python-sortedcontainers: faster SCEngine indexing engine with Table, although this may still be slower in some cases than the default indexing engine'
            'python-pytz: specifies and converts between timezones'
            'python-jplephem: retrieves JPL ephemeris of Solar System objects'
            'python-matplotlib: provides plotting functionality that astropy.visualization enhances'
            'python-setuptools: used for discovery of entry points which are used to insert fitters into astropy.modeling.fitting'
            'python-mpmath: used for the ‘kraft-burrows-nousek’ interval in poisson_conf_interval'
            'python-asdf: enables the serialization of various Astropy classes into a portable, hierarchical, human-readable representation'
            'python-bottleneck: improves the performance of sigma-clipping and other functionality that may require computing statistics on arrays with NaN values'
            'libxml2: validates VOTABLE XML files. This is a command line tool installed outside of Python'
)
conflicts=('python-pyfits' 'python-vo')
makedepends=('cython' 'python-jinja' 'python-pip')
source=("https://files.pythonhosted.org/packages/source/a/astropy/astropy-${pkgver}.tar.gz")
sha512sums=('14bb90aac13f3fe668114ebe578aac401987e8e2cd2bb9fb0971e5b8e9f8df6a594d454bb53e330807c3854c44d295e2b4dc96b57ccb69e5f53ee11356869d9d')

build() {
  cd "${srcdir}/astropy-${pkgver}"

  ASTROPY_USE_SYSTEM_ALL=1 PIP_CONFIG_FILE=/dev/null pip wheel --no-cache-dir --no-deps --wheel-dir="${srcdir}/astropy-${pkgver}" .
}

package() {
  cd "${srcdir}/astropy-${pkgver}"

  install -d -m755 "${pkgdir}/usr/share/licenses/${pkgname}/"
  install -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}/" licenses/*
  PIP_CONFIG_FILE=/dev/null pip install --isolated --ignore-installed --no-deps --no-warn-script-location --root="${pkgdir}" "$(ls ./*.whl 2> /dev/null)"
  rm "${pkgdir}"/usr/lib/python*/site-packages/astropy-"${pkgver}".dist-info/direct_url.json
}
