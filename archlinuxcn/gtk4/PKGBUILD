# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Contributor: Dario Ostuni <dario.ostuni@gmail.com>
# Based on gtk4-git

pkgname=gtk4
pkgver=4.0.0
pkgrel=1
pkgdesc="GObject-based multi-platform GUI toolkit"
arch=('i686' 'x86_64')
url="https://www.gtk.org/"
license=('LGPL')
provides=('gtk4' 'gtk4-print-backends' 'gtk4-update-icon-cache')
replaces=('gtk4-print-backends' 'gtk4-update-icon-cache')
conflicts=('gtk4-git' 'gtk4-print-backends' 'gtk4-update-icon-cache')
depends=('hicolor-icon-theme'
         'at-spi2-atk'
         'atk'
         'dconf'
         'glib2'
         'libepoxy'
         'libxcomposite'
         'libxcursor'
         'libxinerama'
         'libxkbcommon'
         'libxrandr'
         'mesa'
         'pango'
         'wayland'
         'graphene'
         'json-glib'
         'colord'
         'libcups'
         'rest'
         'vulkan-icd-loader'
         'gdk-pixbuf2'
         'gst-plugins-bad')
makedepends=('gobject-introspection'
             'meson'
             'ninja'
             'vulkan-headers'
             'wayland-protocols'
             'pkgconfig'
             'git'
             'sassc')
optdepends=('gnome-icon-theme: Default icon theme'
            'gnome-themes-standard: Default widget theme'
            'gdk-pixbuf2: An image loading library')
source=("https://download.gnome.org/sources/gtk/${pkgver%.*}/gtk-${pkgver}.tar.xz"
        'gtk4.install'
        'gtk4-update-icon-cache.hook'
        'gtk4-update-icon-cache.script'
        'settings.ini'
        'fix-incompatible-vulkan-error.patch')
sha512sums=('5fe807bcdb59f0df2ad1cc5a28b654dbf90f5fa29bf9a4c69c9278543ab9a3e4f8b1712547fb2fd1f35711c438f78ee8a5cd1a509cf64f815274bb8c82023922'
            '5dcb698a15e7d5f4611c9357782d475052944cc71e73351238ffb5dfbe18d1bd1b62289da7f8066cde256c4339de5efa982088f47781876f5d8317f92b87f79f'
            '9d3bb80afb3a00dc50402d32476719daaeab017e1a066425bb602316b534d0a9899d48734a84f70af1066ed104df0491264383a34969dfad2ea9828fb41b9b6b'
            '805cf12606c738d0442d8af415223d3faada93c933b563b7c4c1d5e0c16d2d21435406add1fcc69300fb2fe534f2d0ddbf50b2c0463fc7462109d0f7802ccef1'
            '1642d77622d61234e316e8fcbc803a6a5556c606e37e56aa5981ef2f2df85bfa959c31b5d1bff248b340760e1178281cb0d7abdf540c5f7d4b62cb383a67c685'
            '2abb3e5c0743992bdffb5cdb2a9256577acba1e3da39971921e013d9d197dbbc5dd29555176f558a2176bd2a2853fd6370b8e7004257c4d001d3211694a9b9c3')
install=gtk4.install

prepare() {
  cd gtk-${pkgver}
  patch -p1 -i "$srcdir"/fix-incompatible-vulkan-error.patch
}

build() {
  cd gtk-${pkgver}

  meson --prefix=/usr \
    --sysconfdir=/etc \
    --localstatedir=/var \
    --libdir=/usr/lib \
    -Dbroadway-backend=true \
    -Dvulkan=enabled \
    -Dgtk_doc=false \
    _build .

  cd _build

  ninja
}

package() {
  cd gtk-${pkgver}/_build

  DESTDIR="$pkgdir" ninja install

  install -Dm 644 "../../settings.ini" "$pkgdir"/usr/share/gtk-4.0/settings.ini
  install -D "gtk/tools/gtk4-update-icon-cache" "$pkgdir"/usr/bin/gtk4-update-icon-cache
  install -Dm 644 "../../gtk4-update-icon-cache.hook" "$pkgdir"/usr/share/libalpm/hooks/gtk4-update-icon-cache.hook
  install -Dm 755 "../../gtk4-update-icon-cache.script" "$pkgdir"/usr/share/libalpm/scripts/gtk4-update-icon-cache

  # Remove conflicts with gtk3
  rm -f "$pkgdir/usr/share/gettext/its/gtkbuilder.its"
  rm -f "$pkgdir/usr/share/gettext/its/gtkbuilder.loc"
  rm -f "$pkgdir/usr/share/glib-2.0/schemas/org.gtk.Demo.gschema.xml"
  rm -f "$pkgdir/usr/share/glib-2.0/schemas/org.gtk.Settings.ColorChooser.gschema.xml"
  rm -f "$pkgdir/usr/share/glib-2.0/schemas/org.gtk.Settings.Debug.gschema.xml"
  rm -f "$pkgdir/usr/share/glib-2.0/schemas/org.gtk.Settings.FileChooser.gschema.xml"
  rm -f "$pkgdir/usr/share/glib-2.0/schemas/org.gtk.Settings.EmojiChooser.gschema.xml"
  rm -f "$pkgdir/usr/share/glib-2.0/schemas/org.gtk.exampleapp.gschema.xml"

  # Remove conflicts with gtk-doc
  rm -f "$pkgdir/usr/bin/gtkdoc-check"
  rm -f "$pkgdir/usr/bin/gtkdoc-depscan"
  rm -f "$pkgdir/usr/bin/gtkdoc-fixxref"
  rm -f "$pkgdir/usr/bin/gtkdoc-mkdb"
  rm -f "$pkgdir/usr/bin/gtkdoc-mkhtml"
  rm -f "$pkgdir/usr/bin/gtkdoc-mkhtml2"
  rm -f "$pkgdir/usr/bin/gtkdoc-mkman"
  rm -f "$pkgdir/usr/bin/gtkdoc-mkpdf"
  rm -f "$pkgdir/usr/bin/gtkdoc-rebase"
  rm -f "$pkgdir/usr/bin/gtkdoc-scan"
  rm -f "$pkgdir/usr/bin/gtkdoc-scangobj"
  rm -f "$pkgdir/usr/bin/gtkdocize"
  rm -f "$pkgdir/usr/share/aclocal/gtk-doc.m4"
  rm -rf "$pkgdir/usr/share/cmake/GtkDoc"
  rm -rf "$pkgdir/usr/share/gtk-doc"
  rm -f "$pkgdir/usr/share/pkgconfig/gtk-doc.pc"
}
