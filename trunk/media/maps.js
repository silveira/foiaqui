//<![CDATA[

function mk_marker(point, desctext, when, mobility, quantity, thief, weapon, period){
	var icon = new GIcon();
	icon.image = "mediafiles/finger.png";
	icon.shadow = "mediafiles/shadow.png";
	icon.iconSize = new GSize(25, 27);
	icon.shadowSize = new GSize(37, 25);
	icon.iconAnchor = new GPoint(6, 20);
	icon.infoWindowAnchor = new GPoint(5, 1);

	var marker = new GMarker(point, icon);

	var desc_html = "<img src=\"/mediafiles/talking.png\"> <strong>Como foi:</strong><br /> <div class=\"desc\">"+desctext+"</div><img src=\"/mediafiles/clock.png\"> <strong>Quando foi:</strong><br /><div class=\"desc\">"+when+"</div>"
	var open_icon = "<img src=\"/mediafiles/"
	var close_icon = ".png\"/>"

	var icons_html = "<center>"+open_icon+mobility+close_icon+"   "+ open_icon+quantity+close_icon +"   "+ open_icon+thief+close_icon +"   "+ open_icon+weapon+close_icon +"   "+ open_icon+period+close_icon+"</center>"

	GEvent.addListener(marker, "click", function() {marker.openInfoWindowHtml(desc_html+icons_html);});
	return marker;
}

// <textarea rows="10" cols="30"> The cat was playing in the garden. </textarea>

function load() {
	if (GBrowserIsCompatible()) {
		var map = new GMap2(document.getElementById("map"));
		map.addControl(new GSmallMapControl());
		map.addControl(new GMapTypeControl());
		map.setCenter(new GLatLng(-3.746391, -38.574307), 13);

		GDownloadUrl("/crimes/xml", function(data, responseCode) {
			var xml = GXml.parse(data);
			var markers = xml.documentElement.getElementsByTagName("incident");
			for (var i = 0; i < markers.length; i++) {
				var point = new GLatLng(parseFloat(markers[i].getAttribute("lat")), parseFloat(markers[i].getAttribute("lng")));
				var desc = markers[i].getAttribute("desc");
				var when = markers[i].getAttribute("date");
				var mobility = markers[i].getAttribute("mobility");
				var quantity = markers[i].getAttribute("quantity");
				var thief = markers[i].getAttribute("thief");
				var weapon = markers[i].getAttribute("weapon");
				var period = markers[i].getAttribute("period");
				var marker = mk_marker(point, desc, when, mobility, quantity, thief, weapon, period);
				map.addOverlay(marker);
			}
		});
	}
}
//]]>
