# Maintainer: Morgenstern <charles [at] charlesbwise [dot] com>
# Maintainer: Geballin <macniaque [at] free [dot] fr>
# Contributor: Thomas Mudrunka <harvie [at] email [dot] cz>
# Contributor: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=xscreensaver-arch-logo
pkgver=6.12
pkgrel=1
pkgdesc="Screen saver and locker for the X Window System with Arch Linux branding"
url="https://www.jwz.org/${pkgname%%-*}/"
arch=('x86_64')
license=('0BSD')
depends=('glu'
         'gtk3'
         'libxmu'
         'perl-libwww'
         'xdg-utils'
         'xorg-appres') 
makedepends=('bc'
             'intltool'
             'libxpm'
             'systemd')
optdepends=('gdm: for login manager support'
            'perl-lwp-protocol-https: for MapScroller hack support, per FS #74184')
conflicts=('xscreensaver')
provides=('xscreensaver')
backup=('etc/pam.d/xscreensaver')
source=("${pkgname}-${pkgver}.tar.gz::https://www.jwz.org/${pkgname%%-*}/${pkgname%%-*}-${pkgver}.tar.gz"
        LICENSE 
        logo-50.gif
        logo-180.gif
        logo-360.gif
        logo-big.gif
        logo.pdf
        logo-32.png
        logo-50.png 
        logo-180.png
        logo-360.png
        logo-512.png
        logo-50.xpm
        logo-180.xpm
        logo-360.xpm)
noextract=("${pkgname}-${pkgver}.tar.gz")
sha512sums=('df98e07fe66fd6ad1fd680c6790d66a160f146ff721f90a76c46142888a0d17f82f068343b1ac82aa4562385460da393dc4733abdb26f0cda0f2a8944a614497'
            '529ed9b7904631989803a4e1f306a0f3e496e50a123ebbd6ff77058e52aeb1b2328148d8224e54b547faff14e9d591146b9849c5fb9d1063e6db41f295f3074e'
            'a63d93f148500eb8ae4a011286c1e762a38575773381d33fa1c79cb1b94df8bdba54b40c52c5861ab865934f1d3a3a225c1ef5758a698a9e587b0779d76a0a34'
            '4814fa3178d5f37b5422dcfa73b53f94492863e958987590796ea1a5a5df85977033aa2064e2cd6b2b813908751d8f9982e5103b6615d5b60d521d720340483b'
            '76139b58517487d5f8ae92aad5b2d4702597987b2f3ad17186c4e725bd13cf331225584972d8b1897bccd39ffd378edc39e17f5530e3cb535a6f079f85ebaaf8'
            'de24901d68d4d979e8027c5cac0f421f4bde82d464e1ae4f17b32264b5d4598c37d041faca3328a42323e18c8bf3e59ae4391e9f86650166be66480451c0539f'
            '22ab41d8d32faa3b3538d9a931c2733d4efcee9b80ca91bb69798979d3a7c9f083ed79b40915545adaf84de2f8c2dcd648fc3f60972ae9849edab3fd28b82d32'
            '46036e523f480029bd5bc7f18b2798ff8961d5da9a2753a537992a6a9d4e0284a0c1765c7672313a687ed0368ee78f5ff837fdf2e3cd35c481acf6a22267c580'
            '609a5a6f4fc75b9662df21a81f67ab290dc0b153bbf1433818a67975e0b8ed85e407c1f1cb7834f190580c5575e1ffc902ff27e9138ffe1568e5a6a2fc64540a'
            '43981e4a77be2a2049575884edf1ffb85bcc520a80454ae9b5a51c3f8a2616579c85e33834892ad1078e63b275a2c5e28c046b3c2cfc32589f23dcf449f6ce52'
            '0f24fa0a83228d6a940f52b0d7b8f449df969acd48335b3ede23a573bc396707f2ed4f93281811b834725f3aab597bc129ee4b368ab6638342e8074f82de301b'
            'e650ad1351107aef023420bcb7422279efb1f2594362e66b737c960e2a1a5444f4925449ecae5b4ffa3a0127d6645f9d466f3b5d17767c865dcaf438b3b0e44f'
            'abc52d3821deb9b34779c7bea2a3512a2bb015982fa1c196a2da75a74d8bf4d6766402dfb620d34b2eb9e117c1c9e9acc2f579c8acb15a1389d40fe0c5d1c93a'
            '5b1762bb1b3f01d23d7df14a0773f34fb0b751c013220e5e105916375ff8f094fb5821f2dbdc3c90ec5d10552dc6e8e15c4491ab239f0e5123eec51a2527ec70'
            'dcbf893a99ad1ad8c4868481eea1921c465737cb09b36fc7cafcdee6b0ec9c8b701051e2a17e215ed9b368d79c72b4a752c532e1ddd565602c0d58782b7cb4a7')

prepare() {
  # xscreensaver-6.12 tarball has duplicates that will not work with bsdtar - workaround
  tar -zxf "${pkgname}-${pkgver}.tar.gz"

  local logos_png
  local logos

  cd "${srcdir}"
  logos_png=(logo-32.png
             logo-50.png
             logo-180.png
             logo-360.png)
  for _pngfile in "${logos_png[@]}"; do
	install -Dm0644 "${_pngfile}" "${srcdir}/${pkgname%%-*}-${pkgver}/hacks/images/${_pngfile}"
  done
  
  logos=(logo.pdf
         logo-50.gif
         logo-50.xpm
         logo-180.gif
         logo-180.xpm
         logo-360.gif
         logo-360.xpm
         logo-512.png
         logo-big.gif)
  for _file in "${logos[@]}"; do
	install -Dm0644 "${_file}" "${srcdir}/${pkgname%%-*}-${pkgver}/utils/images/${_file}"
  done
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
      --with-pam \
      --with-login-manager \
      --with-gtk \
      --with-gl \
      --without-gle \
      --with-pixbuf \
      --with-jpeg \
      --with-systemd \
      --enable-pam-check-account-type \
      --with-wayland=no
  make
}

package() {
  cd "${pkgname%%-*}-${pkgver}"
  install -d "${pkgdir}/etc/pam.d"
  make install_prefix="${pkgdir}" install
  install -vDm0644 ../LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
