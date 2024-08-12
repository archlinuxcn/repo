# Maintainer: Manuel Hüsers <aur@huesers.de>
# Contributor: Iwan Timmer <irtimmer@gmail.com>
# Contributor: Timothée Ravier <tim at siosm dot fr>
# Contributor: Tom <reztho at archlinux dot org>

pkgbase=tuned
pkgname=("${pkgbase}" "${pkgbase}-ppd")
pkgver=2.24.0
pkgrel=1
pkgdesc='Daemon that performs monitoring and adaptive configuration of devices in the system'
arch=('any')
url="https://github.com/redhat-performance/${pkgbase}"
license=('GPL-2.0-or-later')
depends=('dbus-glib' 'ethtool' 'gawk' 'hdparm' 'polkit' 'python-configobj' 'python-dbus' 'python-gobject' 'python-linux-procfs' 'python-perf' 'python-pyudev')
makedepends=('desktop-file-utils')
source=("https://github.com/redhat-performance/${pkgbase}/archive/v${pkgver}/${pkgbase}-${pkgver}.tar.gz")
sha512sums=('d004cd621e26195fff14b39f29b2143cf47de09641454acd3029d61142c3d000a452f018356c84c32772bd99fc766f6ee847d2a8eddbde8ae34aaa0ecefa644e')

prepare() {
	cd "${pkgbase}-${pkgver}"
	mv libexec lib

	sed -i 's|/libexec/|/lib/|g' Makefile
	sed -i 's|/sbin/|/bin/|g' Makefile tuned.service tuned-gui.py tuned-gui.desktop tuned/ppd/tuned-ppd.service
	sed -i 's|install-ppd: install$|install-ppd: install-dirs|' Makefile
}

package_tuned() {
	optdepends=('virt-what: virtual machine detection'
		'systemtap: detailed system monitoring'
		'tuned-ppd: power-profiles-daemon api translation')
	backup=('etc/tuned/active_profile'
		'etc/tuned/bootcmdline'
		'etc/tuned/cpu-partitioning-powersave-variables.conf'
		'etc/tuned/cpu-partitioning-variables.conf'
		'etc/tuned/post_loaded_profile'
		'etc/tuned/profile_mode'
		'etc/tuned/realtime-variables.conf'
		'etc/tuned/realtime-virtual-guest-variables.conf'
		'etc/tuned/realtime-virtual-host-variables.conf'
		'etc/tuned/tuned-main.conf')
	install="${pkgbase}.install"

	cd "${pkgbase}-${pkgver}"

	make DESTDIR="${pkgdir}" install
	rm -rv "${pkgdir}"/{run,var}

	python -m compileall -d /usr/lib "${pkgdir}/usr/lib"
	python -O -m compileall -d /usr/lib "${pkgdir}/usr/lib"
}

package_tuned-ppd() {
	pkgdesc='Daemon that allows applications to easily transition to TuneD from power-profiles-daemon (PPD)'
	depends=('tuned')
	conflicts=('power-profiles-daemon')
	backup=('etc/tuned/ppd.conf')
	options=('!emptydirs')

	cd "${pkgbase}-${pkgver}"

	make DESTDIR="${pkgdir}" install-ppd
}
