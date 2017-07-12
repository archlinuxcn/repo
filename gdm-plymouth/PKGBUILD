# Maintainer: Sebastian Lau <lauseb644 _at_ gmail _dot_ com>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Damian01w <damian01w@gmail.com>

_pkgbase=gdm
pkgbase=gdm-plymouth
pkgname=(gdm-plymouth libgdm-plymouth)
pkgver=3.24.1
pkgrel=2
pkgdesc="Gnome Display Manager with Plymouth support."
arch=(i686 x86_64)
license=(GPL)
url="http://www.gnome.org"
depends=('plymouth' 'gnome-shell>=3.24.1' 'gnome-session' 'upower' 'xorg-xrdb' 'xorg-server' 'xorg-server-xwayland' 'xorg-xhost')
makedepends=('intltool' 'yelp-tools' 'gobject-introspection')
checkdepends=('check')
source=("https://git.gnome.org/browse/gdm/snapshot/${_pkgbase}-${pkgver}.tar.xz"
	"0002-Xsession-Don-t-start-ssh-agent-by-default.patch")
sha256sums=('0d7b70a0e937356925d0b1d5e595e60711b71418e78bb5078b92edf616aa1557'
            '63f99db7623f078e390bf755350e5793db8b2c4e06622caf42eddc63cd39ecca')

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
    --with-gnome-settings-daemon-directory=/usr/lib/gnome-settings-daemon \
    --without-tcp-wrappers \
    --with-default-pam-config=arch

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

  rm -r "$pkgdir/var/run"

### Split libgdm
  make -C libgdm DESTDIR="$pkgdir" uninstall
  mv "$pkgdir/usr/share/glib-2.0/schemas/org.gnome.login-screen.gschema.xml" "$srcdir"
}

package_libgdm-plymouth() {
  pkgdesc="GDM support library including Plymouth support"
  depends=(systemd glib2)
  provides=("libgdm")
  conflicts=("libgdm")

  cd $_pkgbase-${pkgver}
  make -C libgdm DESTDIR="$pkgdir" install
  install -Dm644 "$srcdir/org.gnome.login-screen.gschema.xml" \
    "$pkgdir/usr/share/glib-2.0/schemas/org.gnome.login-screen.gschema.xml"
}
