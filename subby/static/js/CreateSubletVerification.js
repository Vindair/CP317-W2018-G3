$(function () {
    $('#create-sublet-submit').on('click', function (e) {
        let title = $('#listing-title');
        let street_address = $('#street_address');
        let city = $('#city');
        let postal_code = $('#postal_code');
        let price = $('#price');
        let description = $('#listing-description');
        let lat = $('#lat');
        let lng = $('#lng');
        let duration = $('#listing-duration');
        let images = $('#files');
        let error = false;

        title.popover('hide');
        price.popover('hide');
        description.popover('hide');
        duration.popover('hide');
        images.popover('hide');
        $('#pac-input').popover('hide');

        if (!title.val()) {
            console.log('1');
            title.popover('show');
            error = true;
        }
        console.log(duration.val());
        if (!duration.val()) {
            console.log('2');
            duration.popover('show');
            error = true;
        }
        if (!street_address.val() || !city.val() || !postal_code.val() || !lat.val() || !lng.val()) {
            console.log('3');
            $('#pac-input').popover('show');
            error = true;
        }
        if (!price.val()) {
            console.log('4');
            price.popover('show');
            error = true;
        }
        if (!description.val()) {
            console.log('5');
            description.popover('show');
            error = true;
        }
        if (!images.val()) {
            console.log('6');
            images.popover('show');
            error = true;
        }
        if (error) {
            console.log('7');
            //e.preventDefault();
            return false;
        }
    });
});