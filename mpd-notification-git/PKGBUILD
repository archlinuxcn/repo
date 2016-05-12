# Maintainer: Christian Hesse <mail@eworm.de>

pkgname=mpd-notification-git
pkgver=0.7.0.r0.g14c059a
pkgrel=1
pkgdesc='Notify about tracks played by mpd - git checkout'
arch=('i686' 'x86_64')
url='https://github.com/eworm-de/mpd-notification'
depends=('ffmpeg' 'libnotify' 'libmpdclient' 'gnome-icon-theme')
makedepends=('git' 'markdown')
conflicts=('mpd-notification')
provides=('mpd-notification')
license=('GPL')
source=('git://github.com/eworm-de/mpd-notification.git')
sha256sums=('SKIP')

pkgver() {
	cd mpd-notification/

	if GITTAG="$(git describe --abbrev=0 --tags 2>/dev/null)"; then
		printf '%s.r%s.g%s' \
			"$(sed -e "s/^${pkgname%%-git}//" -e 's/^[-_/a-zA-Z]\+//' -e 's/[-_+]/./g' <<< ${GITTAG})" \
			"$(git rev-list --count ${GITTAG}..)" \
			"$(git log -1 --format='%h')"
	else
		printf '0.r%s.g%s' \
			"$(git rev-list --count master)" \
			"$(git log -1 --format='%h')"
	fi
}

build() {
	cd mpd-notification/

	make
}

package() {
	cd mpd-notification/

	make DESTDIR="${pkgdir}" install
}

