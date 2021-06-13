function home(){
	document.getElementById("dynamic_page").innerHTML="<div id='center_box'><h2>SiLK HTTP Server</h2><p><i>Please Select what you would like to do from the menu bar</i></p><div id='silk_status'></div></div>"
	fetch("/api/silk_status")
	.then(function (response) {
    	return response.text()
  	}).then(function (text) {
  		text = JSON.parse(text)
  		console.log(text)
  		document.getElementById("silk_status").innerHTML="<p>YAF Status: "+text.yaf+"</p><p>rwflowpack Status: "+text.rwflowpack+"</p></div>"
	})
};


// function current_time(){
// 	fetch("/api/current_time")
// 	.then(function (response) {
//     	return response.text();
//   	}).then(function (text) {
//   		document.getElementById("dynamic_page").innerHTML="<div id='center_box'> <p> The Current Time is: "+JSON.parse(text).current_time+"</p></div>"
// 	})
// }
// function echo_system(){
// 	fetch("/api/echo_system")
// 	.then(function (response) {
//     	return response.text();
//   	}).then(function (text) {
//   		document.getElementById("echo_system_box").innerHTML="<p>"+JSON.parse(text).echo_system+"</p>"
// 	})
// }

