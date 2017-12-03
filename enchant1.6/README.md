# Enchant Aur

A wrapper library for generic spell checking.

* Uses the following third party elements:
  * Building the packages is enhanced and partially automated by [grunt][]

## Getting started

The following commands are needed to get a certain degree of automation into
the process:

* Install npm : **npm Install**
* Make sure that the Gruntfile.js contains other needed tasks.
* Only if you start this as a fresh project: Initialize the git environment.
	This includes adding the defined repository as origin: **grunt init**.
* Install the grunt hooks into the local repo: **grunt hooks**

## Building the package:

The following commands have you covered:
* Just building a tar package: grunt archive
* Tagging the current HEAD commit with the version information from the
	package.json and archiving it into a tar package:
	* grunt prerelease : Bumps the version to the next prerelease (prev) version.
	* grunt prepatch : Bumps the version to the next prerelease patch version (increases the patch number)
	* grunt preminor: Bumps the version to the next prereleae minor version.
	* grunt premajor : Bumps the version to the next prerelease major version.
	* grunt release: Bumps the version to the next proper patch version.
	* grunt releaseminor: Bumps the version to the next proper minor version.
	* grunt releasemajor: Bumps the version to the next proper major version.

## Changelog

[Grunt]:				http://gruntjs.com/									"Grunt Task Runner"
