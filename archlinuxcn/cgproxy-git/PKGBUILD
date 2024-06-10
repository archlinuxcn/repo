# Maintainer: Kimiblock
# Contributor: Fancy Zhang <springzfx@gmail.com>

pkgname=cgproxy-git
pkgver=0.20.r0.g86fe42ec
pkgrel=3
pkgdesc="A transparent proxy program powered by cgroup2 and tproxy"
arch=('x86_64')
url="https://github.com/springzfx/cgproxy"
license=('GPL-2.0-or-later')
makedepends=('cmake' 'nlohmann-json' 'clang' 'bpf' 'libbpf' "git")
depends=("libbpf" "iproute2" "which" "nftables" "iptables-nft" "bash" "glibc" "gcc-libs")
provides=('cgproxy')
conflicts=('cgproxy')

source=("${pkgname}::git+https://github.com/springzfx/cgproxy#branch=master")
md5sums=('SKIP')
backup=('etc/cgproxy/config.json')

function pkgver() {
	cd "${srcdir}/${pkgname}"
	git describe --long --tags --abbrev=8 | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

function prepare() {
	cd "${srcdir}/${pkgname}"
	
	# Cherry Pick Pull Request #52
	git cherry-pick -n d7990c0c2f1a1add5f863d35c670ec6aa720f1d3^..0b2c9a4c8264c2c4464ac38b12a60b96adf364f6
	git cherry-pick -n 3e68415864bacfe7fdbb73c08f403f867b440253
	git cherry-pick -n cb809d4033a0fb30ad22c03d98e0792793835f07
}

function build() {
	mkdir -p "${srcdir}/${pkgname}/build"
	cd "${srcdir}/${pkgname}/build"
	cmake -DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-Dbuild_execsnoop_dl=ON \
		-Dbuild_static=OFF \
		.. 
	make
}

function package() {
	cd "${srcdir}/${pkgname}"/build
	make DESTDIR="${pkgdir}" install
}


