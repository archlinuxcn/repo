# Maintainer:
# Contributor: Aleksandr Beliaev <trap000d@gmail.com>

## links
# https://posit.co/products/open-source/rstudio/
# https://github.com/rstudio/rstudio

## options
: ${_gwt_version:=2.12.2}
: ${_java_version:=17}
: ${_nodeversion:=23}
: ${_pandocver:=current}
: ${_soci_version:=4.0.3}

: ${_quarto_branch:=release/rstudio-cranberry-hibiscus}
: ${_quarto:=false}

: ${_copilot_version:=1.371.0}

: ${_commit:=af5fc22a687c0f462ee27c6afeeee38ee46507b9}

_pkgname="rstudio-desktop"
pkgname="$_pkgname"
pkgver=2025.09.0.387
pkgrel=1
pkgdesc="A powerful and productive integrated development environment (IDE) for R programming language"
url="https://github.com/rstudio/rstudio"
license=('AGPL-3.0-only')
arch=('x86_64')

depends=(
  'dbus'
  'hicolor-icon-theme'
  'hunspell-en_US'
  'libboost_chrono.so'          # boost-libs
  'libboost_filesystem.so'      # boost-libs
  'libboost_iostreams.so'       # boost-libs
  'libboost_program_options.so' # boost-libs
  'libboost_thread.so'          # boost-libs
  'libcups'
  'libyaml-cpp.so' # yaml-cpp
  'mathjax2'
  'nspr'
  'nss'
  'pandoc'
  'r'
)
makedepends=(
  "java-environment${_java_version:+=$_java_version}"
  'ant'
  'boost'
  'cmake'
  'git'
  'libcups'
  'ninja'
  'nvm'
  'openssl'
  'pam'
  'postgresql-libs'
  'python'
  'python-setuptools'
  'wget'
  'yarn'
)
optdepends=(
  'git: for git support'
  'nodejs: for copilot support'
  'openssh-askpass: for a git ssh access'
  'postgresql-libs: for postgresql'
  'quarto: for Quarto projects support'
  'subversion: for subversion support'
)

if [[ "${_quarto::1}" == "t" ]]; then
  makedepends+=('quarto') # AUR
fi

provides=("$_pkgname")
conflicts=("$_pkgname")

options=('!emptydirs' '!debug' '!strip')

_source_main() {
  _pkgsrc="rstudio-$_commit"
  local _pkgext="tar.gz"
  source=(
    "rstudio-$pkgver-${_commit::7}.$_pkgext"::"https://github.com/rstudio/rstudio/archive/$_commit.$_pkgext"
    "quarto"::"git+https://github.com/quarto-dev/quarto.git#branch=${_quarto_branch}"
  )
  sha256sums=(
    'SKIP'
    'SKIP'
  )
}

_source_gwt() {
  _pkgext_gwt="tar.gz"
  noextract+=("gwt-${_gwt_version}.$_pkgext_gwt")
  source+=("https://rstudio-buildtools.s3.us-east-1.amazonaws.com/gwt/gwt-${_gwt_version}.$_pkgext_gwt")
  sha256sums+=('27284accdad05ff8919a7ac6dc5f939a511a90842a35f6393517506d74809e76')
}

_source_soci() {
  local _pkgext_soci="tar.gz"
  source+=("soci-$_soci_version.$_pkgext_soci"::"https://github.com/SOCI/soci/archive/refs/tags/v$_soci_version.$_pkgext_soci")
  sha256sums+=('4b1ff9c8545c5d802fbe06ee6cd2886630e5c03bf740e269bb625b45cf934928')

  _build_soci() (
    echo "Building SOCI..."
    local _opts_soci=(
      -B "soci-$_soci_version/build"
      -S "soci-$_soci_version"
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
      -DBUILD_SHARED_LIBS=OFF
      -Wno-dev
    )

    cmake "${_opts_soci[@]}"
    cmake --build "soci-$_soci_version/build"
  )
}

