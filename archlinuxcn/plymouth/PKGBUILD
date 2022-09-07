# Maintainer: Taijian <taijian@posteo.de>
# Contributor: Sebastian Lau <lauseb644@gmail.com>
# Contributor Damian01w <damian01w@gmail.com>
# Contributor: Padfoot <padfoot@exemail.com.au>
#

pkgname=plymouth
pkgver=22.02.122
pkgrel=4
pkgdesc="A graphical boot splash screen with kernel mode-setting support"
url="https://www.freedesktop.org/wiki/Software/Plymouth/"
arch=('i686' 'x86_64')
license=('GPL')

depends=('libdrm' 'pango' 'systemd')
makedepends=('docbook-xsl')
optdepends=('cantarell-fonts: For text output, e.g. during decryption'
        'xf86-video-fbdev: Support special graphic cards on early startup')
backup=('etc/plymouth/plymouthd.conf')

source=("https://gitlab.freedesktop.org/${pkgname}/${pkgname}/-/archive/${pkgver}/${pkgname}-${pkgver}.tar.gz"
      'arch-logo.png'
       'plymouth.encrypt_hook'
       'plymouth.encrypt_install'
       'lxdm-plymouth.service'
       'lightdm-plymouth.service'
       'sddm-plymouth.service'
       'plymouth-deactivate.service' # needed for sddm
       'plymouth.initcpio_hook'
       'plymouth.initcpio_install'
       'sd-plymouth.initcpio_install'
       'plymouth-quit.service.in.patch'
       'plymouth-update-initrd.patch'
       'plymouthd.conf.patch'
       'ply-utils.c.patch'
       'runstatedir.patch'
)

sha256sums=('8921cd61a9f32f5f8903ceffb9ab0defaef8326253e1549ef85587c19b7f2ab6'
            'de4369ad5a5511b684305e3a882c2c56204696514ea8ccdb556dd656eca062e7'
            '748e0cfa0e10ab781bc202fceeed46e765ed788784f1b85945187b0f29eafad7'
            '373ec20fe4c47e693a0c45cc06dd906e35dd1d70a85546bd1d571391de11763a'
            '06b31999cf60f49e536c7a12bc1c4f75f2671feb848bf5ccb91a963147e2680d'
            '86d0230d9393c9d83eb7bb430e6b0fb5e3f32e78fcd30f3ecd4e6f3c30b18f71'
            'c39f526f7e99173bc8f012900f53257537a25e2d8c19e23df630f1fe9a7627ba'
            '3b17ed58b59a4b60d904c60bba52bae7ad685aa8273f6ceaae08a15870c0a9eb'
            '2a80e2cad8de428358647677afa166219589d3338c5f94838146c804a29e2769'
            '9eab84d8748591798e89c9bd301de313e3f6884ccff9f5219102006146acd8f4'
            '50086877511c0890a2778359e969c1a390abec43b4401cbfad988465f09762bb'
            'dec28b86ddea93704f8479d33e08f81cd7ff4ccaad57e9053c23bd046db2278a'
            '74908ba59cea53c6a9ab67bb6dec1de1616f3851a0fd89bb3c157a1c54e6633a'
            '71d34351b4313da01e1ceeb082d9776599974ce143c87e93f0a465f342a74fd2'
            '1bd7693d1e135fe9e22a03f7635309e2ae616e952665d9774eb5ca4d82718e1b'
            '7c0224737119f949b8d5ca24c438f253b5734e3391a47e8f5f1dda28b8c4ab92')

prepare() {
	cd "$srcdir"/${pkgname}-${pkgver}
	patch -p1 -i $srcdir/plymouth-update-initrd.patch
	patch -p1 -i $srcdir/plymouth-quit.service.in.patch
	patch -p1 -i $srcdir/plymouthd.conf.patch
	# apply upstream patches
	patch -p1 -i $srcdir/ply-utils.c.patch
	patch -p1 -i $srcdir/runstatedir.patch
}

build() {
	cd "$srcdir"/${pkgname}-${pkgver}

	LDFLAGS="$LDFLAGS -ludev" ./autogen.sh \
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
		--without-system-root-install \
		--runstatedir=/run

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

	for i in {sddm,lxdm,lightdm}-plymouth.service; do
		install -Dm644 "$srcdir/$i" "$pkgdir/usr/lib/systemd/system/$i"
	done

	install -Dm644 "$srcdir/plymouth-deactivate.service" 	"$pkgdir/usr/lib/systemd/system/plymouth-deactivate.service"
	install -Dm644 "$pkgdir/usr/share/plymouth/plymouthd.defaults" "$pkgdir/etc/plymouth/plymouthd.conf"
}
