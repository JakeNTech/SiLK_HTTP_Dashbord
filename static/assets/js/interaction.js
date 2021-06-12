function get_time(){
	fetch("/api/echo_system")
	.then(function (response) {
    	return response.text();
  	}).then(function (text) {
  		document.getElementById("time_box").innerHTML="<p>"+text+"</p>"
	})
}