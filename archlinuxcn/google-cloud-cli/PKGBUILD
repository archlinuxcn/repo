# Maintainer: Josef Vybíhal <josef.vybihal@gmail.com>
# Contributor: Polarian <polarian@polarian.dev>
# Contributor: Benjamin Denhartog <ben@sudoforge.com>
# Contributor: Mansour Behabadi <mansour@oxplot.com>
# Contributor: Troy Engel <troyengel+arch@gmail.com>
# Contributor: Geoff Hill <geoff@geoffhill.org>
# Contributor: Sebastien Bariteau <numkem@numkem.org>
# Contributor: Justin Dray <justin@dray.be>
# Contributor: tobbik

#  shellcheck disable=SC2164,SC2154,SC2148,SC2034

# Release Notes: https://cloud.google.com/sdk/docs/release-notes
# Cloud Storage Bucket: https://console.cloud.google.com/storage/browser/cloud-sdk-release/for_packagers/linux
# deb pool:
#  - https://packages.cloud.google.com/apt/dists/cloud-sdk/main/binary-amd64/Packages
#  - https://packages.cloud.google.com/apt/pool/cloud-sdk/google-cloud-cli_516.0.0-0_amd64_e19fae4ce840c378a624e2cbdba2aa87.deb

_extracted_name='google-cloud-sdk'
pkgbase='google-cloud-cli'
pkgname=(
  'google-cloud-cli'
  'google-cloud-cli-bq'
  'google-cloud-cli-gsutil'
  'google-cloud-cli-bundled-python3-unix'
  'google-cloud-cli-component-gke-gcloud-auth-plugin'
)
# pkgname=(
#   'google-cloud-cli'
#   'google-cloud-cli-component-anthos-auth'
#   'google-cloud-cli-component-anthoscli'
#   'google-cloud-cli-component-app-engine-go'
#   'google-cloud-cli-component-app-engine-grpc'
#   'google-cloud-cli-component-app-engine-java'
#   'google-cloud-cli-component-app-engine-python'
#   'google-cloud-cli-component-app-engine-python-extras'
#   'google-cloud-cli-component-bigtable-emulator'
#   'google-cloud-cli-component-cbt'
#   'google-cloud-cli-component-cloud-build-local'
#   'google-cloud-cli-component-cloud-run-proxy'
#   'google-cloud-cli-component-config-connector'
#   'google-cloud-cli-component-datastore-emulator'
#   'google-cloud-cli-component-docker-credential-gcr'
#   'google-cloud-cli-component-enterprise-certificate-proxy'
#   'google-cloud-cli-component-firestore-emulator'
#   'google-cloud-cli-component-istioctl'
#   'google-cloud-cli-component-kpt'
#   'google-cloud-cli-component-kubectl-oidc'
#   'google-cloud-cli-component-local-extract'
#   'google-cloud-cli-component-log-streaming'
#   'google-cloud-cli-component-managed-flink-client'
#   'google-cloud-cli-component-minikube'
#   'google-cloud-cli-component-nomos'
#   'google-cloud-cli-component-package-go-module'
#   'google-cloud-cli-component-pubsub-emulator'
#   'google-cloud-cli-component-run-compose'
#   'google-cloud-cli-component-skaffold'
#   'google-cloud-cli-component-spanner-cli'
#   'google-cloud-cli-component-spanner-emulator'
#   'google-cloud-cli-component-spanner-migration-tool'
#   'google-cloud-cli-component-terraform-tools'
#   'google-cloud-cli-component-tests'
#   'google-cloud-sdk-bundled-python3-unix'
#   'google-cloud-cli-component-kubectl'
#   'google-cloud-cli-component-gsutil'
# )
pkgver=537.0.0
pkgrel=1
pkgdesc="A core set of command-line tools for the Google Cloud Platform. Includes only gcloud core (with beta and alpha commands), gcloud-crc32c and man pages"
url="https://cloud.google.com/cli/"
license=('Apache-2.0')
arch=('x86_64' 'aarch64')
depends=('python>=3.9')
makedepends=('jq')
options=('!strip' 'staticlibs' '!zipman' '!debug' '!lto')

export _force_budled_python=false
export _package_bundled_python=false

