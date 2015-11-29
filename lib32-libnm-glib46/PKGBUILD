# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Jan de Groot <jgc@archlinxu.org>
# Contributor: Wael Nasreddine <gandalf@siemens-mobiles.org>
# Contributor: Tor Krill <tor@krill.nu>
# Contributor: Will Rea <sillywilly@gmail.com>
# Contributor: Valentine Sinitsyn <e_val@inbox.ru>

pkgname=lib32-libnm-glib46
pkgver=0.9.8.10
pkgrel=1
pkgdesc='NetworkManager library'
arch=('x86_64')
url='http://www.gnome.org/projects/NetworkManager/'
license=('GPL2' 'LGPL2.1')
depends=('lib32-dbus-glib' 'lib32-systemd' 'lib32-nss')
makedepends=('dhcpcd' 'dhclient' 'dhcp-client' 'gtk-doc' 'intltool' 'iproute2'
             'iptables' 'lib32-libmm-glib' 'lib32-libndp' 'lib32-libnewt'
             'lib32-libnl' 'lib32-polkit' 'lib32-libsoup' 'lib32-libteam'
             'modemmanager' 'ppp' 'python2' 'vala' 'wpa_supplicant')
replaces=('lib32-libnm-glib')
source=("http://ftp.gnome.org/pub/gnome/sources/NetworkManager/${pkgver%.*.*}/NetworkManager-${pkgver}.tar.xz"
        'disable_set_hostname.patch')
sha256sums=('064d27223d3824859df12e1fb25b787fec1c68bbc864dc52a0289b9211c4c972'
            '25056837ea92e559f09563ed817e3e0cd9333be861b8914e45f62ceaae2e0460')

prepare() {
  cd NetworkManager-$pkgver

  patch -Np1 -i ../disable_set_hostname.patch
  NOCONFIGURE=1 ./autogen.sh
}

build() {
  cd NetworkManager-${pkgver}

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32' \
    --libexecdir='/usr/lib32/networkmanager' \
    --localstatedir='/var' \
    --sbindir='/usr/bin' \
    --sysconfdir='/etc' \
    --enable-modify-system \
    --disable-doc \
    --disable-introspection \
    --disable-more-warnings \
    --disable-qt \
    --disable-static \
    --disable-wimax \
    --with-crypto='nss' \
    --with-dhclient='/usr/bin/dhclient' \
    --with-dhcpcd='/usr/bin/dhcpcd' \
    --with-dnsmasq='/usr/bin/dnsmasq' \
    --with-iptables='/usr/bin/iptables' \
    --with-modem-manager-1 \
    --with-resolvconf='/usr/bin/resolvconf' \
    --with-systemdsystemunitdir='/usr/lib/systemd/system' \
    --with-udev-dir='/usr/lib32/udev' \
    --with-session-tracking='systemd'
  make -C libnm-util
  make -C libnm-glib
}

package() {
  cd NetworkManager-$pkgver

  make DESTDIR="${pkgdir}" -C libnm-util install
  make DESTDIR="${pkgdir}" -C libnm-glib install
  rm -rf "${pkgdir}"/usr/{include,lib32/pkgconfig,share}
  find "${pkgdir}" -type l -delete
}

# vim: ts=2 sw=2 et:
