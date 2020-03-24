# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Contributor: Dario Ostuni <dario.ostuni@gmail.com>
# Based on gtk4-git

pkgname=gtk4
pkgver=3.98.1
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
         'wayland-protocols'
         'graphene'
         'json-glib'
         'colord'
         'libcups'
         'rest'
         'vulkan-icd-loader'
         'gdk-pixbuf2'
         'gst-plugins-bad')
makedepends=('gobject-introspection'
             'gtk-doc'
             'meson'
             'ninja'
             'vulkan-headers'
             'pkgconfig'
             'git'
             'sassc')
optdepends=('gnome-icon-theme: Default icon theme'
            'gnome-themes-standard: Default widget theme'
            'gdk-pixbuf2: An image loading library')
source=("https://gitlab.gnome.org/GNOME/gtk/-/archive/${pkgver}/gtk-${pkgver}.tar.gz"
        'gtk4.install'
        'gtk4-update-icon-cache.hook'
        'gtk4-update-icon-cache.script'
        'settings.ini')
sha512sums=('7f00a04d4666a3fb17859da935e655f827e91edf254949c039cc87e546e7230382b604d06cfafedb9a343475423ae511b0e4d5b735861bf9653fb4c380885cf3'
            '5dcb698a15e7d5f4611c9357782d475052944cc71e73351238ffb5dfbe18d1bd1b62289da7f8066cde256c4339de5efa982088f47781876f5d8317f92b87f79f'
            '9d3bb80afb3a00dc50402d32476719daaeab017e1a066425bb602316b534d0a9899d48734a84f70af1066ed104df0491264383a34969dfad2ea9828fb41b9b6b'
            '805cf12606c738d0442d8af415223d3faada93c933b563b7c4c1d5e0c16d2d21435406add1fcc69300fb2fe534f2d0ddbf50b2c0463fc7462109d0f7802ccef1'
            '1642d77622d61234e316e8fcbc803a6a5556c606e37e56aa5981ef2f2df85bfa959c31b5d1bff248b340760e1178281cb0d7abdf540c5f7d4b62cb383a67c685')
install=gtk4.install

build() {
  cd gtk-${pkgver}

  meson --prefix=/usr \
    --sysconfdir=/etc \
    --localstatedir=/var \
    --libdir=/usr/lib \
    -Dbroadway-backend=true \
    -Dvulkan=yes \
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
}
