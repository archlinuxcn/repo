# Maintainer: Doug Newgard <scimmia at archlinux dot org>
# Contributor: XavierCLL <xavier.corredor.llano (a) gmail.com>
# Contributor: SaultDon <sault.don gmail>
# Contributor: Lantald < lantald at gmx.com >
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: dibblethewrecker dibblethewrecker.at.jiwe.dot.org
# Contributor: Gerardo Exequiel Pozzi <vmlinuz386@yahoo.com.ar>
# Contributor: Eric Forgeot < http://esclinux.tk >

# Globe Plugin and Map Server are disabled in cmake by default.
# Uncomment them in the build() portion if you'd like them enabled.
# You will also need to install osgearth or fcgi, respectively, before building.

pkgname=qgis
pkgver=3.0.1
pkgrel=1
pkgdesc='Geographic Information System (GIS) that supports vector, raster & database formats'
url='https://qgis.org/'
license=('GPL')
arch=('x86_64')
depends=('expat' 'gcc-libs' 'gdal' 'geos' 'glibc' 'libspatialite' 'libzip' 'postgresql-libs' 'proj'
         'qca-qt5' 'qextserialport' 'qscintilla-qt5' 'qt5-3d' 'qt5-base' 'qt5-location' 'qt5-svg'
         'qt5-webkit' 'qtkeychain' 'qwt' 'qwtpolar' 'spatialindex' 'sqlite'
         'python' 'python-qscintilla-qt5' 'python-pyqt5' 'python-sip')
makedepends=('cmake' 'gsl' 'perl' 'txt2tags' 'qt5-tools' 'python-six')
optdepends=('gpsbabel: GPS Tool plugin'
            'gsl: Georeferencer plugin'
            'python-gdal: DB Manager plugin; Processing plugin'
            'python-jinja: MetaSearch plugin'
            'python-owslib: MetaSearch plugin'
            'python-psycopg2: DB Manager plugin; Processing plugin'
            'python-pygments: MetaSearch plugin; DB Manager plugin'
            'python-numpy: Processing plugin'
            'python-yaml: Processing plugin'
            'saga-gis-ltr: Saga processing tools')
source=("https://qgis.org/downloads/$pkgname-$pkgver.tar.bz2")
md5sums=('a9fac346ab7a4dfdf8755c7d3aecc3a0')

prepare() {
  cd $pkgname-$pkgver

  # Find Qt5ExtSerialPort
  sed -e '/include$/ s/$/\/qt/' \
      -e 's/qextserialport-1.2/Qt5ExtSerialPort/' \
      -i cmake/FindQextserialport.cmake

  # Remove mime types already defined by freedesktop.org
  sed -e '/type="image\/tiff"/,/<\/mime-type>/d' \
      -e '/type="image\/jpeg"/,/<\/mime-type>/d' \
      -e '/type="image\/jp2"/,/<\/mime-type>/d' \
      -e '/type="application\/x-adobe-mif"/,/<\/mime-type>/d' \
      -i debian/qgis.xml

  [[ -d build ]] || mkdir build
}

build() {
  cd $pkgname-$pkgver/build

  cmake -G "Unix Makefiles" ../ \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DQGIS_MANUAL_SUBDIR=share/man \
    -DENABLE_TESTS=FALSE \
    -DWITH_PY_COMPILE=TRUE \
    -DWITH_3D=TRUE \
    -DWITH_INTERNAL_QEXTSERIALPORT=FALSE \
    -DWITH_QWTPOLAR=TRUE \
#    -DWITH_SERVER=TRUE \
#    -DWITH_GLOBE=TRUE

  make

  # Rebuild srs database, QGIS distributes an old, buggy one
  LD_LIBRARY_PATH="$PWD/output/lib/" make synccrsdb
  mv /tmp/srs.db ../resources/
}

package() {
  cd $pkgname-$pkgver/build

  # Add optional deps based on selected or autodetected options
  [[ -n "$(sed -n '/^GRASS_PREFIX7:/ s/.*=//p' CMakeCache.txt)" ]]      && optdepends+=('grass: GRASS7 plugin')
  [[ "$(sed -n '/^WITH_SERVER:/ s/.*=//p' CMakeCache.txt)" == "TRUE" ]] && optdepends+=('fcgi: Map Server')
  [[ "$(sed -n '/^WITH_GLOBE:/  s/.*=//p' CMakeCache.txt)" == "TRUE" ]] && optdepends+=('osgearth: Globe plugin')

  make DESTDIR="$pkgdir" install

  cd "$srcdir/$pkgname-$pkgver"

  # install desktop file and icon
  install -Dm644 debian/qgis.desktop -t "$pkgdir/usr/share/applications/"
  install -Dm644 images/icons/qgis_icon.svg "$pkgdir/usr/share/icons/hicolor/scalable/apps/qgis.svg"

  # install mime information and icons
  install -Dm644 debian/qgis.xml -t "$pkgdir/usr/share/mime/packages/"
  for _type in asc ddf dem dt0 dxf gml img mime mldata qgs qlr qml qpt shp sqlite; do
    install -Dm644 images/icons/qgis_${_type}_icon.svg "$pkgdir/usr/share/icons/hicolor/scalable/mimetypes/qgis-$_type.svg"
  done
}
