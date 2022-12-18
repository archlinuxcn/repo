# Maintainer: Geballin <macniaque [at] free [dot] fr>
# Maintainer: Morgenstern <charles [at] charlesbwise [dot] com>
# Contributor: Thomas Mudrunka <harvie [at] email [dot] cz>
# Contributor: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=xscreensaver-arch-logo
pkgver=6.06
pkgrel=1
pkgdesc="Screen saver and locker for the X Window System with Arch Linux branding"
url="https://www.jwz.org/${pkgname%%-*}/"
arch=('x86_64')
license=('BSD')
depends=('glu' 
         'gtk3'
         'libxmu'         
         'perl-libwww' 
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
sha512sums=('988e30d422ef985ac348c275e098ddfe1ee034a2e916c91690ee2836c908801c1e017e22d828aca981b0f8bfc5491cd83ab7c45aabc155ba5013df8b149cbcb5'
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
            '306f5b305c3e628e660d284d0e6cd5cf2ee939e01dccd7f1c91afe35e49c96f7697ef7e62678eb17647abdc2c7ae6105e33a290fe6b79dbca50b4f9e954b3b47'
            'b5172c09bbc65e5adf2ce4ca8c84391aec99cd1d5120380fa6f4878e2ec01a758f10d4ef89c78a93d2d2dd418a6054bdc1d532aac46c47f48cf803f0f83a863b'
            '376892f2dea54cd93c8e2f20ed76b0779ad2a038a6b590da189aedbd8c7fdd4d1f16add323a5f94e3772e0cc7e5ca74a74c20be3da54c637b76577a388e93fce')

prepare() {
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
	--with-jpeg
  make
}

package() {
  cd "${pkgname%%-*}-${pkgver}"
  install -d "${pkgdir}/etc/pam.d"
  make install_prefix="${pkgdir}" install
  install -Dm0644 ../LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
