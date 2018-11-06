#
# Maintainer: Sebastian Lau <lauseb644@gmail.com>
# Contributor Damian01w <damian01w@gmail.com>
# Contributor: Padfoot <padfoot@exemail.com.au>
#

pkgname=plymouth
pkgver=0.9.4
pkgrel=1
pkgdesc="A graphical boot splash screen with kernel mode-setting support"
url="http://www.freedesktop.org/wiki/Software/Plymouth/"
arch=('x86_64')
license=('GPL')

depends=('libdrm' 'pango' 'systemd')
makedepends=('docbook-xsl')
optdepends=('ttf-dejavu')
provides=('plymouth')
conflicts=('plymouth-git' 'plymouth-legacy' 'plymouth-nosystemd')
backup=('etc/plymouth/plymouthd.conf')

options=('!libtool' '!emptydirs')

source=("http://www.freedesktop.org/software/${pkgname}/releases/${pkgname}-${pkgver}.tar.xz"
        'arch-logo.png'
	'plymouth.encrypt_hook'
	'plymouth.encrypt_install'
	'gdm-plymouth.service'
	'lxdm-plymouth.service'
	'lightdm-plymouth.service'
	'slim-plymouth.service'
	'sddm-plymouth.service'
	'plymouth-deactivate.service'
	'plymouth-start.service'
	'plymouth-start.path'
	'plymouth.initcpio_hook'
	'plymouth.initcpio_install'
	'sd-plymouth.initcpio_install'
	'plymouth-quit.service.in.patch'
	'plymouth-update-initrd.patch')

md5sums=('4efa5551d230165981b105e7c6a50aa7'
         '65fa2763d5c9bb9f80973ea5e6e3db3e'
         'd67132b297ccfb1a877a2efd78076963'
         '02861a13840dee3a5f2224b598274220'
         'ae6e97bb1104bb12cbca6738e3fb872d'
         '1430ae2ec501d600f8f6771454dc9bbe'
         '870ea3e63c6989e2badf79d1fbafa914'
         'a3cfc30df846b2d7057a29e7fbe8733a'
         'f803c315739f46128b99232d64c268ca'
         '006847d16b852c7a50ee2f241fd9647e'
         '606cd558141551a1ce0d80150a045d83'
         '672ad913e2383483bcb4599a0a6bee48'
         '32f04fdbd1eb94ade30d1e63fdcdd9b5'
         'c17e915b19a469198a37dd7376a846c7'
         'af3c3eadc80e240416d11b2d5983dfb5'
         '165a39dbedcc6e123c8ca05d5b4b2e25'
         '0357775c16b5f90f1af485e6a4c80a9e')

prepare() {
	cd "$srcdir"/${pkgname}-${pkgver}
	patch -p1 -i $srcdir/plymouth-update-initrd.patch
	patch -p1 -i $srcdir/plymouth-quit.service.in.patch
}

build() {
	cd "$srcdir"/${pkgname}-${pkgver}

	LDFLAGS="$LDFLAGS -ludev" ./configure \
		--prefix=/usr \
		--exec-prefix=/usr \
		--sysconfdir=/etc \
		--localstatedir=/var \
		--libdir=/usr/lib \
		--libexecdir=/usr/lib \
		--sbindir=/usr/bin \
		--enable-systemd-integration \
		--enable-drm \
		--enable-tracing \
		--enable-pango \
		--enable-gtk=no \
		--with-release-file=/etc/os-release \
		--with-logo=/usr/share/plymouth/arch-logo.png \
		--with-background-color=0x000000 \
		--with-background-start-color-stop=0x000000 \
		--with-background-end-color-stop=0x4D4D4D \
		--without-rhgb-compat-link \
		--without-system-root-install

	make
}

package() {
  cd "$srcdir"/${pkgname}-${pkgver}

  make DESTDIR="$pkgdir" install

  install -Dm644 "$srcdir/arch-logo.png" "$pkgdir/usr/share/plymouth/arch-logo.png"

  install -Dm644 "$srcdir/plymouth.encrypt_hook" "$pkgdir/usr/lib/initcpio/hooks/plymouth-encrypt"
  install -Dm644 "$srcdir/plymouth.encrypt_install" "$pkgdir/usr/lib/initcpio/install/plymouth-encrypt"
  install -Dm644 "$srcdir/plymouth.initcpio_hook" "$pkgdir/usr/lib/initcpio/hooks/plymouth"
  install -Dm644 "$srcdir/plymouth.initcpio_install" "$pkgdir/usr/lib/initcpio/install/plymouth"
  install -Dm644 "$srcdir/sd-plymouth.initcpio_install" "$pkgdir/usr/lib/initcpio/install/sd-plymouth"

  for i in {gdm,sddm,lxdm,slim,lightdm}-plymouth.service; do
    install -Dm644 "$srcdir/$i" "$pkgdir/usr/lib/systemd/system/$i"
  done

  install -Dm644 "$srcdir/plymouth-deactivate.service" 	"$pkgdir/usr/lib/systemd/system/plymouth-deactivate.service"
  install -Dm644 "$srcdir/plymouth-start.service" "$pkgdir/usr/lib/systemd/system/plymouth-start.service"
  install -Dm644 "$srcdir/plymouth-start.path" 	"$pkgdir/usr/lib/systemd/system/plymouth-start.path"
  install -Dm644 "$pkgdir/usr/share/plymouth/plymouthd.defaults" "$pkgdir/etc/plymouth/plymouthd.conf"
}
