# Maintainer: catsout <outline941 at live.com>
# Contributor: Epix <epixtm@protonmail.com>
# Contributor: Manuel Hüsers <aur@huesers.de>


pkgname=plasma6-wallpapers-wallpaper-engine-git
pkgver=0.5.4.r94.g641767d
pkgrel=1
pkgdesc="A simple kde wallpaper plugin integrating wallpaper engine"
arch=('x86_64')
url="https://github.com/catsout/wallpaper-engine-kde-plugin"
license=('GPL-2.0-only')
depends=(
    "plasma5support" "gst-libav" "python-websockets" "qt6-declarative"
    "qt6-websockets" "qt6-webchannel" "vulkan-driver" "libplasma"
    "kpackage" "qt6-5compat" "qt6-webengine" "qt6-multimedia"
    "plasma-workspace" "kdeclarative" "glfw"
)
makedepends=(
    "vulkan-headers" "extra-cmake-modules" "git" "cmake" "mpv"
)
optdepends=(
	"mpv: alternative video backend"
)
provides=("plasma6-wallpapers-wallpaper-engine")
conflicts=("plasma6-wallpapers-wallpaper-engine")
source=(
    "${pkgname}::git+${url}.git#branch=main"
    "backend_scene::git+https://github.com/catsout/wallpaper-scene-renderer.git"
    "git+https://github.com/KhronosGroup/glslang.git"
    "nlohmann::git+https://github.com/nlohmann/json.git"
    "git+https://github.com/KhronosGroup/SPIRV-Reflect.git"
    "Eigen::git+https://gitlab.com/libeigen/eigen.git"
    "git+https://github.com/mackron/miniaudio.git"
    "git+https://github.com/google/googletest.git"
)
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

prepare(){
    declare -ra modules=(
      "${srcdir}/${pkgname}" "${srcdir}/${pkgname}/src/backend_scene"
      "${srcdir}/${pkgname}/src/backend_scene/third_party/SPIRV-Reflect"
    )
    for p in "${modules[@]}"
    do
        cd "${p}"
        git submodule init
        grep submodule .gitmodules | sed 's/\[submodule "//;s/"\]//' | while read -r module
        do
            repo=$(basename "${module}")
            git config "submodule.${module}.url" "${srcdir}/${repo}"
        done
        git -c protocol.file.allow=always submodule update
    done
}
pkgver(){
    cd "${srcdir}/${pkgname}"
    git describe --tags --long | sed 's/v//;s/-/.r/;s/-/./g'
}
build(){
    echo "Building main program..."
    cmake -B build -S "${srcdir}/${pkgname}" \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_BUILD_TYPE=None \
        -DQT_MAJOR_VERSION=6 \
        -DBUILD_QML=ON \
        -DUSE_PLASMAPKG=OFF
    cmake --build build

    echo "Building sceneviewer..."
    cmake -B build-sceneviewer -S "${srcdir}/${pkgname}/src/backend_scene/standalone_view" \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_BUILD_TYPE=None \
        -DQT_MAJOR_VERSION=6 \
        -DBUILD_QML=ON
    cmake --build build-sceneviewer
}
package(){
    DESTDIR="${pkgdir}" cmake --install build
    install -Dm755 build-sceneviewer/sceneviewer \
        "${pkgdir}/usr/bin/sceneviewer"
    install -Dm755 build-sceneviewer/sceneviewer-qml \
        "${pkgdir}/usr/bin/sceneviewer-qml"
}
