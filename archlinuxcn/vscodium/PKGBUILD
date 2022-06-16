# Maintainer: Cedric Roijakkers <cedric [the at sign goes here] roijakkers [the dot sign goes here] be>.
# Inspired from the PKGBUILD for vscodium-bin and code-stable-git.

pkgname=vscodium
# Make sure the pkgver matches the git tags in vscodium and vscode git repo's!
pkgver='1.68.1'
pkgrel=1
pkgdesc="Free/Libre Open Source Software Binaries of VSCode (git build from latest release)."
arch=('x86_64' 'aarch64' 'armv7h')
# The vscodium repo that will be checked out.
url='https://github.com/VSCodium/vscodium.git'
# The vscode repo that will also be checked out.
microsofturl='https://github.com/microsoft/vscode.git'
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
    "git+${url}#tag=${pkgver}"
    "git+${microsofturl}#tag=${pkgver}"
    'vscodium.desktop'
)
sha256sums=(
    'SKIP'
    'SKIP'
    '63eccd0977b9dc783a11ff401940f48bbabd0d098b9563b7ef26402495dc9b88'
)
provides=('codium')

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

prepare() {
    cd 'vscodium'
    # Normally, we would execute get_repo.sh to clone the Microsoft repo here, but makepkg can't do this.
    # So we rely on the clone that happened earlier, and move the git directory to the expected place.
    rm -rf 'vscode'
    mv '../vscode' 'vscode'
}

build() {
    cd "vscodium"

    # Export some environment variables that would normally be set by Travis CI.
    export SHOULD_BUILD="yes"
    export VSCODE_ARCH="${_vscode_arch}"
    export OS_NAME="linux"
    export LATEST_MS_COMMIT=$(git rev-list --tags --max-count=1)
    export LATEST_MS_TAG=$(git describe --tags "${LATEST_MS_COMMIT}")

    # Disable building rpm, deb, and AppImage packages which are not needed in an AUR build
    export SKIP_LINUX_PACKAGES="True"

    # Deactivate any pre-loaded nvm, and make sure we use our own in the current source directory
    which nvm >/dev/null 2>&1 && nvm deactivate && nvm unload
    export NVM_DIR="${srcdir}/.nvm"
    source /usr/share/nvm/init-nvm.sh || [[ $? != 1 ]]

    # TODO: Remove this when VSCodium adds the .nvmrc file
    if [ ! -f .nvmrc ]
    then
        echo "v14.19.0" > .nvmrc
    fi
    # TODO: End remove this

	# Install the correct version of NodeJS (read from .nvmrc)
	nvm install $(cat .nvmrc)
    nvm use

    # Check if the correct version of node is being used
    if [[ "$(node --version)" != "$(cat .nvmrc)" ]]
    then
    	echo "Using the wrong version of NodeJS! Expected ["$(cat .nvmrc)"] but using ["$(node --version)"]."
    	exit 1
    fi

    # Build!
    ./build.sh
}

package() {
    install -d -m755 ${pkgdir}/usr/bin
    install -d -m755 ${pkgdir}/usr/share/{${pkgname},applications,pixmaps}
    install -d -m755 ${pkgdir}/usr/share/licenses/${pkgname}
    cp -r ${srcdir}/vscodium/LICENSE ${pkgdir}/usr/share/licenses/${pkgname}
    cp -r ${srcdir}/vscodium/VSCode-linux-${_vscode_arch}/* ${pkgdir}/usr/share/${pkgname}
    ln -s /usr/share/${pkgname}/bin/codium ${pkgdir}/usr/bin/codium
    ln -s /usr/share/${pkgname}/bin/codium ${pkgdir}/usr/bin/vscodium
    install -D -m644 vscodium.desktop ${pkgdir}/usr/share/applications/vscodium.desktop
    install -D -m644 ${srcdir}/vscodium/VSCode-linux-${_vscode_arch}/resources/app/resources/linux/code.png \
            ${pkgdir}/usr/share/pixmaps/vscodium.png
}
