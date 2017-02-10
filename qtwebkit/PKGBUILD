# $Id: PKGBUILD 252776 2015-12-06 12:09:40Z bpiotrowski $
# Maintainer: Andrea Scarpino <andrea@archlinux.org>

pkgname=qtwebkit
pkgver=2.3.4
pkgrel=4
arch=('i686' 'x86_64')
url='http://trac.webkit.org/wiki/QtWebKit'
pkgdesc='An open source web browser engine (Qt port)'
license=('LGPL2.1' 'GPL3')
depends=('qt4' 'systemd' 'gst-plugins-base-libs')
makedepends=('gperf' 'python2' 'ruby' 'git' 'mesa')
conflicts=('qt<4.8')
_qtver=4.8.7
source=("https://sources.archlinux.org/other/packages/${pkgname}/${pkgname}-${pkgver}.tar.xz"
        "http://download.qt-project.org/official_releases/qt/4.8/${_qtver}/qt-everywhere-opensource-src-${_qtver}.tar.gz"
        'use-python2.patch'
        'qwebview.patch' 'gcc-5.patch')
sha1sums=('31bc60de1cf26bb0766d539b4d564651ddbb0650'
          '76aef40335c0701e5be7bb3a9101df5d22fe3666'
          '315b6ff603f35e5492a036f7082f6aa075dfb607'
          'c3df6107233f466a032e36681cee07f16536657c'
          '5d506578ea30daeeeb1e91ab83876fe6d5669715')

prepare() {
  cd ${pkgname}-${pkgver}
  patch -p1 -i "${srcdir}"/use-python2.patch

# Fix build with GCC 5 (Fedora)
  patch -p1 -i "$srcdir"/gcc-5.patch

  cd ../qt-everywhere-opensource-src-${_qtver}
  patch -p1 -i "${srcdir}"/qwebview.patch
}

build() {
  cd ${pkgname}-${pkgver}

  OPTS="--no-webkit2"
  if [ "${CARCH}" = "i686" ]; then
      # FS#33418
      OPTS="${OPTS} --no-force-sse2"
  fi

  export QTDIR=/usr
  export PATH="/usr/lib/qt4/bin:$PATH"
  Tools/Scripts/build-webkit --qt \
    --makeargs="${MAKEFLAGS}" \
    --prefix=/usr \
    ${OPTS}

  # Build the QWebView plugin (FS#27914)
  cd ../qt-everywhere-opensource-src-${_qtver}/tools/designer/src/plugins/qwebview
  qmake-qt4
  make
}

package() {
  cd ${pkgname}-${pkgver}
  make INSTALL_ROOT="${pkgdir}" -C WebKitBuild/Release install

  cd ../qt-everywhere-opensource-src-${_qtver}/tools/designer/src/plugins/qwebview
  make INSTALL_ROOT="${pkgdir}" install

  # Fix wrong libs path in pkgconfig file
  perl -pi -e "s, -L${srcdir}/?\S+,,g" "${pkgdir}"/usr/lib/pkgconfig/QtWebKit.pc

  # Fix wrong path in prl file
  sed -i -e '/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/' "${pkgdir}"/usr/lib/libQtWebKit.prl
}
