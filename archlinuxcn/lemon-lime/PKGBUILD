# Maintainer: Coelacanthus <CoelacanthusHex@gmail.com>

pkgname=lemon-lime
pkgver=0.3.6
pkgrel=1
pkgdesc="为了 OI 比赛而生的基于 Lemon 的轻量评测系统 | A tiny judging environment for OI contest based on Project_LemonPlus"
arch=('x86_64' 'i686')
url="https://github.com/Project-LemonLime/Project_LemonLime"
license=('GPL-3.0-or-later')
depends=('gcc-libs'
         'glibc'
         'hicolor-icon-theme'
         'qt6-base'
         'xdg-utils'
         )
makedepends=('cmake'
             'git'
             'ninja'
             'qt6-tools'
             )
optdepends=('fpc: Pascal support'
            'freebasic: BASIC support'
            'gcc: C and C++ support'
            'java-environment: Java support'
            'python: Python support')
provides=('lemon-lime')
conflicts=('lemon-lime-git')

source=(Project_LemonLime::git+https://github.com/Project-LemonLime/Project_LemonLime.git#tag=$pkgver
        SingleApplication::git+https://github.com/itay-grudev/SingleApplication.git
        Testlib-for-Lemons::git+https://github.com/GitPinkRabbit/Testlib-for-Lemons.git
        )

b2sums=('e87fd91b2bee1ef72c4e372ff0081a72510a9073d7e47079099e2802d90e30870a76867edf0428077a457ec63ef8b556acb029030c48262142b5f815d5881893'
        'SKIP'
        'SKIP')

prepare() {
    cd "Project_LemonLime"
    git submodule init
    submodules=('SingleApplication')
    for module in ${submodules[@]}; do
        git config submodule."3rdparty/$module".url "${srcdir}/$module"
    done

    git config submodule."assets/Testlib-for-Lemons".url "${srcdir}/Testlib-for-Lemons"

    git -c protocol.file.allow=always submodule update
}

build() {
    cmake -S Project_LemonLime -B build \
        -DCMAKE_BUILD_TYPE=None \
        -GNinja \
        -DCMAKE_INSTALL_PREFIX="${pkgdir}/usr" \
        -DLEMON_BUILD_INFO="Build for Arch Linux" \
        -DLEMON_QT6=ON \
        -DEMBED_TRANSLATIONS=OFF \
        -DEMBED_DOCS=OFF
    ninja -C build

}

package() {
    ninja -C build install
}

# vim: set ts=4 sw=4 et:
