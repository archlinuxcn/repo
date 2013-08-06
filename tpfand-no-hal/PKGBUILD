# Maintainer: evr <evanroman @ gmail>
# Maintainer: Simon Legner <Simon.Legner@gmail.com>
# integrated patch from https://gist.github.com/3125216
# integrated systemd service file from https://bugs.launchpad.net/tp-fan/+bug/776547

pkgname=tpfand-no-hal
pkgver=0.94
pkgrel=6
pkgdesc="Monitors temperatures and controls fan speed of IBM/Lenovo ThinkPad notebooks (patched to work without HAL)."
arch=('any')
url="http://www.gambitchess.org/mediawiki/index.php/ThinkPad_Fan_Control"
license=('GPL3')
depends=(python2 dbus-python pygobject)
optdepends=(tpfan-admin tpfand-profiles)
source=(http://launchpad.net/tp-fan/tpfand/$pkgver/+download/tpfand-$pkgver.tar.gz tpfand.PMUTILS tpfand-nohal-sys.patch tpfand.service)
conflicts=(tpfand)
provides=(tpfand)

package() {
	cd "$srcdir/tpfand-$pkgver"

	patch -p0 < $srcdir/tpfand-nohal-sys.patch

	sed -i 's|#! /usr/bin/env python|#! /usr/bin/env python2|' src/tpfand/* wrappers/tpfand

	install -d "$pkgdir"/usr/lib/python2.7/site-packages/tpfand
	install -m644 src/tpfand/* "$pkgdir"/usr/lib/python2.7/site-packages/tpfand
	install -d "$pkgdir"/usr/share/tpfand/models/{by-id,by-name}
	install -m644 share/models/generic "$pkgdir"/usr/share/tpfand/models
	install -d "$pkgdir"/etc/dbus-1/system.d/
	install -m644 etc/dbus-1/system.d/* "$pkgdir"/etc/dbus-1/system.d/
	install -d "$pkgdir"/usr/bin
	install wrappers/tpfand "$pkgdir"/usr/bin/
	install -d "$pkgdir"/etc/modprobe.d
	install -m644 etc/modprobe.d/thinkpad_acpi.modprobe "$pkgdir"/etc/modprobe.d/thinkpad_acpi.conf
	if [ -e /etc/tpfand.conf ] 
	then install -m644 /etc/tpfand.conf "$pkgdir"/etc/tpfand.conf 
	else install -m644 etc/tpfand.conf "$pkgdir"/etc/tpfand.conf
	fi
	install -D -m755 $srcdir/tpfand.PMUTILS "$pkgdir"/etc/pm/sleep.d/09tpfand
	install -D -m644 $srcdir/tpfand.service "$pkgdir"/usr/lib/systemd/system/tpfand.service
}

md5sums=('fa08a5c3eebd47842e1fb84b6283416d'
         '353aa8a394f9f1762e70ecb7c6e623ef'
         '048c4c483feec1c106d2b3d42072e270'
         'c89c04e8e255fc93808b828975bec6d8')
sha1sums=('0f6cb53618f757b73d8b6e8627bcfaa17e2a1e7e'
          '8fa0c0d529a4213c75a841f7a63f0ce8284fd84d'
          '529d4e0cbdfb7352cfd7af275de6cb4bd93ef058'
          '7d5f5c7b4993c4f6b552126dc3776408e7b73e76')
