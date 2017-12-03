'strict-mode';
module.exports = function (grunt) {
  var config = {
    pkg:  grunt.file.readJSON("package.json"),
    gta: {
      options: {
        stdout: true,
        stderr: true,
      },
      hook: {
        // Adjust this git command to only add the files needed.
        command: 'add package.json README.md .gitignore Gruntfile.js PKGBUILD .SRCINFO',
      },
      tag: {
        command: 'tag v<%= pkg.version %> -sm "Releasing v<%= pkg.version %>"',
      },
      archive: {
        // Adjust this command to only archive what is needed. It currently adds
        // all files.
        command: 'archive --format="tar.gz" --prefix="<%= pkg.name %>-v<%= pkg.version %>/" --output="<%= pkg.name %>-v<%= pkg.version %>.tgz" HEAD -- ./',
      },
      init: {
        command: 'init',
      },
      origin: {
        command: 'remote add origin vcs:/~/enchant-aur.git',
      },
    },
    githooks: {
      all: {
        // Adjust this hook to execute all needed grunt tasks.
        'pre-commit': "shell:hook gta:hook",
      }
    },
    bump: {
      options: {
        files: ['package.json'],
        updateConfigs: ['pkg'],
        commit: true,
        commitFiles: ['package.json'],
        createTag: false,
        push: false,
        prereleaseName: 'prev',
      },
    },
    shell:{
      options: {
        stderr: false
      },
      hook: {
        command: [
          'folder="$(pwd)"',
          'gitroot=$(git rev-parse --show-toplevel)',
          'cd "${gitroot}"',
          'updpkgsums',
          'mksrcinfo',
          'cd "${folder}"'
        ].join('&&')
      },
    },
  };

  // Loading the configuration.
  grunt.initConfig(config);

  // Loading the modules:
  grunt.loadNpmTasks('grunt-git-them-all');
  grunt.loadNpmTasks('grunt-githooks');
  grunt.loadNpmTasks('grunt-bump');
  grunt.loadNpmTasks('grunt-shell');

  // Registering the default task.
  grunt.registerTask('default', ['githooks:all']);
  grunt.registerTask('hooks', ['githooks:all']);
  grunt.registerTask('init', ['gta:init', 'gta:origin']);
  grunt.registerTask('archive', ['gta:archive']);
  grunt.registerTask('release', ['bump:patch', 'gta:tag', 'gta:archive']);
  grunt.registerTask('releaseminor', ['bump:minor', 'gta:tag', 'gta:archive']);
  grunt.registerTask('releasemajor', ['bump:major', 'gta:tag', 'gta:archive']);
  grunt.registerTask('prerelease', ['bump:prerelease', 'gta:tag', 'gta:archive']);
  grunt.registerTask('prepatch', ['bump:prepatch', 'gta:tag', 'gta:archive']);
  grunt.registerTask('preminor', ['bump:preminor', 'gta:tag', 'gta:archive']);
  grunt.registerTask('premajor', ['bump:premajor', 'gta:tag', 'gta:archive']);
};