source=(
  "$pkgbase.sh"
  "$pkgbase.install"
)
source_x86_64=("$pkgbase-$pkgver.orig_x86_64.tar.gz::https://dl.google.com/dl/cloudsdk/release/downloads/for_packagers/linux/${pkgbase}_${pkgver}.orig_amd64.tar.gz")
source_aarch64=("$pkgbase-$pkgver.orig_aarch64.tar.gz::https://dl.google.com/dl/cloudsdk/release/downloads/for_packagers/linux/${pkgbase}_${pkgver}.orig_aarch64.tar.gz")

sha256sums=('6e88b535c020b0f28c986fdb66918f8c07e4d337e813b77ec2068068f03457f8'
            '6ac95bcc5afa06e9c1e3bd402ecbe1a2092b963d70a8f314215dd4be27e16fc6')
sha256sums_x86_64=('3e1076f44c060a83af0ddfc5047b61e2070e49e19a930c2b8036e564e5e571a3')
sha256sums_aarch64=('af25fd35e87e1bde81ab0523b7b95765ed45fc9f60d962f83c0c08b7ce426490')

prepare() {
  cd "$_extracted_name"

  if [ "$_package_bundled_python" = false ]; then
    # relax forced 'core' dependency on bundled-python3-unix
    sed -i '/bundled-python3-unix/d' .install/core*.snapshot.json
    if ls .install/bundled-python3-* 1> /dev/null 2>&1; then
      mkdir -p "$srcdir/bundledpython/.install"
      mv platform/bundledpythonunix     $srcdir/bundledpython/
      mv .install/bundled-python3-unix* $srcdir/bundledpython/.install/
    fi
  fi

  find "$srcdir" -name '__pycache__' -type d -exec rm -rf {} +
}

package_google-cloud-cli() {
  # Conflict the old package name to force migration
  conflicts=('google-cloud-sdk')
  provides=('google-cloud-sdk' 'google-cloud-cli-alpha' 'google-cloud-cli-beta')
  replaces=('google-cloud-sdk')
  optdepends=(
    'google-cloud-cli-bq: BigQuery Command Line Tool'
    'google-cloud-cli-gsutil: Cloud Storage Command Line Tool. Not the recommended CLI for Cloud Storage')
  install=$pkgbase.install
  backup=( 'etc/profile.d/google-cloud-cli.sh' )

  sdir="${srcdir}/${_extracted_name}"
  ddir="${pkgdir}/opt/${pkgbase}"

  # _install_path="${pkgdir}/opt/${pkgbase}"
  _bundled_py_bin="${ddir:${#pkgdir}}/platform/bundledpythonunix/bin/python3"

  install -d -m 0755 \
    "${pkgdir}/opt" \
    "${pkgdir}/etc/bash_completion.d" \
    "${pkgdir}/usr/share/zsh/site-functions"

  cp -r "${sdir}" "${ddir}"

  # remove components
  rm -rf "$ddir/platform/gsutil"
  rm -f  "$ddir/.install/gsutil"*
  rm -f  "$ddir/bin/gsutil"
  rm -f  "$ddir/data/cli/gsutil.json"

  rm -rf "$ddir/platform/bq"
  rm -f  "$ddir/.install/bq"*
  rm -f  "$ddir/bin/bq"
  rm -f  "$ddir/data/cli/bq.json"

  install -D -m 0644 "${srcdir}/${source[0]}" \
    "${pkgdir}/etc/profile.d/google-cloud-cli.sh"

  if [ "$_force_budled_python" = true ]; then
    { echo "export CLOUDSDK_PYTHON=${_bundled_py_bin}"
      echo "export CLOUDSDK_GSUTIL_PYTHON=${_bundled_py_bin}"
      echo "export CLOUDSDK_BQ_PYTHON=${_bundled_py_bin}"
    } >> "${pkgdir}/etc/profile.d/google-cloud-cli.sh"
  fi

  ln -rsT "${ddir}/completion.bash.inc" \
    "${pkgdir}/etc/bash_completion.d/google-cloud-cli"

  for cmd in gcloud gsutil bq; do
    ln -rsT "${ddir}/completion.zsh.inc" \
      "${pkgdir}/usr/share/zsh/site-functions/_${cmd}"
  done

  install -d -m 0755 "${pkgdir}/usr/bin"
  for bin in gcloud \
             gcloud-crc32c \
             docker-credential-gcloud \
             git-credential-gcloud.sh \
             ; do
    ln -rsT "${ddir}/bin/${bin}" \
      "${pkgdir}/usr/bin/${bin}"
  done

  install -d -m 0755 "${pkgdir}/usr/share"
  mv -f "${pkgdir}/opt/${pkgbase}/help/man" "${pkgdir}/usr/share/"
  rm -rf "$ddir"/{deb,rpm,help}
}

