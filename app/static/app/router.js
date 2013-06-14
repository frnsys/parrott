define([
			 // Application.
			 'app',

			 // Modules.
			 'modules/tweet'
], function(app, Tweet) {
	var Router = Backbone.Router.extend({
		initialize: function() {
            console.log("hello");
			var collections = {
				tweets: new Tweet.Collection()
			}

			// Attach collections to the router
			// i.e. this.books
			_.extend(this, collections);
		},

		routes: {
			'': 'index',
			'tweet/:id': 'tweet'
		},

		index: function() {
            console.log("index");
			// Create main layout (main.jade)
			app.useLayout('main').setViews({
				".tweets": new Tweet.Views.List({ tweets: this.tweets })
			}).render();

			this.tweets.fetch({ reset: true });
		},

		tweet: function(id) {
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
