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

			// Attach collections to the router
			// i.e. this.books
			_.extend(this, collections);
		},

		routes: {
			'': 'index',
            'audited': 'audited',
            'audit': 'audit'
		},

		index: function() {
			// Create main layout (main.jade)
			app.useLayout('main').setViews({
				".tweets": new Tweet.Views.List({ tweets: this.tweets })
			}).render();

            // Set the proper API endpoint
            // to fetch from.
            this.tweets.url = '/api/tweet';
			this.tweets.fetch({ reset: true });
		},

		audited: function() {
            // Reset/empty out the collections.
            this.reset();

			app.useLayout('main').setViews({
				".tweets": new Tweet.Views.List({ tweets: this.tweets })
			}).render();

            // Set the proper API endpoint
            // to fetch from.
            this.tweets.url = '/api/audited';
            this.tweets.fetch({ reset: true });
		},

        audit: function() {
            // Reset/empty out the collections.
            this.reset();

			app.useLayout('main').setViews({
				".tweets": new Tweet.Views.List({ tweets: this.tweets })
			}).render();

            // Set the proper API endpoint
            // to fetch from.
            this.tweets.url = '/api/audit'
            this.tweets.fetch({ reset: true });
        },

		reset: function() {
			// Reset collections to initial state
			if (this.tweets.length) {
				this.tweets.reset();
			}
		},

		// Shortcut for building a url
		go: function() {
			return this.navigate(_.toArray(arguments).join("/"), true);
		}
	});

	return Router;
});
