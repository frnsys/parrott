define([
			 // Application.
			 'app',

			 // Modules.
			 'modules/tweet'
], function(app, Tweet) {
	var Router = Backbone.Router.extend({
		initialize: function() {
			var collections = {
				tweets: new Tweet.Collection()
			}

			// Attach collections to the router.
			// i.e. this.tweets
			_.extend(this, collections);
		},

		routes: {
			'': 'index',
            'audited': 'audited',
            'audited/:page': 'audited',
            'audit': 'audit',
            'audit/:page': 'audit'
		},

		index: function() {
            // Create and insert the view,
            // using the 'main' layout (main.jade).
			app.useLayout('main').setViews({
				".tweets": new Tweet.Views.List({ tweets: this.tweets })
			}).render();

            // Set the proper API endpoint
            // to fetch from.
            this.tweets.url = '/api/tweet';
			this.tweets.fetch({ reset: true });
		},

		audited: function(page) {
            var page = page || 0

            // Reset/empty out the collections.
            this.reset();

            // Create and insert the view.
			app.useLayout('main').setViews({
				".tweets": new Tweet.Views.List({ tweets: this.tweets })
			}).render();

            // Set the proper API endpoint
            // to fetch from.
            this.tweets.url = '/api/audited/' + page.toString();
            this.tweets.fetch({ reset: true });
		},

        audit: function(page) {
            var page = page || 0

            // Reset/empty out the collections.
            this.reset();

            // Create and insert the view.
			app.useLayout('main').setViews({
				".tweets": new Tweet.Views.List({ tweets: this.tweets })
			}).render();

            // Set the proper API endpoint
            // to fetch from.
            this.tweets.url = '/api/audit/' + page.toString();
            this.tweets.fetch({ reset: true });
        },

		reset: function() {
			// Reset collections to initial state.
			if (this.tweets.length) {
				this.tweets.reset();
			}
		},

		// Shortcut for building a url.
		go: function() {
			return this.navigate(_.toArray(arguments).join("/"), true);
		}
	});

	return Router;
});
