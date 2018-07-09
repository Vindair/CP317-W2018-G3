$(function() {
// Login/Sign-up Model
  let $form_model = $('.login-signup-model');
  let $form_login = $form_model.find('#login-button');
  let $form_signup = $form_model.find('#signup-button');
  let $form_forgot_password = $form_model.find('#reset-password');
  let $form_model_tab = $('.switch-buttons');
  let $tab_login = $form_model_tab.children('li').eq(0).children('a');
  let $tab_signup = $form_model_tab.children('li').eq(1).children('a');
  let $forgot_password_link = $form_login.find('.user-form-bottom-message a');
  let $back_to_login_link = $form_forgot_password.find('.user-form-bottom-message a');
  let $main_nav = $('.main-nav');

  $main_nav.on('click', function (event) {
    if ($(event.target).is($main_nav)) {
      $(this).children('ul').toggleClass('is-visible');
    } else {
      $main_nav.children('ul').removeClass('is-visible');
      if ($(event.target).is('#login-span') || $(event.target).is('#signup-span')) {
        $form_model.addClass('is-visible');
      }
      ($(event.target).is('#signup-span')) ? signup_selected() : login_selected();
    }

  });

  $('.login-signup-model').on('click', function (event) {
    if ($(event.target).is($form_model) || $(event.target).is('.close-form')) {
      $form_model.removeClass('is-visible');
    }
  });
  $(document).keyup(function (event) {
    if (event.which == '27') {
      $form_model.removeClass('is-visible');
    }
  });

  $form_model_tab.on('click', function (event) {
    event.preventDefault();
    ($(event.target).is($tab_login)) ? login_selected() : signup_selected();
  });
  $('.hide-password').on('click', function () {
    var $this = $(this),
      $password_field = $this.prev('input');

    ('password' == $password_field.attr('type')) ? $password_field.attr('type', 'text') : $password_field.attr('type', 'password');
    ('Hide' == $this.text()) ? $this.text('Show') : $this.text('Hide');

    $password_field.putCursorAtEnd();
  });

  $forgot_password_link.on('click', function (event) {
    event.preventDefault();
    forgot_password_selected();
  });

  $back_to_login_link.on('click', function (event) {
    event.preventDefault();
    login_selected();
  });

  function login_selected() {
    $form_login.addClass('is-selected');
    $form_signup.removeClass('is-selected');
    $form_forgot_password.removeClass('is-selected');
    $tab_login.addClass('selected');
    $tab_signup.removeClass('selected');
  }

  function signup_selected() {
    $form_login.removeClass('is-selected');
    $form_signup.addClass('is-selected');
    $form_forgot_password.removeClass('is-selected');
    $tab_login.removeClass('selected');
    $tab_signup.addClass('selected');
  }

  function forgot_password_selected() {
    $form_login.removeClass('is-selected');
    $form_signup.removeClass('is-selected');
    $form_forgot_password.addClass('is-selected');
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
