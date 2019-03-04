/**
 * 改变分类名
 */

!function (factory) {
    "use strict";

	// CommonJS/Node.js
	if (typeof require === "function" && typeof exports === "object" && typeof module === "object")
    {
        module.exports = factory;
    }
	else if (typeof define === "function")  // AMD/CMD/Sea.js
	{
        if (define.amd) // for Require.js
        {
            /* Require.js define replace */
        }
        else
        {
		    define(["jquery"], factory);  // for Sea.js
        }
	}
	else
	{
        window.article = factory();
	}
}(function () {

    var article = function () {
        $("ul[data-id='sort-name'] li a").click(function () {
            let s = $("button[data-id='sort-name']");
            s.attr('data-value', $(this).html());
            s.html($(this).html())
        });
        $("ul[data-id='label-name'] li a").click(function () {
            let s = $("button[data-id='label-name']");
            s.attr('data-value', $(this).html());
            s.html($(this).html())
        });
    }

});