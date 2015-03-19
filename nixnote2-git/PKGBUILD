# Maintainer: maz-1 <loveayawaka@gmail.com>

_pkgname=nixnote2
pkgname=$_pkgname-git
pkgver=411.7a8d856
pkgrel=1
pkgdesc="Nixnote2 is a C++ rewrite of nixnote,which is a clone of Evernote designed to run on Linux.Nixnote is formerly called nevernote."
arch=('x86_64' 'i686')
url="http://nevernote.sourceforge.net/"
license=('GPL2')
depends=('tidyhtml' 'opencv' 'hunspell'  'qtwebkit' 'sqlite' 'poppler-qt4' 'qt4')
makedepends=('git' 'boost')
provides=($_pkgname)
conflicts=($_pkgname 'nixnote-beta')
source=("git://github.com/baumgarr/$_pkgname.git")
sha256sums=('SKIP')
_gitname=$_pkgname

pkgver() {
	cd "$srcdir/$_gitname"
	echo "$(git rev-list --count HEAD).$(git describe --always)"
}
prepare() {
        rm -rf ${srcdir}/build
        mkdir ${srcdir}/build
}
build() {
	cd "${srcdir}/build"
	#sed -i "s:/usr/lib/x86_64-linux-gnu/qt4/bin/qmake:/usr/lib/qt4/bin/qmake:" ./Makefile
	#sed -i "s:CONFIG+=debug:CONFIG+=release:" ./Makefile
	#sed -i "s:QMAKE_CXXFLAGS +=-g -O2:QMAKE_CXXFLAGS +=-Os:" ./NixNote2.pro
        qmake-qt4 ../${_gitname}/NixNote2.pro
	make
}

package() {
	cd "$srcdir/build"
	#make DESTDIR="$pkgdir" install
	mkdir -p $pkgdir/usr/share/nixnote2
	mkdir -p $pkgdir/usr/bin
	mkdir -p $pkgdir/usr/share/applications
	install -m 755 ./nixnote2 $pkgdir/usr/bin/nixnote2
        cd "${srcdir}/${_gitname}"
	cp -R ./certs $pkgdir/usr/share/nixnote2
	cp -R ./help $pkgdir/usr/share/nixnote2
	cp -R ./images $pkgdir/usr/share/nixnote2
	cp -R ./qss $pkgdir/usr/share/nixnote2
	cp -R ./translations $pkgdir/usr/share/nixnote2
	lrelease-qt4 $pkgdir/usr/share/nixnote2/translations/*.ts
	rm $pkgdir/usr/share/nixnote2/translations/*.ts
	cp -R ./java $pkgdir/usr/share/nixnote2
	cp ./changelog.txt $pkgdir/usr/share/nixnote2
	cp ./copyright $pkgdir/usr/share/nixnote2
	cp ./gpl.txt $pkgdir/usr/share/nixnote2
	cp ./license.html $pkgdir/usr/share/nixnote2
	cp ./README.txt $pkgdir/usr/share/nixnote2
	cp ./shortcuts.txt $pkgdir/usr/share/nixnote2
	cp ./nixnote2.desktop $pkgdir/usr/share/applications
}
