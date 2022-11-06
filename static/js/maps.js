// Code for Google Maps API from Code Institute's Bootstrap Resume Project

function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 6,
        center: {
            lat: 52.5,
            lng: -2.134766,
        }
    }); 

    var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

    var locations = [
        {lat: 50.825017, lng: -0.153250},
        {lat: 51.495169, lng: -0.141662},
        {lat: 53.483148, lng: -2.238485}
    ];

    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    var markerCluster = new MarkerClusterer(map, markers,
    {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
}