_source_copilot() {
  source+=("https://github.com/github/copilot-language-server-release/releases/download/${_copilot_version}/copilot-language-server-linux-x64-${_copilot_version}.zip")
  sha256sums+=('SKIP')
}

_source_main
_source_gwt
_source_soci
_source_copilot

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
  sed -E -e '/PANDOC_VERSION/s/"[0-9\.]+"/"'${_pandocver}'"/' -i "cmake/globals.cmake"

  # Suppress _FORTIFY_SOURCE mismatch warnings
  sed -i 's/D_FORTIFY_SOURCE=2/D_FORTIFY_SOURCE=3/' "src/cpp/CMakeLists.txt"

  # fix npm/node paths
  sed -E -e 's&set\(RSTUDIO_NODE_PATH .*\)&set(RSTUDIO_NODE_PATH "/usr/bin")&' \
    -i cmake/globals.cmake

  install -dm755 "$srcdir/$_pkgsrc/dependencies/common/node"
  ln -sfT "$NVM_DIR/versions/node/v$RSTUDIO_NODE_VERSION" "$srcdir/$_pkgsrc/dependencies/common/node/${RSTUDIO_NODE_VERSION}-patched"

  sed -E -e 's&^external-node-path=.*$&external-node-path=/usr/bin/node&' \
    -i src/cpp/conf/rsession-dev.conf

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

  # needed for system yaml-cpp
  sed '/add_subdirectory(src)/i find_package(yaml-cpp REQUIRED)' -i CMakeLists.txt

  # fix os-release path
  sed -E 's&(STRINGS) "/etc/os-release" (OS_RELEASE)&\1 "/usr/lib/os-release" \2&' \
    -i cmake/modules/OsRelease.cmake

  # bundled deps
  cd "$srcdir/$_pkgsrc/dependencies"
  install -d pandoc/${_pandocver}
  ln -sfT /usr/bin/pandoc pandoc/${_pandocver}/pandoc

  ln -sfT /usr/share/myspell/dicts dictionaries
  ln -sfT /usr/share/mathjax2 mathjax-27

  install -Dm755 "$srcdir/copilot-language-server" -t "copilot-language-server"
  ln -sfT "$srcdir/soci-$_soci_version" "soci-$_soci_version"

  # Panmirror is picked up now from Quarto repo
  ln -sfT "$srcdir/quarto" "$srcdir/$_pkgsrc/src/gwt/lib/quarto"

  # GWT
  mkdir -p common/gwtproject
  cd common/gwtproject
  bsdtar -xf "$srcdir/gwt-$_gwt_version.$_pkgext_gwt"
)

build() (
  export CMAKE_POLICY_VERSION_MINIMUM=3.5

  _nvm_env
  _run_if_exists _build_soci

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

  cd "${srcdir}"
  echo "Downloading and installing R packages..."
  export R_LIBS_USER="$srcdir/$_pkgsrc/dependencies/R"
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
    -DRSTUDIO_USE_SYSTEM_BOOST=ON
    -DRSTUDIO_USE_SYSTEM_SOCI=OFF
    -DRSTUDIO_USE_SYSTEM_YAML_CPP=ON
    -DRSTUDIO_NODE_VERSION="Current"
    -DQUARTO_ENABLED=${_quarto}
    -DRSTUDIO_UNIT_TESTS_ENABLED=OFF
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

name=rstudio
flags_file="\${XDG_CONFIG_HOME:-\$HOME/.config}/\${name}-flags.conf"
fallback_file="\${XDG_CONFIG_HOME:-\$HOME/.config}/electron-flags.conf"

lines=()
if [[ -f "\${flags_file}" ]]; then
  mapfile -t lines < "\${flags_file}"
elif [[ -f "\${fallback_file}" ]]; then
  mapfile -t lines < "\${fallback_file}"
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

_run_if_exists() {
  if declare -F "$1" > /dev/null; then
    eval "$1"
  fi
}
