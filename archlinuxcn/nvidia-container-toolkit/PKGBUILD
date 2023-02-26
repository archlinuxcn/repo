# Maintainer: Kien Dang <mail at kien dot ai>
# Maintainer: Julie Shapiro <jshapiro at nvidia dot com>

pkgname=nvidia-container-toolkit

pkgver=1.12.0
pkgrel=2

pkgdesc='NVIDIA container runtime toolkit'
arch=('x86_64')
url='https://github.com/NVIDIA/nvidia-container-toolkit'
license=('Apache')

makedepends=('go')
depends=('libnvidia-container-tools>=1.9.0')
conflicts=('nvidia-container-runtime-hook' 'nvidia-container-runtime<2.0.0')
replaces=('nvidia-container-runtime-hook')
options=(!lto)

backup=('etc/nvidia-container-runtime/config.toml')

source=("v${pkgver}-${pkgrel}.tar.gz"::"${url}/archive/v${pkgver}.tar.gz")
sha256sums=('b84dbc28dabd8c8d3731e60d75002619f55422d3930d399fb66677c7875e384f')

_srcdir="nvidia-container-toolkit-${pkgver}"

build() {
  cd "${_srcdir}"

  mkdir bin

  GO_LDFLAGS="-Wl,-z,lazy,${LDFLAGS}" \
  GO111MODULE=auto \
  GOPATH="${srcdir}/gopath" \
  go build -v \
    -modcacherw \
    -buildmode=pie \
    -gcflags "all=-trimpath=${PWD}" \
    -asmflags "all=-trimpath=${PWD}" \
    -ldflags "-s -w -extldflags=${GO_LDFLAGS/%,/}" \
    -o bin \
    "./..."
    # -trimpath \  # only go > 1.13
    #-ldflags " -s -w -extldflags=-Wl,-z,now,-z,relro" \

  # go leaves a bunch of local stuff with 0400, making it break future `makepkg -C` _grumble grumble_
  GO111MODULE=auto \
  GOPATH="${srcdir}/gopath" \
  go clean -modcache
}

package() {
  install -D -m755 "${_srcdir}/bin/nvidia-container-runtime-hook" "${pkgdir}/usr/bin/nvidia-container-runtime-hook"
  install -D -m755 "${_srcdir}/bin/nvidia-ctk" "${pkgdir}/usr/bin/nvidia-ctk"

  pushd "${pkgdir}/usr/bin/"
  ln -sf "nvidia-container-runtime-hook" "${pkgname}"
  popd
  install -D -m644 "${_srcdir}/config/config.toml.rpm-yum" "${pkgdir}/etc/nvidia-container-runtime/config.toml"
  install -D -m644 "${_srcdir}/oci-nvidia-hook.json" "${pkgdir}/usr/share/containers/oci/hooks.d/00-oci-nvidia-hook.json"

  install -D -m644 "${_srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
