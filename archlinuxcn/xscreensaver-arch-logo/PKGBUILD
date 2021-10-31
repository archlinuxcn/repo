# Maintainer: Geballin <macniaque [at] free [dot] fr>
# Maintainer: Morgenstern <charles [at] charlesbwise [dot] com>
# Contributor: Thomas Mudrunka <harvie [at] email [dot] cz>
# Contributor: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=xscreensaver-arch-logo
pkgver=6.02
pkgrel=1
pkgdesc="Screen saver and locker for the X Window System with Arch Linux branding"
url="https://www.jwz.org/${pkgname%%-*}/"
arch=('x86_64')
license=('BSD')
depends=('gdk-pixbuf-xlib'
         'glu' 
         'gtk2'
         'libxmu'         
         'perl-libwww' 
         'xorg-appres') 
makedepends=('bc' 
             'intltool' 
             'libxpm'
             'systemd')
optdepends=('gdm: for login manager support')
conflicts=('xscreensaver')
provides=('xscreensaver')
backup=('etc/pam.d/xscreensaver')
source=("${pkgname}-${pkgver}.tar.gz::https://www.jwz.org/${pkgname%%-*}/${pkgname%%-*}-${pkgver}.tar.gz"
        LICENSE 
        logo-50.xpm 
        logo-180.xpm 
        logo-50.png 
        logo-180.png)
sha512sums=('2291ec6ca2d2a24dae975f7f3a8e1733c06f289eb74955db5b3344c7ddcc1d72f82d380df984ef9199f2ed7ab8a7bc920da57d98f589ae5fd1cee082755ba1ff'
            '529ed9b7904631989803a4e1f306a0f3e496e50a123ebbd6ff77058e52aeb1b2328148d8224e54b547faff14e9d591146b9849c5fb9d1063e6db41f295f3074e'
            'dcaa60ffc8e871ce6b4199ff5cdb6ac4d391ff8c1f548f9d6a098e33ba45532dc6e4854e0ae20fbaf0f18ffc5acb2d318e558a0c94254a298ce1ec92ee1b8ec3'
            '2f9bbbd6a7fba30ed3935e4e8106642b393984ccfb6fd2e202be22021651810f8f29f21b523607268b79c7bd3f3de9fea6731a8002d027d1b1568bb6f25c9c2c'
            'a8319072feac775309a7aa0f821483240dd8eab10056c2fbaf0c1b93bcc93dc1c6ee2a8c1a7393d5fa92b7dbce6bf38d78ee1a84d8be7745de635843b1db71d8'
            '86c5e84374068827ba939121e0d269633b392e89cb206ea39479ee640c2f01dbe35b9ca4012d32c299a5c7c46f448bd51226533cb419c5c975810e826d21d5c9')

prepare() {
  cd "${srcdir}"
  for _file in logo-*; do
	install "${_file}" -Dm0644 "${srcdir}/${pkgname%%-*}-${pkgver}/hacks/images/${_file}"
  done
  install -Dm0644 "${srcdir}/logo-180.xpm" "${srcdir}/${pkgname%%-*}-${pkgver}/utils/images/logo-180.xpm"
}

build() {
  cd "${pkgname%%-*}-${pkgver}"
  ./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--localstatedir=/var \
	--libexecdir=/usr/lib \
	--with-app-defaults=/usr/share/X11/app-defaults \
	--without-setuid-hacks \
	--without-setcap-hacks \
	--with-pam \
	--with-login-manager \
	--with-gtk \
	--with-gl \
	--without-gle \
	--with-pixbuf \
	--with-jpeg
  make
}

package() {
  cd "${pkgname%%-*}-${pkgver}"
  install -d "${pkgdir}/etc/pam.d"
  make install_prefix="${pkgdir}" install
  install -Dm0644 ../LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  echo "NotShowIn=KDE;GNOME;" >> "${pkgdir}/usr/share/applications/${pkgname%%-*}-properties.desktop"
}
