# Maintainer: S Stewart <tda@null.net>
# Maintainer: Cranky Supertoon <crankysupertoon@gmail.com>
pkgname="gdlauncher"
pkgver="1.1.20"
pkgrel=1
arch=('x86_64')
pkgdesc="GDLauncher is simple, yet powerful Minecraft custom launcher with a strong focus on the user experience"
url="https://gdevs.io"
license=('GPL3')
makedepends=('gendesk' 'nodejs' 'npm' 'rust')
depends=('libnotify' 'libxss' 'libxtst' 'libindicator-gtk3' 'libappindicator-gtk3' 'electron' 'p7zip')
conflicts=('gdlauncher-beta' 'gdlauncher-beta-bin' 'gdlauncher-appimage' 'gdlauncher-git' 'gdlauncher-bin' 'gdlauncher-appimage')
provides=('gdlauncher')
source=("https://github.com/gorilla-devs/GDLauncher/archive/refs/tags/v${pkgver}.tar.gz"
        "use-system-7za-and-disable-updater.patch")
md5sums=('4aea6eb0dadc828ac1bad2b64a05550a'
         '68c75869fe0898c54699b9a5eb667d7b')

prepare() {
    # Generate .desktop
    gendesk --pkgname "GDLauncher" --pkgdesc "${pkgdesc}" --icon ${pkgname} --exec "/usr/bin/${pkgname}" --categories "Application;Game" -n -f

    cd "${srcdir}/GDLauncher-${pkgver}/"

    # Apply patches, copied from ObserverOfTime's gdlauncher-git
    sed -i package.json \
        -e '/electron-updater/d;/7zip-bin/d' \
        -e 's$public/electron.js$build/electron.js$' \
        -e '/"dependencies"/i\  "bundledDependencies": ["7zip-bin"],' \
        -e 's/0.13.1/0.13.2/g' # bump dependency version
    patch -p1 -i "${srcdir}/use-system-7za-and-disable-updater.patch"

    # Create .git folder to stop Husky from crashing
    mkdir -p .git
}

build() {
    cd "${srcdir}/GDLauncher-${pkgver}/"

    # Install required npm packages
    npm install --cache="${srcdir}/npm-cache"

    # Build the program
    export CI=false \
        APP_TYPE=electron \
        NODE_ENV=production \
        REACT_APP_RELEASE_TYPE=setup
    npx craco build
    npx webpack --config ./scripts/electronWebpackConfig.js
}

package() {
    # Copy runtime files
    install -d -m755 "${pkgdir}/usr/lib/gdlauncher/"
    rm "${srcdir}/GDLauncher-${pkgver}/build/installer"{.nsh,{Header,Sidebar}.bmp}  # Unecessary install files
    cp -r "${srcdir}/GDLauncher-${pkgver}/"{package.json,build} "${pkgdir}/usr/lib/gdlauncher/"

    # Create run script
    install -d -m755 "${pkgdir}/usr/bin/"
    printf '#!/bin/sh\ncd /usr/lib/gdlauncher/\nexec electron . "$@"' > "${pkgdir}/usr/bin/gdlauncher"
    chmod a+x "${pkgdir}/usr/bin/gdlauncher"

    # Desktop entry
    install -d -m755 "${pkgdir}/usr/share/applications/"
    install -D -m644 "${srcdir}/GDLauncher.desktop" "${pkgdir}/usr/share/applications/GDLauncher.desktop"

    # Install icons
    cd "${srcdir}/GDLauncher-${pkgver}/public/linux-icons/"
    for icon in *.png; do
        install -d -m755 "${pkgdir}/usr/share/icons/hicolor/${icon::-4}/apps/"
        cp "$icon" "${pkgdir}/usr/share/icons/hicolor/${icon::-4}/apps/${pkgname}.png"
    done
}
