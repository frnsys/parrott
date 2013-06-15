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

        // Properly parse the JSON
        // response from the backend.
        parse: function(response) {
            return response
        }
	});

	Tweet.Collection = Backbone.Collection.extend({
		model: Tweet.Model,

		// Where to fetch the data from.
		url: function() {
			return "/api/tweet";
		},

		// How to handle the fetched
        // JSON response.
		parse: function(response) {
			return response.data;
		}
	});

	Tweet.Views.Item = Backbone.View.extend({
		template:"tweet/item",
		tagName:"li",

		// The data that gets passed to the view.
		serialize: function() {
			return {
				tweet: this.model.toJSON()
			};
		},

		// Bind some events.
		events: {
			'click .delete': 'delete',
            'click .mark-positive': 'markPositive',
            'click .mark-negative': 'markNegative'
		},

        // Delete a tweet.
		delete: function() {
            if ( confirm("Are you sure you want to delete this tweet?") ) {
                this.model.destroy();
                this.$el.fadeOut();
            }
		},

        // Mark a tweet as positive.
        markPositive: function() {
            this.model.set({
                'audited': true,
                'positive': true
            });
            this.model.save();
        },

        // Mark a tweet as negative.
        markNegative: function() {
            this.model.set({
                'audited': true,
                'positive': false
            });
            this.model.save();
        }

	});

	Tweet.Views.List = Backbone.View.extend({
		template: "tweet/list",
		className: "tweet-list",

		// The data that gets passed to the view.
		serialize: function() {
			return {
				collection: this.options.tweets,

                // For building the pagination links.
				count: this.options.tweets.length,
                page: this.options.page,
                path: this.options.path
			};
		},

		// Do stuff before the view is rendered.
		beforeRender: function() {
			var self = this;

			// For each tweet in collection
			this.options.tweets.each(function(tweet) {

				// Insert a Tweet item view with tweet to the ul
				self.insertView("ul", new Tweet.Views.Item({
					model: tweet
				}));

			});
		},

		initialize: function() {
			// Listen to some events.
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

	// Return the module for AMD compliance.
	return Tweet;
});
