require([
				// Application.
				'app',

				// Main Router.
				'router'

// Get the whole application started.
], function(app, Router) {
	// Create our router and
	// attach it to the app.
	app.router = new Router();

    // HTML History API!
	Backbone.history.start({ pushState: true, root: app.root });

	// Relative links will be navigated
	// through the Backbone router.
	// If the link has a `data-bypass` attr,
	// this special behavior will be ignored.
	$(document).on('click', 'a[href]:not([data-bypass])', function(evt) {
		var href = {
			prop: $(this).prop('href'),
			attr: $(this).attr('href')
		};

		var root = location.protocol + '//' + location.host + app.root;

		// Check if the link is relative
		if (href.prop.slice(0, root.length) === root) {
			evt.preventDefault();
			Backbone.history.navigate(href.attr, true);
		}
	});
});