_package_helper() {
  # local -r s=$1
  # local -r p=$2
  # local -r c=$3
  sdir="${srcdir}/${_extracted_name}"
  ddir="${pkgdir}/opt/${pkgbase}"
  install -d -m 0755 "${ddir}/"{bin,.install,platform}
  install -d -m 0755 "${pkgdir}/usr/bin"
  cp -r              "${sdir}/platform/${c}"         "${ddir}/platform/"
  install -D -m 0644 "${sdir}/.install/${c}"*     -t "${ddir}/.install"
  install -D -m 0755 "${sdir}/bin/${c}"              "${ddir}/bin/${c}"
  install -D -m 0644 "${sdir}/data/cli/${c}.json" -t "${ddir}/data/cli"
  ln -rsT "${ddir}/bin/${c}" \
        "${pkgdir}/usr/bin/${c}"
}

package_google-cloud-cli-bq() {
  pkgdesc='BigQuery Command Line Tool'
  provides=('google-cloud-cli-bq')
  c=${pkgname#google-cloud-cli-} # component
  _package_helper
}

# pkgver_google-cloud-cli-gsutil() {
#   cat "${sdir}/platform/gsutil/VERSION"
# }

package_google-cloud-cli-gsutil() {
  pkgdesc='Cloud Storage Command Line Tool: gsutil is not the recommended CLI for Cloud Storage'
  provides=('google-cloud-cli-gsutil' 'gsutil')
  conflicts=('gsutil')
  #depends+=('google-cloud-cli-bundled-python3-unix')
  optdepends=("python-crcmod: verify the integrity of GCS object contents"
  "google-cloud-cli-bundled-python3-unix: bundled python to use if system python is not compatible")
  c=${pkgname#google-cloud-cli-} # component
  backup=( "etc/profile.d/google-cloud-cli-gsutil.sh" )
  _package_helper

  # _bundled_py_bin="${ddir:${#pkgdir}}/platform/bundledpythonunix/bin/python3"
  # install -d -m 0755 "${pkgdir}/etc/profile.d"
  # echo "export CLOUDSDK_GSUTIL_PYTHON=${_bundled_py_bin}" >> \
  # "${pkgdir}/etc/profile.d/google-cloud-cli-${c}.sh"
}

package_google-cloud-cli-bundled-python3-unix() {
  arch=('x86_64')
  pkgdesc='gcloud Bundled Python 3.12'
  ddir="${pkgdir}/opt/${pkgbase}"
  c=${pkgname#google-cloud-cli-} # component
  install -d -m 0755 "${ddir}"/{.install,platform} && cd "${ddir}"
  mv "$srcdir"/bundledpython/bundledpythonunix platform/
  mv "$srcdir"/bundledpython/.install/"${c}"*  .install/
}

package_google-cloud-cli-component-gke-gcloud-auth-plugin() {
  pkgdesc='gke-gcloud-auth-plugin'
  provides=('google-cloud-cli-gke-gcloud-auth-plugin')
  conflicts=('google-cloud-cli-gke-gcloud-auth-plugin')
  c=${pkgname#google-cloud-cli-component-}
  ddir="${pkgdir}/opt/${pkgbase}"
  install -d -m 0755 "${ddir}/"{.install,bin} "${pkgdir}/usr/bin"

  cd "$_extracted_name"

  # allow updater for component
  cat <<< "$(jq '.disable_updater = false' < lib/googlecloudsdk/core/config.json)" > lib/googlecloudsdk/core/config.json

  bin/gcloud -q components install "${c}" > /dev/null 2>&1

  mv .install/"${c}"*  "${ddir}/.install"
  mv bin/"${c}"*       "${ddir}/bin"
  ln -rsT "${ddir}/bin/${c}" \
        "${pkgdir}/usr/bin/${c}"

  # turn off updater
  cat <<< "$(jq '.disable_updater = true' < lib/googlecloudsdk/core/config.json)" > lib/googlecloudsdk/core/config.json

}
