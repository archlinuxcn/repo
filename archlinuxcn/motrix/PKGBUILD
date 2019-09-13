#Maintainer: weearc <q19981121@163.com>
pkgname=motrix
_pkgname=Motrix
pkgver=v1.4.1
_pkgver=1.4.1
pkgrel=7
epoch=
pkgdesc="elegent downloading tool frontend for aria2c,using vue(release version)"
arch=("x86_64")
url="https://github.com/agalwood/Motrix"
license=('MIT')
groups=()
depends=(
	 'gtk3'
	 'libxcb'
	)
makedepends=('curl'
	     'yarn'
	     'npm')
checkdepends=()
optdepends=()
provides=()
conflicts=('motrix-git')
replaces=()
backup=()
options=()
install=
changelog=
source=("Motrix.desktop"
	"aria2.conf"
	"motrix"
	"Motrix.tar.gz"::"https://github.com/agalwood/Motrix/archive/v$_pkgver.tar.gz")
noextract=()
sha256sums=('1b799d1b1e280a27ff625cceb429b1e00c6691eb0256ded44f6a1a0310a899d4'
	'1d87b2906dd9622efcdd3695d19fd4d365f644c53dac8b517931964d4099d2c3'
	'c89824e80769b0b19c66da12168f9e91fc15088d1324d6760ddad960eb006cba'
	'cd10cd5c704f0d780ff501e2861a316b95c44d11b653045574ae07b9a3ccaa8b')
validpgpkeys=()

prepare() {
	tar -xvf $_pkgname.tar.gz
	rm $_pkgname.tar.gz
	mv $_pkgname-$_pkgver $_pkgname
	echo "====================================="
	echo "Finding if you are in China..."
	curl https://myip.ipip.net | grep -i "中国"
	if [ $? -eq 0 ]
	then
		echo "Yes,I'm sure you are in China."
		echo "To speed up installation I'll change npm mirrors to Taobao."
		npm config set registry 'https://registry.npm.taobao.org'
		export ELECTRON_MIRROR='https://npm.taobao.org/mirrors/electron/'
		export SASS_BINARY_SITE='https://npm.taobao.org/mirrors/node-sass'
	else
		curl https://myip.ipip.net | grep -i "China"
		if [ $? -eq 0 ]
		then
			echo "Yes,I'm sure you are in China."
			echo "To speed up installation I'll change npm mirrors to Taobao."
                	npm config set registry 'https://registry.npm.taobao.org'
                	export ELECTRON_MIRROR='https://npm.taobao.org/mirrors/electron/'
                	export SASS_BINARY_SITE='https://npm.taobao.org/mirrors/node-sass'
		fi
	fi
	echo "======================================"
	sed -i '/"dmg"/,/"linux"/{//!d}' $_pkgname/package.json
	sed -i '/"dmg"/d' $_pkgname/package.json
	sed -i '/"deb"/d' $_pkgname/package.json
	sed -i '/"snap"/d' $_pkgname/package.json
	sed -i '/"pacman"/d' $_pkgname/package.json
	sed -i '/"rpm"/d' $_pkgname/package.json
	sed -i 's/"AppImage"/"dir"/g' $_pkgname/package.json

}

build() {
	cd $_pkgname/
	yarn
 	yarn run build
}
package() {
	install -d ${pkgdir}/opt
	install -d ${pkgdir}/usr/bin
	install -d ${pkgdir}/usr/share/icons
	install -d ${pkgdir}/usr/share/applications
	mv ${srcdir}/$_pkgname/release/linux-unpacked/ ${pkgdir}/opt/motrix
	install -Dm644 ${srcdir}/$_pkgname/build/256x256.png ${pkgdir}/usr/share/icons/$pkgname.png
	install -Dm 777 ${srcdir}/motrix ${pkgdir}/usr/bin
	install -Dm 644 ${srcdir}/Motrix.desktop ${pkgdir}/usr/share/applications
	rm ${pkgdir}/opt/motrix/resources/engine/aria2.conf
	cp -p ${srcdir}/aria2.conf ${pkgdir}/opt/motrix/resources/engine/aria2.conf
	rm -rf ${srcdir}
}
