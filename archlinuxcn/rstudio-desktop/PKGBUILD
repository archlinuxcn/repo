# Maintainer:
# Contributor: Aleksandr Beliaev <trap000d@gmail.com>

## links
# https://posit.co/products/open-source/rstudio/
# https://github.com/rstudio/rstudio

## options
: ${_nodeversion:=22}
: ${_pandocver:=current}
: ${_sociver:=4.0.3}
: ${_quarto_branch:=release/rstudio-cranberry-hibiscus}
: ${_quarto:=false}

: ${_commit:=cf37a3e5488c937207f992226d255be71f5e3f41} # 2024.12.0.467

## basic info
_pkgname="rstudio-desktop"
pkgname="$_pkgname"
pkgver=2024.12.0.467
pkgrel=1
pkgdesc="A powerful and productive integrated development environment (IDE) for R programming language"
url="https://github.com/rstudio/rstudio"
license=('AGPL-3.0-only')
arch=('x86_64')

depends=(
  'boost-libs'
  'dbus'
  'hicolor-icon-theme'
  'hunspell-en_US'
  'libcups'
  'mathjax2'
  'nspr'
  'nss'
  'pandoc'
  'r'
)
makedepends=(
  'apache-ant'
  'boost'
  'cmake'
  'git'
  'jdk11-openjdk'
  'libcups'
  'ninja'
  'nvm' # AUR
  'openssl'
  'pam'
  'python'
  'python-setuptools'
  'wget'
  'yarn'
)
optdepends=(
  'git: for git support'
  'nodejs: for copilot support'
  'openssh-askpass: for a git ssh access'
  'quarto: for Quarto projects support'
  'subversion: for subversion support'
)

if [[ "${_quarto::1}" == "t" ]]; then
  makedepends+=(
    'quarto' # AUR
  )
fi

provides=("$_pkgname")
conflicts=("$_pkgname")

options=('!emptydirs' '!debug')

_pkgsrc="rstudio-$_commit"
_pkgext="tar.gz"
source=(
  "rstudio-$pkgver-${_commit::7}.$_pkgext"::"https://github.com/rstudio/rstudio/archive/$_commit.$_pkgext"
  "quarto"::"git+https://github.com/quarto-dev/quarto.git#branch=${_quarto_branch}"
  "soci-$_sociver.tar.gz"::"https://github.com/SOCI/soci/archive/refs/tags/v${_sociver}.tar.gz"
)
sha256sums=(
  'b43ab0a3a37a4efe6ff090be110762f763e2606ccf9b64f2ca0df52e0737ec3e'
  'SKIP'
  '4b1ff9c8545c5d802fbe06ee6cd2886630e5c03bf740e269bb625b45cf934928'
)

_nvm_env() {
  export HOME="$SRCDEST/node-home"
  export NVM_DIR="$SRCDEST/node-nvm"

  # set up nvm
  source /usr/share/nvm/init-nvm.sh || [[ $? != 1 ]]
  nvm install $_nodeversion
  nvm use $_nodeversion

  _npm_path="$(which npm | sed -E 's&/[^/]+$&&')"
  export RSTUDIO_NODE_VERSION=$(echo "$_npm_path" | sed -E 's&^\S+/v([0-9\.]+)/\S+$&\1&')
}

