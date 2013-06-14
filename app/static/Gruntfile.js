module.exports = function(grunt) {

	// Configuration
	// =======================================
	grunt.initConfig({
		// Watch
		watch: {
            options: { livereload: true },
			files: [
				'vendor/**/*',
				'app/styles/**/*.scss',
				'app/styles/**/*.sass',
				'app/templates/**/*.jade',
				'app/*.js',
				'app/modules/**/*.js',
				'data/**/*',
				'source/icons/*',
                '!app/styles/exts/_icons.scss'
			],
			tasks: ['sass', 'jade', 'fontcustom']
		},

		// Compile SASS/SCSS
		// Since all other stylesheets are @import-ed in index.scss,
		// that's the only one we need to compile.
		sass: {
			app: {
				files: {
					'app/styles/index.css': 'app/styles/index.sass'	
				}
			}
		},

		// Compile Jade templates
		jade: {
			compile: {
				options: {
					pretty: true,
					client: true,
					amd: true,
					compileDebug: false
				},
				files: {
					'app/templates/templates.js': ['app/templates/**/*.jade']
				}
			}
		},

		// Font Custom
		shell: {
			fontcustom: {
				command: 'fontcustom compile source/icons'
			}
		},
		copy: {
			fontcustom: {
				files: [
					{src: ['source/icons/fontcustom/*.woff'], dest: 'app/styles/fonts/icons.woff'},
					{src: ['source/icons/fontcustom/*.eot'],  dest: 'app/styles/fonts/icons.eot'},
					{src: ['source/icons/fontcustom/*.svg'],  dest: 'app/styles/fonts/icons.svg'},
					{src: ['source/icons/fontcustom/*.ttf'],  dest: 'app/styles/fonts/icons.ttf'}
				]
			}
		},
		replace: {
			fontcustom: {
				src: ['source/icons/fontcustom/fontcustom.css'],
				dest: ['app/styles/exts/_icons.scss'],
				replacements: [{
					from: /fontcustom_[^.]+/g,
					to: 'fonts/icons'
				}, {
					from: 'fontcustom',
					to: 'icons'
				}]
			}
		}

	});

	// Define grunt tasks
	// =======================================
	grunt.registerTask('default', ['watch']);
	grunt.registerTask('fontcustom', ['shell:fontcustom', 'copy:fontcustom', 'replace:fontcustom']);

	// Load grunt packages
	// =======================================
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-contrib-jade');
	grunt.loadNpmTasks('grunt-contrib-connect');
	grunt.loadNpmTasks('grunt-contrib-copy');
	grunt.loadNpmTasks('grunt-text-replace');
	grunt.loadNpmTasks('grunt-shell');

};