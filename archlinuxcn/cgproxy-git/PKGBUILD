# Maintainer: Fancy Zhang <springzfx@gmail.com>
pkgname=cgproxy-git
pkgver=v0.20.r0.g86fe42e
pkgrel=1
pkgdesc="A transparent proxy program powered by cgroup2 and tproxy"
arch=('x86_64')
url="https://github.com/springzfx/cgproxy"
license=('GPL')
groups=('')
makedepends=('cmake' 'nlohmann-json' 'clang' 'bpf' 'libbpf')
depends=('libbpf' 'iproute2' 'which')
provides=('cgproxy')
conflicts=('cgproxy')

source=("${pkgname}::git+https://github.com/springzfx/cgproxy#branch=master")
md5sums=('SKIP')

pkgver() {
  cd "$pkgname"
  ( set -o pipefail
    git describe --long --tags 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
  )
}

backup=('etc/cgproxy/config.json')
install="cgproxy.install"

build(){
    mkdir -p "${srcdir}/${pkgname}/build"
    cd "${srcdir}/${pkgname}/build"
    cmake -DCMAKE_BUILD_TYPE=Release \
          -DCMAKE_INSTALL_PREFIX=/usr \
          -Dbuild_execsnoop_dl=ON \
          -Dbuild_static=OFF \
          .. 
    make
}

package_cgproxy-git(){
    cd "${srcdir}/$pkgname"/build
    make DESTDIR=$pkgdir install
}


