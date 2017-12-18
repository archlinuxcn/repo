# Maintainer: Doug Newgard <scimmia at archlinux dot info>
# Contributor: XavierCLL <xavier.corredor.llano (a) gmail.com>
# Contributor: SaultDon <sault.don gmail>
# Contributor: Lantald < lantald at gmx.com >
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: dibblethewrecker dibblethewrecker.at.jiwe.dot.org
# Contributor: Gerardo Exequiel Pozzi <vmlinuz386@yahoo.com.ar>
# Contributor: Eric Forgeot < http://esclinux.tk >

# Globe Plugin and Map Server are disabled in cmake by default.
# Uncomment them in the build() portion if you'd like them enabled.
# You will also need to install osgearth-qt4 or fcgi, respectively, before building.

pkgname=qgis
pkgver=2.18.15
pkgrel=2
pkgdesc='Geographic Information System (GIS) that supports vector, raster & database formats'
url='https://qgis.org/'
license=('GPL')
arch=('i686' 'x86_64')
depends=('expat' 'gcc-libs' 'gdal' 'geos' 'glibc' 'libspatialite' 'postgresql-libs' 'proj'
         'qt4' 'qca-qt4' 'qjson' 'qscintilla-qt4' 'qwt-qt4' 'qwtpolar-qt4' 'spatialindex' 'sqlite'
         'python2' 'python2-httplib2' 'python2-future' 'python2-qscintilla-qt4' 'python2-sip' 'python2-six')
makedepends=('cmake' 'gsl' 'perl' 'txt2tags')
optdepends=('gpsbabel: GPS Tool plugin'
            'gsl: Georeferencer plugin'
            'python2-jinja: MetaSearch plugin'
            'python2-owslib: MetaSearch plugin'
            'python2-pygments: MetaSearch plugin'
            'python2-psycopg2: DB Manager plugin'
            'python2-pygments: DB Manager plugin'
            'python2-pyspatialite: DB Manager plugin'
            'python2-psycopg2: Processing plugin'
            'python2-pyspatialite: Processing plugin'
            'python2-yaml: Processing plugin')
source=("https://qgis.org/downloads/$pkgname-$pkgver.tar.bz2")
md5sums=('fd82e49e7ebbb391811bc5b14eb8daa5')

prepare() {
  cd $pkgname-$pkgver

  # Make sure we find the -qt4 versions of qwt and qwtpolar
  sed -i '/QWT_LIBRARY_NAMES/ s/qwt /qwt-qt4 /' cmake/FindQwt.cmake
  sed -i '/PATH_SUFFIXES/ s/qwt$/&-qt4/;/LIBRARY NAMES/ s/qwtpolar/&-qt4/' cmake/FindQwtPolar.cmake

  # Fix references to "python"
  sed -i 's/\(env \|\/usr\/bin\/\)python$/&2/' $(find . -iname "*.py")

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
    -DCMAKE_SKIP_RPATH=TRUE \
    -DPYTHON_EXECUTABLE=/usr/bin/python2 \
    -DWITH_QTWEBKIT=FALSE \
    -DWITH_INTERNAL_QWTPOLAR=FALSE \
    -DWITH_INTERNAL_{MARKUPSAFE,OWSLIB,DATEUTIL,PYTZ,YAML,NOSE2,SIX,FUTURE}=FALSE \
#    -DWITH_SERVER=TRUE \
#    -DWITH_GLOBE=TRUE

  make

  LD_LIBRARY_PATH="$PWD/output/lib/" make synccrsdb
  mv /tmp/srs.db ../resources/
}

package() {
  cd $pkgname-$pkgver/build

  # Add optional deps based on selected or autodetected options
  [[ -n "$(sed -n '/^GRASS_PREFIX:/ s/.*=//p' CMakeCache.txt)" ]] && optdepends+=('grass6: GRASS6 plugin')
  [[ -n "$(sed -n '/^GRASS_PREFIX7:/ s/.*=//p' CMakeCache.txt)" ]] && optdepends+=('grass: GRASS7 plugin')
  [[ "$(sed -n '/^WITH_SERVER:/ s/.*=//p' CMakeCache.txt)" == "TRUE" ]] && optdepends+=('fcgi: Map Server')
  [[ "$(sed -n '/^WITH_GLOBE:/ s/.*=//p' CMakeCache.txt)" == "TRUE" ]] && optdepends+=('osgearth-qt4: Globe plugin')

  make DESTDIR="$pkgdir" install

  cd "$srcdir/$pkgname-$pkgver"

  # install desktop files and icons
  install -Dm644 debian/{qgis,qbrowser}.desktop -t "$pkgdir/usr/share/applications/"
  for icon in qgis-icon{,-16x16,-60x60} qbrowser-icon{,-60x60}; do
    local _resolution="${icon##*-}"; [[ "$_resolution" == "icon" ]] && _resolution="512x512"
    install -Dm644 images/icons/$icon.png "$pkgdir/usr/share/icons/hicolor/$_resolution/apps/${icon%%-*}.png"
  done
  for prog in qgis qbrowser; do
    install -Dm644 images/icons/${prog}_icon.svg "$pkgdir/usr/share/icons/hicolor/scalable/apps/$prog.svg"
  done

  # install mime information and icons
  install -Dm644 debian/qgis.xml "$pkgdir/usr/share/mime/packages/qgis.xml"
  install -Dm644 images/icons/qgis-mime-icon.png "$pkgdir/usr/share/icons/hicolor/128x128/mimetypes/qgis-mime.png"
  for type in asc ddf dem dt0 dxf gml img mime mldata qgs qlr qml qpt shp sqlite; do
    install -Dm644 images/icons/qgis_${type}_icon.svg "$pkgdir/usr/share/icons/hicolor/scalable/mimetypes/qgis-$type.svg"
  done

  # compile python files, since the cmake option doesn't seem to account for DESTDIR
  python2 -m compileall -q "$pkgdir"
}
