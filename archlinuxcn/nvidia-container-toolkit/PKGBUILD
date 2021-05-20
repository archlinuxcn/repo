# Maintainer: Kien Dang <mail at kien dot ai>
# Maintainer: Julie Shapiro <jshapiro at nvidia dot com>

pkgname=nvidia-container-toolkit

pkgver=1.5.0
pkgrel=2

pkgdesc='NVIDIA container runtime toolkit'
arch=('x86_64')
url='https://github.com/NVIDIA/nvidia-container-toolkit'
license=('Apache')

makedepends=('go')
depends=('libnvidia-container-tools>=1.4.0')
conflicts=('nvidia-container-runtime-hook' 'nvidia-container-runtime<2.0.0')
replaces=('nvidia-container-runtime-hook')

source=(fix_cgroup.patch
        "v${pkgver}-${pkgrel}.tar.gz"::"${url}/archive/v${pkgver}.tar.gz")
sha256sums=('48a36a4b01ab64739d55c4a696bbe72f2b90a9e5abc0b9d1c4090a3016d9a1fb'
            'a233de640a69fa3ff1c0e5b929b6c37922b040471a02eb98b6cf209a0dcac107')

install=$pkgname.install

_srcdir="nvidia-container-toolkit-${pkgver}"
_golang_pkg_path="github.com/NVIDIA/nvidia-container-toolkit/pkg"

build() {
  cd "${_srcdir}"

  patch -Np1 -i "${srcdir}/fix_cgroup.patch"

  GOPATH="${srcdir}/gopath" \
  go build -v \
    -buildmode=pie \
    -gcflags "all=-trimpath=${PWD}" \
    -asmflags "all=-trimpath=${PWD}" \
    -ldflags "-s -w -extldflags ${LDFLAGS}" \
    -o "${pkgname}" \
    "${_golang_pkg_path}"
    # -trimpath \  # only go > 1.13
    #-ldflags " -s -w -extldflags=-Wl,-z,now,-z,relro" \

  # go leaves a bunch of local stuff with 0400, making it break future `makepkg -C` _grumble grumble_
  GOPATH="${srcdir}/gopath" \
  go clean -modcache
}

package() {
  install -D -m755 "${_srcdir}/${pkgname}" "$pkgdir/usr/bin/${pkgname}"

  pushd "$pkgdir/usr/bin/"
  ln -sf "${pkgname}" "nvidia-container-runtime-hook"
  popd
  install -D -m644 "${_srcdir}/config/config.toml.centos" "$pkgdir/etc/nvidia-container-runtime/config.toml"
  install -D -m644 "${_srcdir}/oci-nvidia-hook.json" "$pkgdir/usr/share/containers/oci/hooks.d/00-oci-nvidia-hook.json"

  install -D -m644 "${_srcdir}/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
