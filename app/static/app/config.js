// Set the require.js configuration for your application.
require.config({

  // Initialize the application with
	// the main application file (main.js)
	// and the JamJS generated configuration file.
	deps: ["../vendor/jam/require.config", "main"],

	paths: {
    // Use the underscore build of Lo-Dash to minimize incompatibilities.
		"lodash": "../vendor/jam/lodash/dist/lodash.underscore",
		"jade": "../vendor/jam/jade-runtime/jade.runtime"

    // Put additional paths here.
	},

	map: {
    // Ensure Lo-Dash is used instead of underscore.
		"*": { "underscore": "lodash" }

    // Put additional maps here.
	},

	shim: {
    // Put shims here.
	}

});
