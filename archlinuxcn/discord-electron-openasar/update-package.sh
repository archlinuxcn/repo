#!/usr/bin/env bash

set -euo pipefail

readonly all_off="$(tput sgr0)"
readonly bold="${all_off}$(tput bold)"
readonly white="${bold}$(tput setaf 7)"
readonly blue="${bold}$(tput setaf 4)"
readonly red="${bold}$(tput setaf 1)"

msg() {
	printf "${blue}::${white} $1${all_off}\n"
}

error() {
	printf "${red}::${white} $1${all_off}\n"
}

msgbegin() {
	printf "${blue}::${white} $1"
}

msgend() {
	printf "$1${all_off}\n"
}


readonly krisp_zip='discord_krisp-1.zip'
readonly krisp_bin='discord_krisp.node'

# head to directory of this script
cd $(dirname "$0")

# update package to version used in PKGBUILD
source PKGBUILD

msg "Running updpkgsums (Updating checksums)"
updpkgsums

msg "Running mksrcinfo (Updating SRCINFO file)"
makepkg --printsrcinfo > .SRCINFO

msg "Getting Krisp module"
curl -O "https://dl.discordapp.net/apps/linux/${_pkgver:-${pkgver}}/modules/${krisp_zip}"
unzip "${krisp_zip}" "${krisp_bin}"

msg "Checking if Krisp module is patchable (watch output)"
python krisp-patcher.py "${krisp_bin}"

#msg "Updating Krisp module checksum"
#readonly chcksm=$(b2sum "${krisp_bin}.orig" | head -c 128)
#sed -i "s/^_krisp_b2sum='.*'$/_krisp_b2sum='${chcksm}'/" PKGBUILD

msgbegin "Cleaning up... "
rm -f "${krisp_zip}" "${krisp_bin}" "${krisp_bin}.orig"

msgend "Done"
