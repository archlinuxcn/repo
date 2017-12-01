# Maintainer: Dario Ostuni <dario.ostuni@gmail.com>
# Based on gtk4-git

pkgbase=gtk4
pkgname=(gtk4-update-icon-cache gtk4 gtk4-print-backends)
pkgver=3.91.1
pkgrel=2
pkgdesc="GObject-based multi-platform GUI toolkit"
arch=('i686' 'x86_64')
url="http://www.gtk.org/"
license=('LGPL')
depends=('adwaita-icon-theme'
         'at-spi2-atk'
         'atk'
         'cairo'
         'dconf'
         'desktop-file-utils'
         'glib2'
         'gdk-pixbuf2'
         'json-glib'
         'libcups'
         'libepoxy'
         'librsvg'
         'libxcomposite'
         'libxcursor'
         'libxdamage'
         'libxi'
         'libxinerama'
         'libxkbcommon'
         'libxrandr'
         'mesa'
         'pango'
         'shared-mime-info'
         'wayland'
         'wayland-protocols'
         'graphene')
makedepends=('gobject-introspection'
             'gtk-doc'
             'git'
             'colord'
             'rest'
             'libcups'
             'autoconf-archive')
optdepends=('gnome-icon-theme: Default icon theme'
            'gnome-themes-standard: Default widget theme')
backup=('usr/share/gtk-4.0/settings.ini')
source=("https://git.gnome.org/browse/gtk+/snapshot/gtk+-${pkgver}.tar.xz"
        'gtk4.install'
        'gtk4-query-immodules.hook'
        'gtk4-update-icon-cache.hook'
        'gtk4-update-icon-cache.script'
        'settings.ini')
sha512sums=('de97b3957b6697408277f4551a5428a185a151292f57f1041078b9255d821d5eda9252ea987570063f02596ea3f553b96f9bc4e848b6f9f8091d5a61da760e80'
            '5dcb698a15e7d5f4611c9357782d475052944cc71e73351238ffb5dfbe18d1bd1b62289da7f8066cde256c4339de5efa982088f47781876f5d8317f92b87f79f'
            '1dbcce0a3e17ee05b579613adba25feff692f6626155e91fa6859e5f176753201b5ceffa8c9c7c897cf945aeeb32fbd28affa24050dfc0d65237733964bf28de'
            'abfd73de4faa6f53784182800395aa3c39bb98e15a0eb300fb4142073ff7ce565a0836a2363393b2f132060b5293dbc0c30c380a023f38d5bd39c62cb58389c2'
            '5cd50d93bb6bc203438a2a0764bd717409658e124058b18a1da26a21f10ef7564a16f32fc0633a68b45b2e303fa63a5efefeadd6b0bf1d7f474556df8cdb6c58'
            '1642d77622d61234e316e8fcbc803a6a5556c606e37e56aa5981ef2f2df85bfa959c31b5d1bff248b340760e1178281cb0d7abdf540c5f7d4b62cb383a67c685')

prepare() {
  cd gtk+-${pkgver}
  NOCONFIGURE=1 ./autogen.sh
}

build() {
  cd gtk+-${pkgver}

  CXX=/bin/false ./configure --prefix=/usr \
    --sysconfdir=/etc \
    --localstatedir=/var \
    --disable-schemas-compile \
    --enable-x11-backend \
    --enable-broadway-backend \
    --enable-wayland-backend \
    --disable-gtk-doc

  # https://bugzilla.gnome.org/show_bug.cgi?id=655517
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool

  make
}

package_gtk4() {
  depends+=(gtk-update-icon-cache)
  install="gtk4.install"

  cd gtk+-${pkgver}

  make DESTDIR="$pkgdir" install

  install -Dm644 "../settings.ini" "$pkgdir/usr/share/gtk-4.0/settings.ini"
  install -Dm644 ../gtk4-query-immodules.hook "$pkgdir/usr/share/libalpm/hooks/gtk4-query-immodules.hook"

  rm "$pkgdir/usr/bin/gtk4-update-icon-cache"

  cd "$pkgdir"
  for _f in usr/lib/*/*/printbackends/*; do
    case $_f in
        *-file.so|*-lpr.so) continue;;
    esac

    mkdir -p "$srcdir/print-backends/${_f%/*}"
    mv "$_f" "$srcdir/print-backends/$_f"
  done

  # Remove conflicts with gtk3
  rm -f "$pkgdir/usr/share/gettext/its/gtkbuilder.its"
  rm -f "$pkgdir/usr/share/gettext/its/gtkbuilder.loc"
  rm -f "$pkgdir/usr/share/glib-2.0/schemas/org.gtk.Demo.gschema.xml"
  rm -f "$pkgdir/usr/share/glib-2.0/schemas/org.gtk.Settings.ColorChooser.gschema.xml"
  rm -f "$pkgdir/usr/share/glib-2.0/schemas/org.gtk.Settings.Debug.gschema.xml"
  rm -f "$pkgdir/usr/share/glib-2.0/schemas/org.gtk.Settings.FileChooser.gschema.xml"
  rm -f "$pkgdir/usr/share/glib-2.0/schemas/org.gtk.exampleapp.gschema.xml"
}

package_gtk4-update-icon-cache() {
  pkgdesc="GTK+ icon cache updater"
  depends=(gdk-pixbuf2 hicolor-icon-theme)

  cd gtk+-${pkgver}
  install -D gtk/gtk4-update-icon-cache "$pkgdir/usr/bin/gtk4-update-icon-cache"
  install -Dm644 ../gtk4-update-icon-cache.hook "$pkgdir/usr/share/libalpm/hooks/gtk4-update-icon-cache.hook"
  install -D ../gtk4-update-icon-cache.script "$pkgdir/usr/share/libalpm/scripts/gtk4-update-icon-cache"
}

package_gtk4-print-backends() {
  pkgdesc="Print backends for GTK4"
  depends=(gtk4 rest colord libcups)

  mv print-backends/* "$pkgdir"
}
