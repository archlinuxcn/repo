# $Id$
# Maintainer: Colin Keenan <colinkeenan at archlinuxcn dot org>
# Maintainer: Andreas Radke <andyrtr at archlinux dot org>
# Maintainer: Tom Gundersen <teg at jklm dot no>
# Contributor : Rémy Oudompheng <remy at archlinux dot org>
# Contributor: Morgan LEFIEUX <comete at archlinuxfr dot org>

pkgname=hplip-reverted-imageprocessor
_pkgname=hplip
pkgver=3.18.7
pkgrel=1
pkgdesc="Drivers (patched to remove use of libImageProcessor) for HP DeskJet, OfficeJet..."
arch=('x86_64')
url="http://hplipopensource.com"
conflicts=('hplip')
provides=('hplip=$pkgver')
license=('GPL2' 'custom')
depends=('python-dbus' 'ghostscript' 'net-snmp' 'foomatic-db-engine')
makedepends=('python-pyqt5' 'python-gobject' 'sane' 'rpcbind' 'cups' 'libusb')
optdepends=('cups: for printing support'
            'sane: for scanner support'
            'xsane: sane scanner frontend'
            'python-pillow: for commandline scanning support'
            'python-reportlab: for pdf output in hp-scan'
            'rpcbind: for network support'
            'python-pyqt5: for running GUI and hp-toolbox'
            'python-gobject: for running hp-toolbox'
            'libusb: for advanced usb support'
            'wget: for network support')
# 'hplip-plugin: binary blobs for specific devices (AUR) or run hp-setup to download the plugin'
backup=('etc/hp/hplip.conf' 'etc/sane.d/dll.d/hpaio')
source=(https://downloads.sourceforge.net/${_pkgname}/$_pkgname-$pkgver.tar.gz{,.asc}
        'disable_upgrade.patch::https://git.archlinux.org/svntogit/packages.git/plain/trunk/disable_upgrade.patch?h=packages/hplip'
        '0022-Add-include-cups-ppd.h-in-various-places-as-CUPS-2.2.patch::https://git.archlinux.org/svntogit/packages.git/plain/trunk/0022-Add-include-cups-ppd.h-in-various-places-as-CUPS-2.2.patch?h=packages/hplip'
        '0023-Fix-handling-of-unicode-filenames-in-sixext.py.patch::https://git.archlinux.org/svntogit/packages.git/plain/trunk/0023-Fix-handling-of-unicode-filenames-in-sixext.py.patch?h=packages/hplip'
        'fix_install.patch::https://git.archlinux.org/svntogit/packages.git/plain/trunk/fix_install.patch?h=packages/hplip'
        'python.patch::https://git.archlinux.org/svntogit/packages.git/plain/trunk/python.patch?h=packages/hplip'
        'hplip.patch::https://bugs.archlinux.org/task/59548?getfile=16673'
        )
sha1sums=('bb40807ac77fb9b1f6d80a53d5409a22f5d2d197'
          'SKIP'
          '2348bcbca0c52dc09cceb47ed13281a4ccb9d83e'
          '2ef86972ab51c0fdcb8bfc653b9f6f69459449a5'
          '0e36f31b98faf2f14137431bc8f82b74de22705b'
          '759de18bfef699ac2f605962dafee1431e7b5e3b'
          '72db2c60f63c9be2a98a46ec4bcccd3a8a5b935b'
          'e36daa9401ca546d8af1f801304e670ca635e0a3')
validpgpkeys=('4ABA2F66DBD5A95894910E0673D770CDA59047B9') # HPLIP (HP Linux Imaging and Printing) <hplip@hp.com>

prepare() {
 cd $_pkgname-$pkgver

 # disable insecure update - https://bugs.archlinux.org/task/38083
 patch -Np0 -i ${srcdir}/disable_upgrade.patch
 
 # revert libImageProcessor because it doesn't work with hplip-plugin
 patch -Np1 -i ${srcdir}/hplip.patch
 
 # add missing 'include <cups/ppd.h>' at various places
 patch -Np1 -i ${srcdir}/0022-Add-include-cups-ppd.h-in-various-places-as-CUPS-2.2.patch
 # fix some handling unicode file names FS#58412
 patch -Np1 -i ${srcdir}/0023-Fix-handling-of-unicode-filenames-in-sixext.py.patch
 # fix installation of missing library - FS#59548
 patch -Np1 -i ${srcdir}/fix_install.patch
 # fix python issue - FS#59548
 patch -Np1 -i ${srcdir}/python.patch

 export AUTOMAKE='automake --foreign'
 autoreconf --force --install
}

build() {
 cd $_pkgname-$pkgver
 ./configure --prefix=/usr \
             --enable-qt5 \
             --disable-qt4 \
             --enable-hpcups-install \
             --enable-cups-drv-install \
             --enable-pp-build #--help
 make
}

package() {
 cd $_pkgname-$pkgver
 make -j1 rulesdir=/usr/lib/udev/rules.d DESTDIR="$pkgdir/" install
 
 # remove config provided by sane and autostart of hp-daemon
 rm -rf "$pkgdir"/etc/{sane.d,xdg}
 install -dm755 ${pkgdir}/etc/sane.d/dll.d
 echo hpaio > ${pkgdir}/etc/sane.d/dll.d/hpaio
 
 # remove HAL .fdi file because HAL is no longer used
 rm -vrf "$pkgdir"/usr/share/hal
 
 # remove rc script
 rm -vrf "$pkgdir"/etc/init.d

 # add mixed license file
 install -Dt "${pkgdir}"/usr/share/licenses/${_pkgname} -m644 COPYING
}
