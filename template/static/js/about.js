$(function() {
    var tickerLength = $('.scroll-accordion-container-notice ul li').length;
    var tickerHeight = $('.scroll-accordion-container-notice ul li').outerHeight();
    $('.scroll-accordion-container-notice ul li:last-child').prependTo('.scroll-accordion-container-notice ul');
    $('.scroll-accordion-container-notice ul').css('marginTop', -tickerHeight);
  
    function moveTop() {
      $('.scroll-accordion-container-notice ul').animate({
        marginTop: -tickerHeight
      }, 600, function() {
        $('.scroll-accordion-container-notice ul li:first-child').appendTo('.scroll-accordion-container-notice ul');
        $('.scroll-accordion-container-notice ul').css('marginTop', '');
      });
    }
  
    setInterval(function() {
      moveTop();
    }, 3000);
  });

  $(function() {
    var tickerLength = $('.scroll-accordion-container-news ul li').length;
    var tickerHeight = $('.scroll-accordion-container-news ul li').outerHeight();
    $('.scroll-accordion-container-news ul li:last-child').prependTo('.scroll-accordion-container-news ul');
    $('.scroll-accordion-container-news ul').css('marginTop', -tickerHeight);
  
    function moveTop() {
      $('.scroll-accordion-container-news ul').animate({
        marginTop: -tickerHeight
      }, 600, function() {
        $('.scroll-accordion-container-news ul li:first-child').appendTo('.scroll-accordion-container-news ul');
        $('.scroll-accordion-container-news ul').css('marginTop', '');
      });
    }
  
    setInterval(function() {
      moveTop();
    }, 3000);
  });
  $(function() {
    var tickerLength = $('.scroll-accordion-container-cit ul li').length;
    var tickerHeight = $('.scroll-accordion-container-cit ul li').outerHeight();
    $('.scroll-accordion-container-cit ul li:last-child').prependTo('.scroll-accordion-container-cit ul');
    $('.scroll-accordion-container-cit ul').css('marginTop', -tickerHeight);
  
    function moveTop() {
      $('.scroll-accordion-container-cit ul').animate({
        marginTop: -tickerHeight
      }, 600, function() {
        $('.scroll-accordion-container-cit ul li:first-child').appendTo('.scroll-accordion-container-cit ul');
        $('.scroll-accordion-container-cit ul').css('marginTop', '');
      });
    }
  
    setInterval(function() {
      moveTop();
    }, 3000);
  });
  

