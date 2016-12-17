# Maintainer: NicoHood <archlinux {cat} nicohood {dog} de>
# PGP ID: 97312D5EB9D7AE7D0BD4307351DAE9B7C1AE9161
# Contributor: <alcasa dot mz at gmail dot com>
# Contributor: twa022 <twa022 at gmail dot com>

pkgname=xfce4-pulseaudio-plugin
pkgver=0.2.4
pkgrel=3
pkgdesc="Pulseaudio plugin for Xfce4 panel"
arch=('i686' 'x86_64')
license=('GPL2')
url="https://goodies.xfce.org/projects/panel-plugins/xfce4-pulseaudio-plugin"
groups=('xfce4-goodies')
depends=('xfce4-panel>=4.11.0' 'libpulse' 'libkeybinder3' 'gtk-update-icon-cache' )
optdepends=('pavucontrol: default pulseaudio mixer'
            'libnotify: volume notifications'
            #'ido: appindicator support'
            )
makedepends=('intltool' 'libnotify' 'dbus-glib')
# TODO https source
source=(http://archive.xfce.org/src/panel-plugins/${pkgname}/${pkgver%.*}/${pkgname}-${pkgver}.tar.bz2)
sha512sums=('b53ab48e282a506fc7fe91fa70520f0db32f2f73653a0210681bf7389f13441d5af8f855604b59817b1fe7a3f41e2d4fe52b052ac0c3479f3f4e37b2afedb193')
# TODO GPG

prepare() {
    # Use Audio steps of 5 not 6 for more OCD
    sed -i 's/^#define DEFAULT_VOLUME_STEP .*/#define DEFAULT_VOLUME_STEP 5/' \
        "${srcdir}/${pkgname}-${pkgver}/panel-plugin/pulseaudio-config.c"
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  # TODO some libraries are not linked shared
  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --libexecdir=/usr/lib \
    --localstatedir=/var \
    --disable-static \
    --disable-debug
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
}
