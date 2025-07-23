# Maintainer: lilydjwg <lilydjwg@gmail.com>
# Contributor: Gaetan Bisson <bisson@archlinux.org>
# Contributor: Gerhard Brauer <gerhard.brauer@web.de>

pkgname=collectd
pkgver=5.12.0
pkgrel=19
pkgdesc='Daemon which collects system performance statistics periodically'
url='https://collectd.org/'
arch=('x86_64' 'aarch64')
license=('MIT AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-only AND ISC AND MIT-0')

optdepends=('curl: apache, ascent, curl, nginx, and write_http plugins'
            'libdbi: dbi plugin'
            'libesmtp: notify_email plugin'
            'libgcrypt: encryption and authentication for network plugin'
            'libmemcached: memcachec plugin'
            'mariadb-libs: mysql plugin'
            'systemd-libs: UdevNameAttr option'
            'iproute2: netlink plugin'
            'net-snmp: snmp plugin'
            'libnotify: notify_desktop plugin'
            'openipmi: ipmi plugin'
            'liboping: ping plugin'
            'libpcap: dns plugin'
            'perl: perl plugin'
            'postgresql-libs: postgresql plugin'
            'python: python plugin'
            'rrdtool: rrdtool and rrdcached plugins'
            'lm_sensors: lm_sensors and sensors plugins'
            'libvirt: libvirt plugin'
            'libxml2: ascent and libvirt plugins'
            'yajl: curl_json plugin'
            'libatasmart: smart plugin'
            'lvm2: lvm plugin'
            'protobuf-c: write_riemann plugin'
            'mosquitto: MQTT plugin'
            'libmicrohttpd: prometheus plugin'
            'librabbitmq-c: amqp plugin'
            'nut: nut plugin')

makedepends=(${optdepends[@]%:*})
depends=('libltdl' 'iptables' 'libnsl')

source=("https://storage.googleapis.com/collectd-tarballs/${pkgname}-${pkgver}.tar.bz2"
        https://github.com/collectd/collectd/commit/623e95394e0e62e7f9ced2104b786d21e9c0bf53.patch
        ansidecl.patch
        'service')
sha256sums=('5bae043042c19c31f77eb8464e56a01a5454e0b39fa07cf7ad0f1bfc9c3a09d6'
            '777544cbf803af4d08ea228b29619f8f6e7a4777a85e0fb30693d8240db7246b'
            '74088adbd378fd2942ab3b9a959fae110a38b9c411b82557df2b4d1276b61d20'
            '83957b0b2cc7fa05a4d5f22e6c913ae2b0a4d7821f7b4e2d2e763054cc8c6c21')

backup=('etc/collectd.conf')

prepare() {
	cd ${pkgname}-${pkgver}
	sed -i '/sys\/mount.h/d' src/utils/mount/mount.h
        patch -Np1 < ../623e95394e0e62e7f9ced2104b786d21e9c0bf53.patch
        patch -Np0 < ../ansidecl.patch
}

build() {
	cd ${pkgname}-${pkgver}
        # fix nut plugin build
        export CFLAGS="$CFLAGS -Wno-incompatible-pointer-types"
        # quick fix for https://github.com/collectd/collectd/issues/4310
        # libgcrypt-config is gone
        export GCRYPT_CPPFLAGS="$(pkg-config libgcrypt --cflags)"
        export GCRYPT_LIBS="$(pkg-config libgcrypt --libs)"
	./configure \
		--prefix=/usr \
		--sysconfdir=/etc \
		--localstatedir=/var \
		--sbindir=/usr/bin \
		--disable-werror \
		--with-perl-bindings='INSTALLDIRS=vendor' \

	make all V=1
}

package() {
	cd ${pkgname}-${pkgver}
	make DESTDIR="${pkgdir}" install
	rmdir "${pkgdir}/var/run" # FS#30201
	install -Dm644 ../service "${pkgdir}"/usr/lib/systemd/system/collectd.service
	install -Dm644 contrib/collectd2html.pl "${pkgdir}"/usr/share/collectd/collectd2html.pl
}