prepare() (
  _nvm_env
  #npm install yarn

  cd "$_pkgsrc"
  # Do not use outdated version name of pandoc
  sed -E -e '/PANDOC_VERSION/s/2.[0-9]+/current/' -i "cmake/globals.cmake"

  # Suppress _FORTIFY_SOURCE mismatch warnings
  sed -i 's/D_FORTIFY_SOURCE=2/D_FORTIFY_SOURCE=3/' "src/cpp/CMakeLists.txt"

  # fix npm/node paths
  sed -E -e 's&set\(RSTUDIO_NODE_PATH .*\)&set(RSTUDIO_NODE_PATH "/usr/bin")&' \
    -i cmake/globals.cmake

  install -dm755 "$srcdir/$_pkgsrc/dependencies/common/node"
  ln -sfT "$NVM_DIR/versions/node/v$RSTUDIO_NODE_VERSION" "$srcdir/$_pkgsrc/dependencies/common/node/${RSTUDIO_NODE_VERSION}-patched"

  sed -E -e 's&^external-node-path=.*$&external-node-path=/usr/bin/node&' \
    -i src/cpp/conf/rsession-dev.conf

  sed -E -e 's&DIRECTORY "\$\{RSTUDIO_DEPENDENCIES_DIR\}/common/node/\$\{RSTUDIO_INSTALLED_NODE_VERSION\}-patched/"&DIRECTORY "/usr"&' \
    -e 's&(# install node)&\1\nif(FALSE)&' \
    -e 's&(# install quarto)&endif()\n\1&' \
    -i src/cpp/session/CMakeLists.txt

  sed -E -e 's&"\S+/common/node/\S+"&"/usr"&' \
    -i src/cpp/session/SessionOptions.cpp

  sed -E -e '/"node\.version"/s&value="[0-9\.]+"&value="Current"&' \
    -e '/"node\.dir"/s&value="\S+"&value="/usr"&' \
    -e 's&"\S+/common/node/\S+/bin/yarn"&"/usr/bin/yarn"&' \
    -i src/gwt/build.xml

  sed -E -e 's&PATHS "/opt/rstudio-tools/dependencies/common/node/\$\{RSTUDIO_NODE_VERSION\}"&PATHS "'"${_npm_path}"'"&' \
    -e 's&"\S+CMAKE_CURRENT_LIST_DIR\S+/dependencies/common/node/\S+"&"'"${_npm_path}"'"&g' \
    -e 's&set\(RSTUDIO_NODE_VERSION "[0-9\.]+"\)&set(RSTUDIO_NODE_VERSION "Current")&' \
    -i src/node/CMakeNodeTools.txt

  # fix os-release path
  sed -E 's&(STRINGS) "/etc/os-release" (OS_RELEASE)&\1 "/usr/lib/os-release" \2&' \
    -i cmake/modules/OsRelease.cmake

  # fix boost 1.86 incompatibility
  sed -E -e 's&return afterResponse_;&return (bool)afterResponse_;&' \
    -i src/cpp/core/json/JsonRpc.cpp

  cd "$srcdir/$_pkgsrc/dependencies/common"
  install -d pandoc/${_pandocver}

  ln -sfT /usr/share/myspell/dicts dictionaries
  ln -sfT /usr/share/mathjax2 mathjax-27
  ln -sfT /usr/bin/pandoc pandoc/${_pandocver}/pandoc

  # Fix links for src/cpp/session/CMakeLists.txt
  cd "$srcdir/$_pkgsrc/dependencies"
  ln -sfT /usr/share/myspell/dicts dictionaries
  ln -sfT /usr/share/mathjax2 mathjax-27

  # Bundled SOCI libs
  ln -sfT "${srcdir}/soci-${_sociver}" "soci-${_sociver}"

  # Panmirror is picked up now from Quarto repo
  ln -sfT "${srcdir}/quarto" "$srcdir/$_pkgsrc/src/gwt/lib/quarto"
)

_build_soci() {
  echo "Building SOCI libs..."

  local _opts_soci=(
    -B "soci-${_sociver}/build"
    -S "soci-${_sociver}"
    -G Ninja
    -DCMAKE_BUILD_TYPE=None
    -DCMAKE_INSTALL_PREFIX='/usr'
    -DSOCI_TESTS=OFF
    -DSOCI_CXX11=ON
    -DSOCI_EMPTY=OFF
    -DWITH_BOOST=ON
    -DWITH_POSTGRESQL=ON
    -DWITH_SQLITE3=ON
    -DWITH_DB2=OFF
    -DWITH_MYSQL=OFF
    -DWITH_ORACLE=OFF
    -DWITH_FIREBIRD=OFF
    -DWITH_ODBC=OFF
    -Wno-dev
  )

  cmake "${_opts_soci[@]}"
  cmake --build "soci-${_sociver}/build"
}

