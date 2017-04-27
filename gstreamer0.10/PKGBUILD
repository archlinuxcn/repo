# Maintainer Yurii Kolesnykov <yurikoles@gmail.com>
# Credit: Jan de Groot <jgc@archlinux.org>

pkgname=gstreamer0.10
_pkgname=gstreamer
pkgver=0.10.36
pkgrel=16
pkgdesc="GStreamer Multimedia Framework"
arch=('i686' 'x86_64' 'armv7h')
license=('LGPL')
url='https://github.com/triceratops1/gstreamer0'
depends=('libxml2' 'glib2')
makedepends=('intltool' 'pkgconfig' 'gobject-introspection' 'git')
source=("git+https://gitlab.com/gstreamer-sdk/$_pkgname.git#commit=3ddc31eaa18c3be1613e43430eca78a3e445639e"
        'tests-remove-silly-test_fail_abstract_new-check.patch'
        'bison3.patch')
sha256sums=('SKIP'
            'd3d3f4f04453831fdb4244bfe174a38c4e6f9f4da5c8c9050dcfa1a6097aad52'
            'ed154e280abf59b24d98a8ab0fe868b449b26aa61f7ae3813fab8ac615fcaefa')

prepare() {
  cd $_pkgname
  patch -Np1 -i ../tests-remove-silly-test_fail_abstract_new-check.patch
  patch -Np1 -i ../bison3.patch
  sed -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/' -i configure.ac
}
build() {
  cd $_pkgname
  NOCONFIGURE=1 ./autogen.sh
  ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --libexecdir=/usr/lib \
    --with-package-name="GStreamer (Archlinux)" \
    --with-package-origin="http://www.archlinux.org/" \
    --disable-gtk-doc --disable-static
  make
}

package() {
  cd $_pkgname
  make DESTDIR="${pkgdir}" install

  #Remove unversioned gst-* binaries to get rid of conflicts
  cd "${pkgdir}/usr/bin"
  for bins in `ls *-0.10`; do
    rm -f ${bins/-0.10/}
  done
}
