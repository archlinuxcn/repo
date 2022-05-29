# Maintainer: Médéric Boquien <mboquien@free.fr>
# Contributor: Luis Martinez <luis dot martinez at disroot dot org>

pkgname=python-astropy
pkgver=5.1
pkgrel=1
pkgdesc="A community python library for astronomy"
arch=('i686' 'x86_64')
url="http://www.astropy.org/"
license=('BSD')
depends=('python>=3.8' 'python-numpy>=1.18.0' 'python-pyerfa>=2.0' 'python-yaml>=3.13' 'python-packaging>=19.0' 'cfitsio>=4.0.0' 'expat>=2.2.9' 'wcslib>=7.7')
optdepends=('python-scipy: powers a variety of features in several modules'
            'python-matplotlib: provides plotting functionality that astropy.visualization enhances'
            'python-h5py: reads/writes Table objects from/to HDF5 files'
            'python-beautifulsoup4: reads Table objects from HTML files'
            'python-html5lib: reads Table objects from HTML files using the pandas reader'
            'python-bleach: used to sanitize text when disabling HTML escaping in the Table HTML writer'
            'libxml2: validates VOTABLE XML files. This is a command line tool installed outside of Python'
            'python-pandas: converts Table objects from/to pandas DataFrame objects'
            'python-sortedcontainers: faster SCEngine indexing engine with Table, although this may still be slower in some cases than the default indexing engine'
            'python-pytz: specifies and converts between timezones'
            'python-jplephem: retrieves JPL ephemeris of Solar System objects'
            'python-setuptools: used for discovery of entry points which are used to insert fitters into astropy.modeling.fitting'
            'python-mpmath: used for the ‘kraft-burrows-nousek’ interval in poisson_conf_interval'
            'python-asdf: enables the serialization of various Astropy classes into a portable, hierarchical, human-readable representation'
            'python-bottleneck: improves the performance of sigma-clipping and other functionality that may require computing statistics on arrays with NaN values'
            'python-certifi: useful when downloading files from HTTPS or FTP+TLS sites in case Python is not able to locate up-to-date root CA certificates on your system'
            'python-pyarrow: To read/write Table objects from/to Parquet files'
)
conflicts=('python-pyfits' 'python-vo')
makedepends=('cython' 'python-jinja' 'python-setuptools-scm' 'python-extension-helpers')
source=("https://files.pythonhosted.org/packages/source/a/astropy/astropy-${pkgver}.tar.gz")
sha512sums=('fe81429734be6184a9f4321fc34cf9ccf174eb4ee61deeb311e497adabe4321c388476ad2174c7756848575246caadf42b71c5f3587815761b34aa998641c37f')

build() {
  cd "${srcdir}/astropy-${pkgver}"
  ASTROPY_USE_SYSTEM_ALL=1 python setup.py build
}

package() {
  cd "${srcdir}/astropy-${pkgver}"

  install -Dm 644 -t "${pkgdir}/usr/share/licenses/${pkgname}/" licenses/*
  PYTHONHASHSEED=0 python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}
