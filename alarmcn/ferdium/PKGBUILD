# Maintainer: Cedric Roijakkers <cedric [the at sign goes here] roijakkers [the dot sign goes here] be>.
# Inspired from the PKGBUILD for ferdi-git.

_pkgname='ferdium'
pkgname="ferdium"
_electron='electron37'
_electronpackage='electron37'
pkgver=7.1.1
pkgrel=1
pkgdesc='A messaging browser that allows you to combine your favorite messaging services into one application (git build from latest release).'
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
url="https://ferdium.org/"
license=('Apache')
depends=('nss' 'atk' 'at-spi2-atk' 'libcups' 'libdrm' 'gdk-pixbuf2' 'gtk3' 'alsa-lib' 'c-ares' 'ffmpeg' 'libevent' 'libxkbfile' 'libxslt' 'minizip' 're2' 'snappy' "$_electronpackage")
apptag='v7.1.1'
makedepends=('nvm' 'git' 'python' 'libxcrypt-compat' 'asar')
options=(!strip !debug)
provides=(
    'ferdium'
)
conflicts=(
    'ferdium-bin'
    'ferdium-nightly-bin'
    'ferdium-nightly'
    'ferdium-beta-bin'
    'ferdium-beta'
    'ferdium-git'
    'ferdium-electron'
)
source=(
	"$pkgname::git+https://github.com/ferdium/ferdium-app#tag=${apptag}"
)
sha512sums=('fd786a949183a0f1f665bb021ff857a69b4e0ce9de6e044e0918ba56f579e877f45cef6ce1d4680d282baab61f7eaa852b725bf145d572e8ac3a181f9937e43f')

_sourcedirectory="$pkgname"

case "$CARCH" in
	i686)
		_electronbuilderarch='ia32'
	;;
	armv7h)
		_electronbuilderarch='armv7l'
	;;
	aarch64)
		_electronbuilderarch='arm64'
	;;
	*)
		_electronbuilderarch='x64'
	;;
esac

prepare() {
	# Due to patches and sed's, reset the code to upstream before starting
	cd "$srcdir/$_sourcedirectory/"
	git reset --hard "refs/tags/${apptag}"

	# Initialise the recipes submodule
	git submodule init
	cd "$srcdir/$_sourcedirectory/recipes"
	git reset --hard
	cd "$srcdir/$_sourcedirectory/"
	git submodule update --init --recursive

	# Specify path for autostart file
	sed -i -e "s#path: executablePath,#path: '/usr/bin/ferdium',#g" src/stores/AppStore.ts
	# Set noUnusedLocals to false to avoid compilation error in AppStore.ts
	sed -i -e 's#"noUnusedLocals": true#"noUnusedLocals": false#g' tsconfig.json
}

pkgver() {
	cd "$srcdir/$_sourcedirectory/"
	printf "%s" "$(git describe --tags | sed 's/\([^-]*-\)g/r\1/;s/-/./g' | sed 's/^v//')"
}

