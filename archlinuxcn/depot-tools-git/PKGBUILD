# Maintainer: Luis Aranguren <pizzaman@hotmail.com>
# Contributor: Adrian Perez <aperez@igalia.com>
# Contributor: Chih-Hsuan Yen <yan12125@gmail.com>
# Contributor: rway <rway07@gmail.com>
# Contributor: wabi <aschrafl@jetnet.ch>
# Contributor: Alexander RÃ¸dseth <rodseth@gmail.com>
# Contributor: Andreas Schrafl <aschrafl@gmail.com>
# Contributor: piojo <aur@zwell.net>
# Contributor: hack.augusto <hack.augusto@gmail.com>

pkgname=depot-tools-git
pkgver=r6630.44134341f
pkgrel=1
pkgdesc='Build tools for working with Chromium development, include gclient'
arch=('any')
url='https://dev.chromium.org/developers/how-tos/install-depot-tools'
source=(
  "${pkgname}::git+https://chromium.googlesource.com/chromium/tools/depot_tools.git"
  'repo_fix.sh'
  'fixshebangs.py'
  'gsutil-use-google-cloud-sdk.patch'
  'vpython-use-system-python2.patch'
)
license=('Custom')
depends=('git' 'ninja' 'python2')
optdepends=(
	'google-cloud-sdk: for gsutil and download_from_google_storage'
	'subversion: for repositories using svn'
)
provides=('depot_tools' 'gclient')
conflicts=('gclient-svn' 'depot_tools-svn')
options=('!strip')
install="depot_tools.install"
sha512sums=('SKIP'
            'bde33ffcad42a4d554d5490b6562981ef4b9f3abebadbed909749ee05ba391da4b5acb31b901e785b6f019b4ed3f9c740ab92623dd6a87e67b4b599a0010374b'
            '33d772f68deddefce985d2820d3ef60fa730a1f3bc404cef3c8b1b517369501b9c3a07bc7b1b3df4d0589b45cbe4850f935699676c3e10c437bceffb37eb8214'
            '4043722867ebefc3d65b03f6faa016ef31c510587d499a96e3f3ae1f6e19b49299f5b540e3f2d5176e9ecfd73645d9b815d8c052fcc327687091a2355f817d6a'
            '4efd6fa204e429619d2da999d07d27eabd748b1941a913cfd5a83cf23fd93b3c8c021ed97c3f30dcc17f67b0dd32486bc361da374aa26e2be2d1d3ed922712c7')

_scripts_to_fix_exec=(
	cit
	clang-format
	clang_format_merge_driver
	compile_single_file
	luci-auth
	download_from_google_storage
	fetch
	gclient
	git-runhooks
	gn
	roll-dep
)

pkgver () {
	cd "${pkgname}"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare () {
	cd "${pkgname}"

	# This tools work with python2, but ArchLinux default is python3. Fix it.
	# pylint is in extra, ninja is an executable and it does not need any change.
	# gclient.py require a fix for work correctly with python2-colorama
	# Another way is make default python2, but I don't think is a good idea!
	# Fixing python scripts.
	"${srcdir}/fixshebangs.py"

	# Fix gclient.py
	sed -i -r -e 's/from third_party import colorama/import colorama/' \
			  -e 's/from third_party.colorama import Fore/from colorama import Fore/' \
		gclient.py

	# Fixing scripts which use "exec python"
	for script in "${_scripts_to_fix_exec[@]}"
	do
		sed -r -i -e 's/exec python/exec python2/' "${script}"
	done

  # Make gsutil use google-cloud-sdk instead of downloading from Google Storage
  patch -Np1 -i ../gsutil-use-google-cloud-sdk.patch

  # Force vpython to use system Python 2
  patch -Np1 -i ../vpython-use-system-python2.patch
}

package()
{
	# Creating directories
	install -d "${pkgdir}/opt"

	cp -r "${srcdir}/${pkgname}" "${pkgdir}/opt/depot_tools"

	# Install repo_fix.sh script
	install -Dm 755 "${srcdir}/repo_fix.sh" "${pkgdir}/opt/depot_tools"

	# Install License
	install -Dm644 "${pkgdir}/opt/depot_tools/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

	# Move manual pages to /usr/share/man
	install -dm755 "${pkgdir}/usr/share/man"
	mv "${pkgdir}/opt/depot_tools/man"/man[0-8] "${pkgdir}/usr/share/man/"

	# Ditto for HTML pages and README files, to /usr/share/doc
	install -dm755 "${pkgdir}/usr/share/doc/${pkgname}"
	mv "${pkgdir}/opt/depot_tools/man/html" "${pkgdir}/usr/share/doc/${pkgname}"
	mv "${pkgdir}/opt/depot_tools"/README*  "${pkgdir}/usr/share/doc/${pkgname}"

	# Remove stray files
	rm -r "${pkgdir}/opt/depot_tools/man"

	# We depend on the "ninja" package, so the wrapper script which chooses a
	# prebuilt version of it or makes a local build is not needed at all, so
	# those are removed and a wrapper script which runs the system-installed
	# /usr/bin/ninja is created instead.
	rm "${pkgdir}/opt/depot_tools"/ninja*
	cat > "${pkgdir}/opt/depot_tools/ninja" <<-EOF
	#! /bin/sh
	exec /usr/bin/ninja
	EOF
	chmod 755 "${pkgdir}/opt/depot_tools/ninja"

  # some commands (e.g., gsutil) calls vpython directly
  install -Ddm755 "$pkgdir"/usr/bin
  ln -s /opt/depot_tools/vpython "$pkgdir"/usr/bin/vpython

	rm -rf "${pkgdir}/opt/depot_tools/.git"
}
