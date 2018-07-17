$(function () {
    $('.login-btn').on('click', function () {
        $('#signup-modal').modal('hide');
        $('#login-modal').modal('show');
    });

    $('.signup-btn').on('click', function () {
        $('#login-modal').modal('hide');
        $('#signup-modal').modal('show');
    });
});
