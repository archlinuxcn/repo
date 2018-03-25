# Maintainer: Sebastian Lau <lauseb644 _at_ gmail _dot_ com>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Damian01w <damian01w@gmail.com>

_pkgbase=gdm
pkgbase=gdm-plymouth
pkgname=(gdm-plymouth libgdm-plymouth)
pkgver=3.28.0
pkgrel=1
pkgdesc="Gnome Display Manager with Plymouth support."
arch=(i686 x86_64)
license=(GPL)
url="http://www.gnome.org"
depends=('plymouth' 'gnome-shell>=3.24.1' 'gnome-session' 'upower' 'xorg-xrdb' 'xorg-server' 'xorg-server-xwayland' 'xorg-xhost')
makedepends=('intltool' 'yelp-tools' 'gobject-introspection')
checkdepends=('check')
source=("https://git.gnome.org/browse/gdm/snapshot/${_pkgbase}-${pkgver}.tar.xz"
	"0002-Xsession-Don-t-start-ssh-agent-by-default.patch"
	"gdm.sysusers")
sha256sums=('2908bc2e84bd5c14d0736e58afc31ccdbb05b5314df66093d6d81d631a9811e9'
            '63f99db7623f078e390bf755350e5793db8b2c4e06622caf42eddc63cd39ecca'
            '6d9c8e38c7de85b6ec75e488585b8c451f5d9b4fabd2a42921dc3bfcc4aa3e13')

prepare() {
  cd $_pkgbase-${pkgver}

  patch -Np1 -i ../0002-Xsession-Don-t-start-ssh-agent-by-default.patch

  NOCONFIGURE=1 ./autogen.sh
}

build() {
  cd $_pkgbase-${pkgver}
  ./configure \
    --prefix=/usr \
    --sbindir=/usr/bin \
    --sysconfdir=/etc \
    --libexecdir=/usr/lib/gdm \
    --localstatedir=/var \
    --disable-static \
    --disable-schemas-compile \
    --enable-gdm-xsession \
    --enable-ipv6 \
    --with-plymouth \
    --with-at-spi-registryd-directory=/usr/lib/at-spi2-core \
    --with-check-accelerated-directory=/usr/lib/gnome-session \
    --with-default-pam-config=arch \
    --with-default-path=/usr/local/bin:/usr/local/sbin:/usr/bin \
    --with-gnome-settings-daemon-directory=/usr/lib/gnome-settings-daemon \
    --without-tcp-wrappers

  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool

  make
}

check() {
  cd $_pkgbase-${pkgver}
  make check
}

package_gdm-plymouth() {
  depends+=(libgdm-plymouth)
  provides=("gdm")
  conflicts=("gdm")
  optdepends=('fprintd: fingerprint authentication')
  backup=(etc/pam.d/gdm-autologin etc/pam.d/gdm-fingerprint etc/pam.d/gdm-launch-environment
          etc/pam.d/gdm-password etc/pam.d/gdm-smartcard etc/gdm/custom.conf
          etc/gdm/Xsession etc/gdm/PostSession/Default etc/gdm/PreSession/Default)
  groups=(gnome)
  install=gdm-plymouth.install

  cd $_pkgbase-${pkgver}
  make DESTDIR="$pkgdir" install

  chown -R 120:120 "$pkgdir/var/lib/gdm"

  # Unused or created at start
  rm -r "$pkgdir"/var/{cache,log,run}

  install -Dm644 ../gdm.sysusers "$pkgdir/usr/lib/sysusers.d/gdm.conf"

  ### Split libgdm
  make -C libgdm DESTDIR="$pkgdir" uninstall
  mv "$pkgdir/usr/share/glib-2.0/schemas/org.gnome.login-screen.gschema.xml" "$srcdir"
}

package_libgdm-plymouth() {
  pkgdesc="GDM support library including Plymouth support"
  depends=(systemd glib2 dconf)
  provides=("libgdm")
  conflicts=("libgdm")

  cd $_pkgbase-${pkgver}
  make -C libgdm DESTDIR="$pkgdir" install
  install -Dm644 "$srcdir/org.gnome.login-screen.gschema.xml" \
    "$pkgdir/usr/share/glib-2.0/schemas/org.gnome.login-screen.gschema.xml"
}
