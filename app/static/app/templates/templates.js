define(['jade'], function(jade) { if(jade && jade['runtime'] !== undefined) { jade = jade.runtime; }

this["JST"] = this["JST"] || {};

this["JST"]["app/templates/audit"] = function anonymous(locals, attrs, escape, rethrow, merge
/**/) {
attrs = attrs || jade.attrs; escape = escape || jade.escape; rethrow = rethrow || jade.rethrow; merge = merge || jade.merge;
var buf = [];
with (locals || {}) {
var interp;
var __indent = [];
buf.push('\n<h2><span>Audit Tweets</span></h2>\n<div class="tweets"></div>');
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
buf.push('\n<h2><span>Audited Tweets</span></h2>\n<div class="tweets"></div>');
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
buf.push('' + escape((interp = tweet.tweet) == null ? '' : interp) + ' – <span class="user">');
var __val__ = tweet.user
buf.push(escape(null == __val__ ? "" : __val__));
buf.push('</span>\n<div class="actions"><span class="delete icon-close"></span><span class="mark-negative icon-minus"></span><span class="mark-positive icon-plus"></span></div>');
if ( tweet.audited)
{
if ( tweet.positive)
{
buf.push('\n<div class="marker positive"></div>');
}
else
{
buf.push('\n<div class="marker negative"></div>');
}
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