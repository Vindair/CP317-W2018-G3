$(function(){
   $('.edit-btn').on('click', function(){
        $('.edit-disabled-fieldset').prop('disabled', false);
        $(this).attr('style', 'display: none;');
        $('.acc-submit-btn').attr('style', '');
   });
});