define(['jade'], function(jade) { if(jade && jade['runtime'] !== undefined) { jade = jade.runtime; }

this["JST"] = this["JST"] || {};

this["JST"]["app/templates/audit"] = function anonymous(locals, attrs, escape, rethrow, merge
/**/) {
attrs = attrs || jade.attrs; escape = escape || jade.escape; rethrow = rethrow || jade.rethrow; merge = merge || jade.merge;
var buf = [];
with (locals || {}) {
var interp;
var __indent = [];
buf.push('\n<h2>Audit Tweets</h2>\n<div class="tweets"></div>');
}
return buf.join("");
};

this["JST"]["app/templates/audited"] = function anonymous(locals, attrs, escape, rethrow, merge
/**/) {
attrs = attrs || jade.attrs; escape = escape || jade.escape; rethrow = rethrow || jade.rethrow; merge = merge || jade.merge;
var buf = [];
with (locals || {}) {
var interp;
var __indent = [];
buf.push('\n<h2>Audited Tweets</h2>\n<div class="tweets"></div>');
}
return buf.join("");
};

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
buf.push('' + escape((interp = tweet.user) == null ? '' : interp) + ' ( ' + escape((interp = tweet.tweet) == null ? '' : interp) + ' )<span class="delete">delete me</span><span class="mark-positive">positive</span><span class="mark-negative">negative</span>');
if ( tweet.positive)
{
buf.push('+');
}
else
{
buf.push('-');
}
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
buf.push('\n<ul></ul>\n<div class="pagination">');
if ( count > 0)
{
if ( page > 0)
{
 var prev_page = path + (parseInt(page) - 1)
buf.push('<a');
buf.push(attrs({ 'href':(prev_page) }, {"href":true}));
buf.push('>Prev</a>');
}
if ( count == 10)
{
 var next_page = path + (parseInt(page) + 1)
buf.push('<a');
buf.push(attrs({ 'href':(next_page) }, {"href":true}));
buf.push('>Next</a>');
}
}
buf.push('\n</div>');
}
return buf.join("");
};

return this["JST"];

});