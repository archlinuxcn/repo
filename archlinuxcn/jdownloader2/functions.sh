#!/usr/bin/env bash

function changePath() {
	# check the groups of the current loggedin users
	groups | grep -q -E '(\s|^)jdownloader(\s|$)' >/dev/null
	if [ "$?" -eq  0 ] || isRoot ; then
		export JD_SCOPE="global"
		echo "[global JDownloader scope]"
		umask u=rwx,g=rwx,o=rx
		cd '/opt/JDownloader'
	else
		export JD_SCOPE="user"
		echo "[user JDownloader scope]"
		mkdir -p "${HOME}/.jd"
		cd "${HOME}/.jd"
	fi
}

function changeUser() {
	if isRoot; then
		# restart as user jdownloader
		echo "changing to user \"jdownloader\""
		runuser jdownloader -c "/bin/bash $0 $@" -s /bin/bash
		exit $?
	fi
}

function isRoot() {
	if [ "$(id -u)" -eq "0" ]; then
		return 0
	fi
	return 2
}

function downloadJDownloader() {
	changePath
	if [ ! -f "JDownloader.jar" ]; then
		if ! curl -o JDownloader.jar https://installer.jdownloader.org/JDownloader.jar; then
			echo "Cannot download JDownloader!"
			exit 2
		fi
	fi
}

LOGFILE="JDownloader.service.log"
