$(function() {
// report model
  let $form_model = $('.report-model');
  let $form_login = $form_model.find('#report');
  let $main_nav = $('#title');
  $main_nav.on('click', function (event) {
    if ($(event.target).is($main_nav)) {
      $(this).children('ul').toggleClass('is-visible');
    } else {
      $main_nav.children('ul').removeClass('is-visible');
      if ($(event.target).is('#report-button')) {
        $form_model.addClass('is-visible');
      }
      report_selected();
    }

  });

  $('.report-model').on('click', function (event) {
    if ($(event.target).is($form_model) || $(event.target).is('.close-form')) {
      $form_model.removeClass('is-visible');
    }
  });
  $(document).keyup(function (event) {
    if (event.which == '27') {
      $form_model.removeClass('is-visible');
    }
  });


  function report_selected() {
    $form_login.addClass('is-selected');
  }

});

//source: https://css-tricks.com/snippets/jquery/move-cursor-to-end-of-textarea-or-input/
jQuery.fn.putCursorAtEnd = function() {
  return this.each(function() {
    // If this function exists...
    if (this.setSelectionRange) {
      // ... then use it (Doesn't work in IE)
      // Double the length because Opera is inconsistent about whether a carriage return is one character or two. Sigh.
      var len = $(this).val().length * 2;
      this.setSelectionRange(len, len);
    } else {
      // ... otherwise replace the contents with itself
      // (Doesn't work in Google Chrome)
      $(this).val($(this).val());
    }
  });
};
