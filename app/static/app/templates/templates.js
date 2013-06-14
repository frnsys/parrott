define(['jade'], function(jade) { if(jade && jade['runtime'] !== undefined) { jade = jade.runtime; }

this["JST"] = this["JST"] || {};

this["JST"]["app/templates/main"] = function anonymous(locals, attrs, escape, rethrow, merge
/**/) {
attrs = attrs || jade.attrs; escape = escape || jade.escape; rethrow = rethrow || jade.rethrow; merge = merge || jade.merge;
var buf = [];
with (locals || {}) {
var interp;
var __indent = [];
buf.push('\n<div class="tweets"></div>');
}
return buf.join("");
};

this["JST"]["app/templates/tweet/item"] = function anonymous(locals, attrs, escape, rethrow, merge
/**/) {
attrs = attrs || jade.attrs; escape = escape || jade.escape; rethrow = rethrow || jade.rethrow; merge = merge || jade.merge;
var buf = [];
with (locals || {}) {
var interp;
var __indent = [];
buf.push('' + escape((interp = tweet.user) == null ? '' : interp) + ' ( ' + escape((interp = tweet.tweet) == null ? '' : interp) + ' )<span class="delete">delete me</span>');
}
return buf.join("");
};

this["JST"]["app/templates/tweet/list"] = function anonymous(locals, attrs, escape, rethrow, merge
/**/) {
attrs = attrs || jade.attrs; escape = escape || jade.escape; rethrow = rethrow || jade.rethrow; merge = merge || jade.merge;
var buf = [];
with (locals || {}) {
var interp;
var __indent = [];
buf.push('\n<h4>You have ' + escape((interp = count) == null ? '' : interp) + ' books</h4>\n<ul></ul>');
}
return buf.join("");
};

this["JST"]["app/templates/tweet/single"] = function anonymous(locals, attrs, escape, rethrow, merge
/**/) {
attrs = attrs || jade.attrs; escape = escape || jade.escape; rethrow = rethrow || jade.rethrow; merge = merge || jade.merge;
var buf = [];
with (locals || {}) {
var interp;
var __indent = [];
buf.push('\n<h1>' + escape((interp = tweet.user) == null ? '' : interp) + '</h1>\n<h5>' + escape((interp = tweet.tweet) == null ? '' : interp) + '</h5>');
}
return buf.join("");
};

return this["JST"];

});