# Maintainer: DuckSoft <realducksoft@gmail.com>
# Contributor: ArielAxionL <i at axionl dot me>
# Contributor: Leroy.H.Y <me at lhy0403 dot top>
# Contributor: Neboer <rubinposter@gmail.com>
pkgname=qv2ray
pkgver=2.0.0
pkgrel=1
pkgdesc="Cross-platform V2ray Client written in Qt (Stable Release)"
arch=('x86_64')
url='https://github.com/Qv2ray/Qv2ray'
license=('GPL3')
depends=(
    'hicolor-icon-theme' 'qt5-charts>5.11.0'
)
optdepends=('v2ray' 'v2ray-domain-list-community' 'v2ray-geoip')
makedepends=('git' 'make' 'qt5-tools' 'which' 'gcc' 'qt5-declarative' 'go')
provides=('qv2ray')
conflicts=('qv2ray')

source=(
    'Qv2ray::git+https://github.com/Qv2ray/Qv2ray#tag=v2.0.0'
    'QNodeEditor::git+https://github.com/lhy0403/QNodeEditor#tag=v2.1.5'
    'SingleApplication::git+https://github.com/itay-grudev/SingleApplication#tag=v3.0.19'
    'x2struct::git+https://github.com/xyz347/x2struct#tag=v1.2'
    'qzxing::git+https://github.com/ftylitak/qzxing#commit=2a58c5032b2180f2cce95e1db106cbaa4ecaed02'
    'qhttpserver::git+https://github.com/nikhilm/qhttpserver#commit=02a6e7174b5be76e2c0e74a109817e39a141b9fd'
    'QvRPCBridge::git+https://github.com/Qv2ray/QvRPCBridge#tag=v1.1'
)

sha512sums=(
    'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP'
)

pkgver() {
    cd "${srcdir}/Qv2ray"
    printf "%s" $(git describe --long --tags | sed 's/v//;s/-\S*//g')
}

prepare() {
    cd "${srcdir}/Qv2ray"
    git submodule init
    submodules=('QNodeEditor' 'SingleApplication' 'x2struct' 'qzxing' 'qhttpserver')
    for module in ${submodules[@]}; do
        git config submodule."3rdparty/$module".url "${srcdir}/$module"
    done
    
    git config submodule."libs/libqvb".url "${srcdir}/QvRPCBridge"
    git config submodule."libs/gRPC-win32".active false
    git submodule update
}

build() {
    cd "${srcdir}/QvRPCBridge"
    chmod +x ./build.sh && ./build.sh
    ln -sf "${srcdir}/QvRPCBridge/build/libqvb.a" "${srcdir}/Qv2ray/libs/libqvb-linux64.a"

    cd "${srcdir}/Qv2ray"
    mkdir -p build && cd build
    qmake 'CONFIG += with_new_backend' 'DEFINES += QV2RAY_DEFAULT_VCORE_PATH=\\\"/usr/bin/v2ray\\\"' 'DEFINES += QV2RAY_DEFAULT_VASSETS_PATH=\\\"/usr/lib/v2ray\\\"' PREFIX=/usr ../
    make
}

package() {
    cd "${srcdir}/Qv2ray"
    install -Dm755 build/qv2ray "${pkgdir}/usr/bin/qv2ray"
    install -Dm644 assets/qv2ray.desktop "${pkgdir}/usr/share/applications/qv2ray.desktop"
    install -Dm644 assets/icons/qv2ray.png "${pkgdir}/usr/share/icons/hicolor/256x256/apps/qv2ray.png"
}
