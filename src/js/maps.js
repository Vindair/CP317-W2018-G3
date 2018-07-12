function init_map() {
  var mapOptions = {
    center: new google.maps.LatLng(43.467736, -80.523015),
    zoom: 15,
    gestureHandling: 'greedy',
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map=new google.maps.Map(document.getElementById("map"), mapOptions);
}

function init_listing_map() {
  var mapOptions = {
    center: new google.maps.LatLng(43.467736, -80.523015),
    zoom: 15,
    gestureHandling: 'greedy',
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map=new google.maps.Map(document.getElementById("listing-map"), mapOptions);

  let latLng = {lat:43.467736, lng: -80.523015};
  var marker = new google.maps.Marker({
    position: latLng,
    map: map,
    title: 'Marker'
  });
}
