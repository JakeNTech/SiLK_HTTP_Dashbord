function home(){
    //document.getElementById("home_page").className="active"
    //document.getElementById("today_stats").className="in-active"
    document.getElementById("dynamic_page").innerHTML="<div id='center_box'><h2>SiLK HTTP Server</h2><p><i>Please Select what you would like to do from the menu bar</i></p><div id='silk_status'></div></div>"
    fetch("/api/silk_status")
    .then(function (response) {
        return response.text()
    }).then(function (text) {
        text = JSON.parse(text)
        document.getElementById("silk_status").innerHTML="<p>YAF Status: "+text.yaf+"</p><p>rwflowpack Status: "+text.rwflowpack+"</p></div>"
    })
};

function today_stats(){
    //document.getElementById("home_page").className="in-active"
    //document.getElementById("today_stats").className="active"
    fetch("/api/today_stats")
    .then(function (response) {
        return response.text()
    }).then(function (text) {
        console.log(text)
        text = JSON.parse(text)
        document.getElementById("dynamic_page").innerHTML="<div id='center_box'><p>Stat for the current day, "+text.current_date+": </p><p>Total Packets: "+text.packet_count+"</p><p>Total Records: "+text.record_count+"</p><p>Total Data: "+text.data_count+" "+text.data_unit+"</p><div id='graphs'></div></div>"
        graph_paths = text.graph_paths
        //console.log(graph_paths)
        //document.getElementById('graphs').innerHTML="<img src='"+graph_paths.bytes_time+"'>"
        document.getElementById('graphs').innerHTML="<a href='"+graph_paths.bytes_time+"'<button id='btn'>Button</button>"
    })
}