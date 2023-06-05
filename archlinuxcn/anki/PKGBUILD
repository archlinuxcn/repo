# Maintainer: Alexander Bocken <alexander@bocken.org>
# Contributor: Posi <posi1981@gmail.com>
# Contributor: Johannes Löthberg <johannes@kyriasis.com>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Timm Preetz <timm@preetz.us>
# Contributor: Michael 'manveru' Fellinger <m.fellinger@gmail.com>
# Contributor: Dave Pretty <david dot pretty at gmail dot com>

pkgname=anki
pkgver=2.1.65
pkgrel=1
pkgdesc="Helps you remember facts (like words/phrases in a foreign language) efficiently"
url="https://apps.ankiweb.net/"
license=('AGPL3')
arch=('x86_64')
conflicts=('anki-bin' 'anki-git' 'anki-official-binary-bundle' 'anki-qt5')
depends=(
    # anki & aqt
    'python>=3.9'
    'python-beautifulsoup4'
    'python-waitress>=2.0.0'
    'python-requests'

    # anki
    'python-decorator'
    'python-markdown'
    'python-orjson'
    'python-protobuf>=4.21'
    'python-pysocks'
    'python-distro'

    #aqt
    'python-flask-cors' # python-flask required for anki & aqt but a dependency of -cors
    'python-jsonschema'
    'python-send2trash'
    'python-certifi'
    'qt6-multimedia'	# recording voice
    'python-pyqt6-webengine>=6.2'
    'qt6-svg'
)
makedepends=(
    'rsync'
    'ninja'
    'git'
    'cargo'
    'python-installer' # TODO: could use either wheel or installer, both are not needed afaik
    'python-wheel'
    'libxcrypt-compat'
    'nodejs'
    'yarn'
    'mold'
)
optdepends=(
    'lame: record sound'
    'mpv: play sound. prefered over mplayer'
    'mplayer: play sound'
    'texlive-most: render LaTex in cards'
)
changelog="$pkgname.changelog"
# (adjust in respective functions as well)
# anki -> git rev-parse $pkgver --short=8
# ftl -> git submodule
_tag_ftl_core="25c97e48acf6626f0b8bc9daede14e21a83cdaf2"
_tag_ftl_desktop="1fbf87bb8a7d441482e79b3b8c2e06479e9fa978"
source=("$pkgname-$pkgver.tar.gz::https://github.com/ankitects/anki/archive/refs/tags/${pkgver}.tar.gz"
        "anki-core-i18n-${_tag_ftl_core}.tar.gz::https://github.com/ankitects/anki-core-i18n/archive/${_tag_ftl_core}.tar.gz"
        "anki-desktop-ftl-${_tag_ftl_desktop}.tar.gz::https://github.com/ankitects/anki-desktop-ftl/archive/${_tag_ftl_desktop}.tar.gz"
        "disable-git-checks.patch"
        "no-update.patch"
        "strip-formatter-deps.patch"
        "strip-type-checking-deps.patch"
)
sha256sums=('ca1c37e8e32bec02f09421bd29ac67253e4039e705bf9fba919918c4559b48e8'
            '9fe9d498d89d25db3a5b0938c58dc3a584c97e09ccd83a622574df8bb0935841'
            '85c6f4570b66cac1a021eb3efb7e69868d8c9b130b5c6171d459dd5bfbde321a'
            '89f1d00764e0f151600f6a21d7ced4289b3ce3f900ded40fe5da95e658fc9db4'
            'f934553a5ce9e046a0b8253e10da16e661b27375e2b54d6bb915267f32aff807'
            '9858fefa254812980d252b29fc6f32bd19bb83ee7e5a96d72c707626ed5193a7'
            '0df3992e007564433c1f4995959d0023b8ed238a36d4dc345d7626cca1c515e1'
)

prepare() {
    _yc="$srcdir/yarn-cache"
    _ch="$srcdir/cargo-cache"
    _tag_anki="141bc18b"
    _tag_ftl_core="25c97e48acf6626f0b8bc9daede14e21a83cdaf2"
    _tag_ftl_desktop="1fbf87bb8a7d441482e79b3b8c2e06479e9fa978"
    cd "$pkgname-$pkgver"

    patch -p1 < "$srcdir/no-update.patch"
    patch -p1 < "$srcdir/strip-formatter-deps.patch"
    patch -p1 < "$srcdir/strip-type-checking-deps.patch"
    patch -p1 < "$srcdir/disable-git-checks.patch"
    sed -i 's/opt-level = 1$/opt-level= 3/' Cargo.toml	# optimize more
    sed -i 's/channel = "[0-9\.]*"$/channel = "stable"/' rust-toolchain.toml # use most recent stable rust toolchain
    # Build process wants .git/HEAD to be present. Workaround to be able to use tarballs
    # (together with disable-git-checks.patch)
    mkdir -p .git
    touch .git/HEAD
    sed -i "s/MY_REV/${_tag_anki}/" build/runner/src/build.rs

    # place translations in build dir
    rm -r ftl/core-repo ftl/qt-repo
    ln -sT "${srcdir}"/anki-core-i18n-${_tag_ftl_core} ftl/core-repo
    ln -sT "${srcdir}"/anki-desktop-ftl-${_tag_ftl_desktop} ftl/qt-repo

    #force update for 'rustup' package users (not necesarry for 'cargo' package user)
    pacman -Qo $(which cargo) | grep -q rustup && rustup update
    # fetch rust packages
    export CARGO_HOME="$_ch"       # do not litter in ~
    cargo fetch --locked --target "$CARCH-unknown-linux-gnu"

    # fetch node packages already in prepare()
    export YARN_CACHE_FOLDER="$_yc" # do not litter in ~
    yarn install --immutable --modules-folder out/node_modules --ignore-scripts
    ln -sf out/node_modules ./

    # mask pip-sync as we provide dependencies ourselves
    local venv="out/pyenv"
    python -m venv --system-site-packages --without-pip "$venv"
    printf '#!/bin/bash\nexit 0' > "$venv/bin/pip-sync"
    chmod +x "$venv/bin/pip-sync"
}

build() {
    _yc="$srcdir/yarn-cache"
    _ch="$srcdir/cargo-cache"
    cd "$pkgname-$pkgver"

    export YARN_CACHE_FOLDER="$_yc" # do not litter in ~
    yarn run --offline postinstall

    #use local binaries instead of downloading them
    export PYTHON_BINARY=$(which python)
    export PROTOC_BINARY=$(which protoc)
    export NODE_BINARY=$(which node)
    export YARN_BINARY=$(which yarn)

    export CARGO_HOME="$_ch"    # do not litter in ~
    export RELEASE=1	        # anki-internal variable for optimization
    mold -run ./ninja wheels -v # use mold as linker to allow for LTO
}

package() {
    cd "$pkgname-$pkgver"
    for file in out/wheels/*.whl; do
    	python -m installer --destdir="$pkgdir" $file
    done

    install -Dm644 qt/bundle/lin/anki.desktop "$pkgdir"/usr/share/applications/anki.desktop
    install -Dm644 qt/bundle/lin/anki.png "$pkgdir"/usr/share/pixmaps/anki.png
}
