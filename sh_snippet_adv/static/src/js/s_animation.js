odoo.define('sh_snippet_adv.s_animation', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
var registry = publicWidget.registry;
var animations = require('website.content.snippets.animation');

registry.shSnippetAdvAnimationWidget = animations.Animation.extend({
    selector: '.animate__animated',	
    disabledInEditableMode: true,
    effects: [{
        startEvents: 'scroll',
        update: '_animateOnScroll',
    }],

    /**
     * @constructor
     */
    init: function () {
        this._super(...arguments);
        this.HasAnimated = false;
    },

    start: function () {
    	this.animationType = this.$el.attr('data-order') || "";
        return this._super.apply(this, arguments);
    },
    
    
    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------
    /**
     * Called when the window is scrolled
     *
     * @private
     * @param {integer} scroll
     */
    _animateOnScroll: function (scroll) {    	
    	var oTop = this.$el.offset().top - window.innerHeight;
		  if (this.HasAnimated == false && $(window).scrollTop() > oTop) {
			  console.log("animation start here");
			  //counter part start here
			  /*
			  var looping = true;
			  this.$el.find('.js_cls_counter_number').each(function () {
				   var $this = $(this);
				   looping = true;
				   jQuery({ Counter: 0 }).animate({ Counter: $this.text() }, {
				     duration: 3000,
				     easing: 'swing',
				     step: function () {
				       $this.text(Math.ceil(this.Counter));
				     }
				   });
				 }).promise().done( function(){
					 
					 looping = false;
				 });	
			  */
			  //counter part ends here
			  this.HasAnimated = true;
		  }        
    },

});



});