build() (
  _nvm_env
  # Quarto set up
  if (pacman -Q quarto > /dev/null 2> /dev/null); then
    _quarto="ON"
    echo "Quarto is installed, linking for build"
    cd "$srcdir/$_pkgsrc/dependencies"
    install -d quarto/bin/tools
    ln -sfT /usr/bin/quarto quarto/bin/quarto
    ln -sfT /usr/bin/pandoc quarto/bin/tools/pandoc
  else
    _quarto="OFF"
    echo "Quarto is not installed, using Pandoc"
    cd "$srcdir/$_pkgsrc/dependencies"
    install -d pandoc/${_pandocver}/bin/tools
    ln -sfT /usr/bin/pandoc pandoc/${_pandocver}/bin/tools/pandoc
  fi

  _build_soci

  export LDFLAGS+=" -L$srcdir/$_pkgsrc/dependencies/soci-${_sociver}/build/lib"

  cd "${srcdir}"
  echo "Downloading and installing R packages..."
  export R_LIBS_USER="${srcdir}/${_srcname}/dependencies/R"
  _JOBS="$(grep -oP -- "-j\s*\K[0-9]+" <<< "${MAKEFLAGS}")" || _JOBS="1"
  mkdir -p "${R_LIBS_USER}"
  local RPACKAGES=(
    digest
    purrr
    rmarkdown
    testthat
    xml2
    yaml
  )
  for RPKG in ${RPACKAGES[*]}; do
    RINSTALLCMD="if("'!'"require($RPKG, quietly = TRUE)) { options(Ncpus = ${_JOBS} ); install.packages('$RPKG', lib='$R_LIBS_USER', repos='https://cran.rstudio.com/') }"
    echo "> $RINSTALLCMD"
    Rscript -e "$RINSTALLCMD"
  done

  export PATH="/usr/lib/jvm/java-11-openjdk/jre/bin/:${PATH}"
  export RSTUDIO_TOOLS_ROOT="$srcdir/$_pkgsrc/dependencies"
  export RSTUDIO_NODE_PATH=/usr/
  export RSTUDIO_VERSION_MAJOR=$(cut -d'.' -f1 <<< "$pkgver")
  export RSTUDIO_VERSION_MINOR=$(cut -d'.' -f2 <<< "$pkgver")
  export RSTUDIO_VERSION_PATCH=$(cut -d'.' -f3 <<< "$pkgver")
  export RSTUDIO_VERSION_SUFFIX="+$(cut -d'.' -f4 <<< "$pkgver")"
  export GIT_COMMIT="${_commit::7}"
  export PACKAGE_OS=$(uname -om)

  # node-gyp or node have a bug that prevents building with "text file busy"
  # if the kernel is too fast, so we have to disable IO_URING support. This
  # is cleary a hack and needs to be removed as soon as possible
  # nodejs/node#48444 is the necro bumped thread
  # originally from docker
  # https://github.com/nodejs/node/issues/48444
  export UV_USE_IO_URING=0

  # -DCMAKE_INSTALL_PREFIX seems ignored for sub-dependencies,
  # which results as empty '/usr/local/bin' in package
  # Following override works for cmake >3.29
  export CMAKE_INSTALL_PREFIX=/usr/lib/rstudio

  local _opts_rstudio=(
    -B build
    -S "$_pkgsrc"
    -G Ninja
    -DCMAKE_BUILD_TYPE=None
    -DRSTUDIO_TARGET=Electron
    -DRSTUDIO_USE_SYSTEM_BOOST=YES
    -DRSTUDIO_USE_SYSTEM_SOCI=NO
    -DRSTUDIO_NODE_VERSION="Current"
    -DRSTUDIO_INSTALLED_NODE_VERSION="Current"
    -DQUARTO_ENABLED=${_quarto}
    -DBUILD_TESTING=OFF
    -Wno-dev
  )
  cmake "${_opts_rstudio[@]}"
  cmake --build build
)

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm755 /dev/stdin "${pkgdir}/usr/bin/rstudio" << END
#!/usr/bin/env bash

# See following script for potentially useful flags.
# https://github.com/ozankiratli/dotfiles/blob/master/.config/sway/scripts/rstudio-wayland

: \${XDG_CONFIG_HOME:=\$HOME/.config}

flags_file="\$XDG_CONFIG_HOME/rstudio-flags.conf"

lines=()
if [[ -f "\${flags_file}" ]]; then
  mapfile -t lines < "\${flags_file}"
fi

flags=()
for line in "\${lines[@]}"; do
  if [[ ! "\${line}" =~ ^[[:space:]]*#.* ]] && [[ -n "\${line}" ]]; then
    flags+=("\${line}")
  fi
done

: \${ELECTRON_IS_DEV:=0}
export ELECTRON_IS_DEV
: \${ELECTRON_FORCE_IS_PACKAGED:=true}
export ELECTRON_FORCE_IS_PACKAGED

exec /usr/lib/rstudio/rstudio "\${flags[@]}" "\$@"
END
}
