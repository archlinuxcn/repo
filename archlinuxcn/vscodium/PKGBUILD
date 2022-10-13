# Maintainer: Cedric Roijakkers <cedric [the at sign goes here] roijakkers [the dot sign goes here] be>.
# Inspired from the PKGBUILD for vscodium-bin and code-stable-git.

pkgname=vscodium
# Make sure the pkgver matches the git tags in vscodium and vscode git repo's!
pkgver=1.72.2.22286
pkgrel=1
pkgdesc="Free/Libre Open Source Software Binaries of VSCode (git build from latest release)."
arch=('x86_64' 'aarch64' 'armv7h')
url='https://github.com/VSCodium/vscodium.git'
license=('MIT')

depends=(
    'fontconfig'
    'libxtst'
    'gtk3'
    'cairo'
    'alsa-lib'
    'nss'
    'libnotify'
    'libxss'
    'glibc>=2.28-4'
    'libxkbfile'
)
optdepends=(
    'gvfs: For move to trash functionality'
    'libdbusmenu-glib: For KDE global menu'
)
makedepends=(
    'nvm'
    'gulp'
    'yarn'
    'jq'
    'libxdmcp'
    'git'
    'git-lfs'
    'patch'
    'python'
    'pkg-config'
)
source=(
    "${pkgname}.desktop"
    "${pkgname}-uri-handler.desktop"
    "https://github.com/VSCodium/vscodium/releases/download/${pkgver}/VSCodium-${pkgver}-src.tar.gz"
)
sha256sums=('63eccd0977b9dc783a11ff401940f48bbabd0d098b9563b7ef26402495dc9b88'
            'fd3dc7cbea2b3eb74dc205f8faa28e913108d11aba41fcffe19a4e5222be33fd'
            '2e233d8e850f5cde5f9d5600bb6b73fdfe86252feed312b5c11cb98c17f5debe')
provides=(
    'codium'
    'vscodium'
)
conflicts=(
    'codium'
    'vscodium'
    'vscodium-bin'
    'vscodium-git'
)

###############################################################################

# Even though we don't officially support other archs, let's allow the
# user to use this PKGBUILD to compile the package for their architecture.
case "$CARCH" in
  x86_64)
    _vscode_arch=x64
    ;;
  aarch64)
    _vscode_arch=arm64
    ;;
  armv7h)
    _vscode_arch=arm
    ;;
  *)
    # Needed for mksrcinfo
    _vscode_arch=DUMMY
    ;;
esac

build() {
    # Deactivate any pre-loaded nvm, and make sure we use our own in the current source directory
    command -v nvm >/dev/null && nvm deactivate && nvm unload
    export NVM_DIR="${srcdir}/.nvm"
    source /usr/share/nvm/init-nvm.sh || [[ $? != 1 ]]

    # Install the correct version of NodeJS (read from .nvmrc)
	nvm install $(cat .nvmrc)
    nvm use

    # Check if the correct version of node is being used
    if [[ "$(node --version)" != "$(cat .nvmrc)" ]]
    then
    	echo "Using the wrong version of NodeJS! Expected ["$(cat .nvmrc)"] but using ["$(node --version)"]."
    	exit 1
    fi

    # Remove old build
    if [ -d "vscode" ]; then
        rm -rf vscode* VSCode*
    fi

    # Export necessary environment variables
    export SHOULD_BUILD="yes"
    export SHOULD_BUILD_REH="no"
    export CI_BUILD="no"
    export OS_NAME="linux"
    export VSCODE_ARCH="${_vscode_arch}"
    export VSCODE_QUALITY="stable"
    export RELEASE_VERSION="${pkgver}"
    export BUILD_SOURCEVERSION=$( cat /dev/urandom | env LC_ALL=C tr -dc 'a-z0-9' | fold -w 40 | head -n 1 )
    # the app will be updated with pacman
    export DISABLE_UPDATE="yes"

    . get_repo.sh
    . build.sh
}

package() {
    install -d -m755 ${pkgdir}/usr/bin
    install -d -m755 ${pkgdir}/usr/share/{${pkgname},applications,pixmaps}
    install -d -m755 ${pkgdir}/usr/share/licenses/${pkgname}

    cp -r ${srcdir}/VSCode-linux-${_vscode_arch}/* ${pkgdir}/usr/share/${pkgname}
    cp -r ${srcdir}/VSCode-linux-${_vscode_arch}/resources/app/LICENSE.txt ${pkgdir}/usr/share/licenses/${pkgname}
    
    ln -s /usr/share/${pkgname}/bin/codium ${pkgdir}/usr/bin/codium
    ln -s /usr/share/${pkgname}/bin/codium ${pkgdir}/usr/bin/vscodium
    
    install -D -m644 ${pkgname}.desktop ${pkgdir}/usr/share/applications/${pkgname}.desktop
    install -D -m644 ${pkgname}-uri-handler.desktop ${pkgdir}/usr/share/applications/${pkgname}-uri-handler.desktop
    install -D -m644 ${srcdir}/VSCode-linux-${_vscode_arch}/resources/app/resources/linux/code.png ${pkgdir}/usr/share/pixmaps/${pkgname}.png

    # Symlink shell completions
    install -d -m755 ${pkgdir}/usr/share/zsh/site-functions
    install -d -m755 ${pkgdir}/usr/share/bash-completion/completions
    ln -s /usr/share/${pkgname}/resources/completions/zsh/_codium ${pkgdir}/usr/share/zsh/site-functions
    ln -s /usr/share/${pkgname}/resources/completions/bash/codium ${pkgdir}/usr/share/bash-completion/completions
}
