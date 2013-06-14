define([
			 "app"
],
function(app) {

	// Create a module based off
	// the app template (in app.js)
	var Tweet = app.module();

	Tweet.Model = Backbone.Model.extend({
		defaults: {
			tweet: "",
			user: "",
            links: [],
            audited: false
		},

        parse: function(response) {
            return response
        },

		initialize: function() {
		}
	});

	Tweet.Collection = Backbone.Collection.extend({
		model: Tweet.Model,

		// Where to fetch the data from
		url: function() {
			return "/api/tweet";
		},

		// How to handle the fetched data
		parse: function(response) {
			return response.data;
		},

		initialize: function(models, options) {
		}
	});

	Tweet.Views.Item = Backbone.View.extend({
		template:"tweet/item",
		tagName:"li",

		// The data that gets passed to the view
		serialize: function() {
			return {
				tweet: this.model.toJSON()
			};
		},

		// Bind some events
		events: {
			'click .delete': 'delete'
		},

		delete: function() {
            if ( confirm("Are you sure you want to delete this tweet?") ) {
                this.model.destroy();
                this.$el.fadeOut();
            }
		}

	});

	Tweet.Views.List = Backbone.View.extend({
		template: "tweet/list",
		className: "tweet-list",

		// The data that gets passed to the view
		serialize: function() {
			return {
				collection: this.options.tweets,
				count: this.options.tweets.length
			};
		},

		// Do stuff before the view is rendered
		beforeRender: function() {
			var view = this;

			// For each tweet in collection
			this.options.tweets.each(function(tweet) {

				// Insert a Tweet item view with tweet to the ul
				view.insertView("ul", new Tweet.Views.Item({
					model: tweet
				}));

			});
		},

		initialize: function() {
			// Listen to some events
			this.listenTo(this.options.tweets, {
				"reset": function() {
					this.render();
				}
			});
		}
	});

	Tweet.Views.Single = Backbone.View.extend({
		template: "tweet/single",
		className: "single-tweet",
		tagName:"section",

		serialize: function() {
			return {
				tweet: this.model.toJSON()
			};
		}
	});

	// Return the module for AMD compliance
	return Tweet;
});
