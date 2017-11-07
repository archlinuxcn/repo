# Maintainer: farseerfc <farseerfc@archlinuxcn.org>
# Contributor: Nyarcel <nyarcel AT SPAMFREE gmail DOT com>
# Contributor: Lara Maia <lara@craft.net.br>
# Contributor: BlackICE <manfredi at gmail.com>
# Contributor: Daenyth <Daenyth+Arch AT gmail DOT com>

pkgname=pkgtools
pkgver=25
pkgrel=8
pkgdesc="A collection of scripts for Arch Linux packages"
arch=('any')
url="https://bbs.archlinux.org/viewtopic.php?pid=384196"
license=('GPL')
depends=('coreutils'    # for comm in whoneeds
         'bash>=4'
         'pcre'
         'libarchive'
         'python')
optdepends=(
            'gem2arch: Create PKGBUILD from Ruby Gem Package'
            'pkgfile: Required to use pkgconflict'
            'namcap: Package analyzer')
provides=('newpkg' 'pip2arch')
backup=('etc/pkgtools/newpkg.conf'
        'etc/pkgtools/spec2arch.conf')
install=pkgtools.install
source=("${pkgname}-v${pkgver}.tar.gz::https://github.com/Daenyth/pkgtools/tarball/v$pkgver"
        "https://raw.githubusercontent.com/bluepeppers/pip2arch/master/pip2arch.py" # submodule issue
        'whoneeds.bash')
md5sums=('9e9d7aad5ba8ecee1b798c3ed4e0a0a7'
         '9267993a72489019ec1536c887304374'
         'ec05d3bd65bb492dfb7a528b3d42fbf5')

prepare() {
	cp -f pip2arch.py Daenyth-"$pkgname"-*/scripts/pip2arch/
}

package() {
	cp whoneeds.bash "$srcdir"/Daenyth-"$pkgname"-*/scripts/

	cd Daenyth-"$pkgname"-*

	make DESTDIR="$pkgdir" install
}
