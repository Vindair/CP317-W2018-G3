$(function() {
  $(".plus-button").on("click", function() {
    let $picker = $(this).prev('input');
    let old_value = $picker.val();
    if(parseFloat(old_value) < parseFloat($picker.attr('max'))) {
      let new_value = parseFloat(old_value) + 1;
      $picker.val(new_value);
    }
  });
  $(".minus-button").on("click", function() {
    let $picker = $(this).next('input');
    let old_value = $picker.val();
    if(old_value > $picker.attr('min')){
      let new_value = parseFloat(old_value) - 1;
      $picker.val(new_value);
    }
  });
});

