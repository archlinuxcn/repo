# Maintainer: Hork <aliyuchang33@outlook.com>
# Contributer: ArielAxionL <i at axionl dot me>
# Contributor: DuckSoft <realducksoft@gmail.com>
pkgname=qv2ray-dev-git
pkgver=2.3.2.4981+grpc
pkgrel=1
pkgdesc="Cross-platform V2ray Client written in Qt (Development Release)"
arch=('x86_64')
url='https://github.com/Qv2ray/Qv2ray'
license=('GPL3')
depends=('hicolor-icon-theme' 'qt5-base>5.11.0' 'grpc>=1.27.0')
optdepends=('v2ray: use system v2ray core.')
makedepends=('git' 'make' 'qt5-tools' 'which' 'gcc' 'qt5-declarative'
             'grpc-cli>=1.27.0' 'cmake' 'ninja')
provides=('qv2ray')
conflicts=('qv2ray')

source=(
    'Qv2ray::git+https://github.com/Qv2ray/Qv2ray#branch=dev'
    'QNodeEditor::git+https://github.com/Qv2ray/QNodeEditor'
    'SingleApplication::git+https://github.com/itay-grudev/SingleApplication'
    'x2struct::git+https://github.com/xyz347/x2struct'
    'qzxing::git+https://github.com/ftylitak/qzxing'
    'qhttpserver::git+https://github.com/nikhilm/qhttpserver'
    'cpp-httplib::git+https://github.com/yhirose/cpp-httplib'
)

sha512sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

pkgver() {
    printf "%s.%s+grpc" $(cat ${srcdir}/Qv2ray/makespec/VERSION) $(cat ${srcdir}/Qv2ray/makespec/BUILDVERSION)
}

prepare() {
    cd "${srcdir}/Qv2ray"
    git submodule init
    submodules=('QNodeEditor' 'SingleApplication' 'x2struct' 'qhttpserver' 'qzxing' 'cpp-httplib')
    for module in ${submodules[@]}; do
        git config submodule."3rdparty/$module".url "${srcdir}/$module"
    done
    
    git config submodule."libs/libqvb".active false
    git submodule update
}

build() {
    export _QV2RAY_BUILD_INFO_="Qv2ray for Arch Linux CN"
    export _QV2RAY_BUILD_EXTRA_INFO_="(Official Build) $(uname -a | cut -d " " -f3,13)"

    cd "${srcdir}/Qv2ray"
    mkdir -p build && cd build
    cmake .. \
        -DCMAKE_INSTALL_PREFIX=${pkgdir}/usr \
        -DQV2RAY_TRANSLATION_PATH="/usr/share/qv2ray/lang" \
        -DQV2RAY_DEFAULT_VASSETS_PATH="/usr/lib/v2ray" \
        -DQV2RAY_DEFAULT_VCORE_PATH="/usr/lib/v2ray/v2ray" \
        -DQV2RAY_DISABLE_AUTO_UPDATE=on \
        -DCMAKE_BUILD_TYPE=Release \
        -GNinja
    ninja
}

package() {
    cd "${srcdir}/Qv2ray"
    ninja -C "build" install
}
