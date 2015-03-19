# Maintainer: Somasis <somasissounds@gmail.com>
# Original Maintainer: evr <evanroman at gmail>
# Contributor: KRTac
# Contributor: BjÃ¶rn Pettersson <bjorn@hygiena.org>
# Contributor: Michael Reed <m.reed@mykolab.com>
# Contributor: Pyroh <supertron421@gmail.com>

pkgname=mpdscribble-git
pkgver=release.0.22.r9.g979e96a
pkgrel=1
pkgdesc="A mpd client which submits information to a scrobbler, such as last.fm."
arch=('i686' 'x86_64' 'armv5h' 'armv6h' 'armv7h')
url="http://mpd.wikia.com/wiki/Client:Mpdscribble"
license=('GPL')
depends=('curl' 'glib2' 'libmpdclient')
makedepends=('git')
conflicts=('mpdscribble')
provides=('mpdscribble')
install='mpdscribble.install'
source=('git://git.musicpd.org/master/mpdscribble.git'
		'mpdscribble.install'
		'mpdscribble.system.service'
		'mpdscribble.user.service')
md5sums=('SKIP'
         '8349de9fd06cd5d25b8e52446ea96e9a'
         '20a2313eaafe4e06a261ab58fe421b81'
         '8b63320901fbce6867db97fffe1fe1ce')


pkgver() {
	cd "$srcdir/mpdscribble"
	git describe --long | sed -r 's/([^-]*-g)/r\1/;s/-/./g'
}

build() {
	cd "$srcdir/mpdscribble"
	./autogen.sh --prefix="/usr" --sysconfdir="/etc"
	make
}

package() {
	cd "$srcdir/mpdscribble"
	make DESTDIR="$pkgdir" install
	if [ -f "$pkgdir/etc/mpdscribble.conf" ];then
		rm "$pkgdir/etc/mpdscribble.conf"
	fi
	install -D -m644 "${srcdir}"/mpdscribble/doc/mpdscribble.conf \
		"${pkgdir}"/etc/mpdscribble.conf.example

	install -Dm644 "${srcdir}"/mpdscribble.system.service \
	    "${pkgdir}"/usr/lib/systemd/system/mpdscribble.service

	install -Dm644 "${srcdir}"/mpdscribble.user.service \
	    "${pkgdir}"/usr/lib/systemd/user/mpdscribble.service

	mkdir -p "${pkgdir}"/var/cache/mpdscribble
	touch "${pkgdir}"/var/cache/mpdscribble/mpdscribble.cache
}
