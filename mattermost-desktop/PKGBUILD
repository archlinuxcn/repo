# Maintainer: Aleksandar Trifunović <akstrfn at gmail dot com>
# Maintainer: William Gathoye <william at gathoye dot be>
# Contributor: Jan Was <janek dot jan at gmail dot com>

pkgname=mattermost-desktop
pkgver=4.1.1
pkgrel=1
pkgdesc="Mattermost Desktop application for Linux (Beta)"
arch=('i686' 'x86_64')
url="https://github.com/mattermost/desktop"
license=('Apache')
depends=('electron')
makedepends=('npm' 'git')
source=("https://github.com/mattermost/desktop/archive/v${pkgver}.tar.gz"
        "$pkgname.sh"
        "Mattermost.desktop")
sha512sums=('0a31dbbaca5b8bf22ee18fd08081546886f4b061b320b89bc59e31038a0465b6a44d62658f34af0bf2dc92630a4bcbee1bed11daaea8d5045d6a8786cbdba462'
            'c766a3522c5d2a5ecc9a4ded351147a87fbaaa6af1c2f6e8068baf8239ceb4299e98b81e9e51fd972ab09ed36843565c8b82f8819a949ba1d82ca78631f9f5fc'
            '5fc51cd6ee2e77a8e40736612a23e38b4649f4a2cc45f90f92fae73c396ee9d74dc5e743773fc376b52b268b482a2449212616fb4864fd79dca507d34b45c6a9')

prepare() {
    cd "${srcdir}/desktop-${pkgver}"

    # Depending on the architecture, in order to accelerate the build process,
    # removes the compilation of ia32 or x64 build.
    if [[ "$CARCH" == x86_64 ]];then
        sed -i 's/--ia32//g' package.json
    else
        sed -i 's/--x64//g' package.json
    fi

    # Reduce build time by removing the creation of a .deb for Debian
    sed -i -e '/"deb",/d' electron-builder.json
    # No need to compress the package
    sed -i 's/tar.gz/dir/' electron-builder.json
}

build() {
    cd "${srcdir}/desktop-${pkgver}"

    # Hack (npm bug? https://github.com/npm/npm/issues/19989)
    {
        npm install --cache "${srcdir}/npm-cache"
    } || {
        npm install --cache "${srcdir}/npm-cache"
    } || {
        npm install --cache "${srcdir}/npm-cache" 
    }
    npm run build --cache "${srcdir}/npm-cache"
    npm run package:linux --cache "${srcdir}/npm-cache"
}

package() {
    cd "${srcdir}/desktop-${pkgver}"

    install -d -m 755 "${pkgdir}"/usr/lib
    cp -r release/linux*unpacked/resources "$pkgdir/usr/lib/mattermost-desktop"

    install -d -m 755 "$pkgdir/usr/bin"
    install -D -m 755 "$srcdir/$pkgname.sh" "$pkgdir/usr/bin/mattermost-desktop"

    install -Dm644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

    install -Dm644 "$srcdir"/Mattermost.desktop "$pkgdir/usr/share/applications/$pkgname.desktop"
    install -Dm644 "$srcdir/desktop-$pkgver/release/linux-unpacked/icon.png" "$pkgdir/usr/share/pixmaps/$pkgname.png"
}