build() {
	# Prepare recipes
	cd "$srcdir/$_sourcedirectory/"

	# Set environment variables needed for NodeJS/Electron
    export CI=true

    # Deactivate any pre-loaded nvm, and make sure we use our own in the current source directory
    which nvm >/dev/null 2>&1 && nvm deactivate && nvm unload
    export NVM_DIR="${srcdir}/.nvm"
    source /usr/share/nvm/init-nvm.sh || [[ $? != 1 ]]

	# Install the correct version of NodeJS (read from .nvmrc)
	nvm install $(cat .nvmrc)
    nvm use

    # Extract the correct versions of tools from the package.json file
    expected_node_version=$(node -p 'require("./package.json").engines.node' | sed -e 's/\^//g')
    expected_npm_version=$(node -p 'require("./package.json").engines.npm' | sed -e 's/\^//g')
    expected_pnpm_version=$(node -p 'require("./package.json").engines.pnpm' | sed -e 's/\^//g')

    # If pnpm is not found in the package.json, get it from recipes/package.json (old style)
    if [[ "${expected_pnpm_version}" == "undefined" ]]
    then
    	expected_pnpm_version=$(node -p 'require("./recipes/package.json").engines.pnpm')
	fi

    # Cross-check if all versions of node match
    if [[ "$(node --version)" != "v${expected_node_version}" || "$(node --version)" != "v$(cat .nvmrc)" || "v${expected_node_version}" != "v$(cat .nvmrc)" ]]
    then
    	echo "Version mismatch in NodeJS! Version in .nvmrc is [v$(cat .nvmrc)], version in package.json is [v${expected_node_version}], and used version is ["$(node --version)"]."
    	exit 1
    fi

    # Empty the cache before building to avoid issues with packages not being found
    npm cache clean --force

	# Install the correct version of npm and/or pnpm, depending on the contents of package.json
	if [[ "${expected_npm_version}" != "undefined" ]]
	then
		npm i -gf npm@${expected_npm_version}
	fi
	if [[ "${expected_pnpm_version}" != "undefined" ]]
	then
		npm i -gf pnpm@${expected_pnpm_version}
	fi

	# This is useful if we move from 'npm' to 'pnpm' for the main repo as well
    if [[ -s 'pnpm-lock.yaml' ]]; then
		BASE_CMD=pnpm
    else
		BASE_CMD=npm
    fi

	# Build recipe archives, from here on switch to pnpm
	$BASE_CMD i
	$BASE_CMD run prepare-code || true # Ignore errors, because there is a false error causing the build to break

	# Run the package script
	pushd recipes
    pnpm i
    pnpm run package
    popd

	# Make sure the internal version of electron-builder is being used by prefixing it to the $PATH
	export PATH=./node_modules/.bin/:$PATH

	# When passing arguments downstream, npm needs an extra "--" while pnpm does not
	extra_cli_args=""
	if [[ "${BASE_CMD}" == "npm" ]]
	then
		extra_cli_args="--"
	fi

	# Run the electron build script,
	# passing parameters "-l dir" to only build for Linux and the dir target (which we will use later in function package() to make the Arch package),
	# and "--${_electronbuilderarch}" to only build for the current architecture, saving build time
	NODE_ENV='production' $BASE_CMD run build ${extra_cli_args} -l dir --${_electronbuilderarch} -c.electronDist="/usr/lib/$_electron" -c.electronVersion="$(cat "/usr/lib/$_electron/version" | sed -e 's/^v//')"
}

package() {
	cd "$srcdir/$_sourcedirectory/"

	# Determine where the unpacked output directory is located
	local _outpath='out/linux'
	if [ "$_electronbuilderarch" != 'x64' ]; then
		_outpath="$_outpath-$_electronbuilderarch"
	fi
	_outpath="$_outpath-unpacked"

	# Create a shell script to start Ferdium with Electron
	install -d -m755 "${pkgdir}/usr/bin/"
	cat > "$pkgdir/usr/bin/$_pkgname" <<EOF
#!/bin/sh
ELECTRON_IS_DEV=0 exec /usr/bin/$_electron /opt/$pkgname/ "\$@"
EOF
	chmod +x "$pkgdir/usr/bin/ferdium"

	# Extract the asar package to the system
	install -d -m755 "${pkgdir}/opt/$pkgname/"
	asar e "$_outpath/resources/app.asar" "${pkgdir}/opt/$pkgname/"

    # Create a .desktop file
	install -dm755 "$pkgdir/usr/share/applications/"
	cat << EOF > "$pkgdir/usr/share/applications/$_pkgname.desktop"
[Desktop Entry]
Name=${_pkgname^}
Exec=/usr/bin/$_pkgname %U
Terminal=false
Type=Application
Icon=ferdium
StartupWMClass=Ferdium
Comment=Ferdium is your messaging app / former heir to the throne of Austria-Hungary and combines chat & messaging services into one application. Ferdium currently supports Slack, WhatsApp, Gmail, Facebook Messenger, Telegram, Google Hangouts, GroupMe, Skype and many more. You can download Ferdium for free for Mac, Windows, and Linux.
MimeType=x-scheme-handler/ferdium;
Categories=Network;InstantMessaging;
EOF
	# Install the icons
	for _size in 16 24 32 48 64 96 128 256 512 1024; do
		install -Dm644 "build-helpers/images/icons/${_size}x${_size}.png" "$pkgdir/usr/share/icons/hicolor/${_size}x${_size}/apps/$_pkgname.png"
	done
}
