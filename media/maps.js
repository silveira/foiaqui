//<![CDATA[

function mk_marker(point, desctext, date){
	var icon = new GIcon();
	icon.image = "mediafiles/finger.png";
	icon.shadow = "mediafiles/shadow.png";
	icon.iconSize = new GSize(25, 27);
	icon.shadowSize = new GSize(37, 25);
	icon.iconAnchor = new GPoint(6, 20);
	icon.infoWindowAnchor = new GPoint(5, 1);

	var marker = new GMarker(point, icon);

	GEvent.addListener(marker, "click", function() {marker.openInfoWindowHtml("<img src=\"mediafiles/talking.png\"> <strong>Como foi:</strong><br /> <div class=\"desc\">"+desctext+"</div><img src=\"mediafiles/clock.png\"> <strong>Quando foi:</strong><br /><div class=\"desc\">"+date+"</div>");});
	return marker;
}

// <textarea rows="10" cols="30"> The cat was playing in the garden. </textarea>

function load() {
	if (GBrowserIsCompatible()) {
		var map = new GMap2(document.getElementById("map"));
		map.addControl(new GSmallMapControl());
		map.addControl(new GMapTypeControl());
		map.setCenter(new GLatLng(-3.746391, -38.574307), 13);

		GDownloadUrl("crimes", function(data, responseCode) {
			var xml = GXml.parse(data);
			var markers = xml.documentElement.getElementsByTagName("incident");
			for (var i = 0; i < markers.length; i++) {
				var point = new GLatLng(parseFloat(markers[i].getAttribute("lat")), parseFloat(markers[i].getAttribute("lng")));
				var desc = markers[i].getAttribute("desc");
				var date = markers[i].getAttribute("date");
				var marker = mk_marker(point, desc, date);
				map.addOverlay(marker);
			}
		});
	}
}
//]]>