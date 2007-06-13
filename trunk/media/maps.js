//<![CDATA[

// Creates a new incident marker.
function mk_marker(point, desctext, when, mobility, quantity, thief, weapon, period){
	var icon = new GIcon();
	icon.image = "mediafiles/finger.png";
	icon.shadow = "mediafiles/shadow.png";
	icon.iconSize = new GSize(25, 27);
	icon.shadowSize = new GSize(37, 25);
	icon.iconAnchor = new GPoint(6, 20);
	icon.infoWindowAnchor = new GPoint(5, 1);

	var marker = new GMarker(point, icon);

	var desc_html = "<img src=\"/mediafiles/talking.png\"> <strong>Como foi:</strong><br /> <div class=\"desc\">"+desctext+"</div>";
	//var when_html = "<img src=\"/mediafiles/clock.png\"> <strong>Quando foi:</strong><br /><div class=\"desc\">"+when+"</div>";
	var open_icon = "<img src=\"/mediafiles/";
	var close_icon = ".png\"/>";
	//var labels_html = "<img src=\"/mediafiles/tag.png\"> <strong>Rótulos:</strong><br /><div class=\"desc\"><center>"+open_icon+mobility+close_icon+"   "+ open_icon+quantity+close_icon +"   "+ open_icon+thief+close_icon +"   "+ open_icon+weapon+close_icon +"   "+ open_icon+period+close_icon+"</center></div>";
	var labels_html = "<center>"+open_icon+mobility+close_icon+"   "+ open_icon+quantity+close_icon +"   "+ open_icon+thief+close_icon +"   "+ open_icon+weapon+close_icon +"   "+ open_icon+period+close_icon+"</center>";

	GEvent.addListener(marker, "click", function() {marker.openInfoWindowHtml(desc_html+labels_html);});
	return marker;
}


// The Main funcion
function load() {
	var map;
	if (GBrowserIsCompatible()) {
		map = new GMap2(document.getElementById("map"));
		map.addControl(new GLargeMapControl());
		map.addControl(new GMapTypeControl());
		map.setCenter(new GLatLng(-3.746391, -38.574307), 13);

		GDownloadUrl("/crimes/xml", function(data, responseCode) {
			var xml = GXml.parse(data);
			var markers = xml.documentElement.getElementsByTagName("incident");
			for (var i = 0; i < markers.length; i++) {
				var point = new GLatLng(parseFloat(markers[i].getAttribute("lat")), parseFloat(markers[i].getAttribute("lng")));
				var desc = markers[i].getAttribute("summary");
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

		// New input marker
		var old_marker = null;
		
		// When clicks in a empty space in the map
		GEvent.addListener(map, "click", function(overlay, point) {
			if (overlay==null) {
				if(old_marker != null){
					map.removeOverlay(old_marker);
				}
				// yes, you can drag it
				old_marker = new GMarker(point, {draggable: true});
				
				// When you try to drag it, info window closes.
				GEvent.addListener(old_marker, "dragstart", function() {map.closeInfoWindow();});
				
				// Add an callback to an new marker
				GEvent.addListener(old_marker, "click", function() {
					//open_form = "<form name=\"theform\" action=\"/crimes/insert/\" method=\"post\" id=\"theform\">";
					open_form = "<form name=\"theform\" action=\"/crimes/form/\" method=\"post\" id=\"theform\">";
					input_desc = "<img src=\"/mediafiles/talking.png\"> <strong>Como foi?</strong><br /> <textarea name=\"desc\" class=\"desc\" >Insira sua descrição aqui</textarea> <br/>";
					footer = "<img src=\"/mediafiles/cancel.png\"> <input type=\"image\" src=\"/mediafiles/add.png\" />";
					
					point = old_marker.getPoint();
 
					// Some hidden values
					lat = "<input class=\"hidden\" type=\"hidden\" name=\"lat\" value=\""+point.lat()+"\" id=\"lat\" />";
					lng = "<input class=\"hidden\" type=\"hidden\" name=\"lng\" value=\""+point.lng()+"\" id=\"lng\" />";
					from_main = "<input class=\"hidden\" type=\"hidden\" name=\"from_main\" value=\"True\"/>";

					close_form = "</form>";
					html = open_form + input_desc + footer + lat + lng + from_main + close_form;
					old_marker.openInfoWindowHtml(html);				
				});
				map.addOverlay(old_marker);
			}
 		});
	}
}
//]]>
