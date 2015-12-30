function sendCoordinates() {
    $.ajax({
        url: "http://127.0.0.1:5000/sendCoordinates",
        data: {},
        type: "GET",
        crossDomain: true,
        dataType: "jsonp",
        success: function(data) {
            if (data.status == 'success') {
                $("#serverresponse").html("Success");
            } else {
                $("#serverresponse").text("Failed");
            }

        },
        error: function(xhr, status) {
            $("#serverresponse").text("Server might be offline.");
        },
        complete: function(xhr, status) {

        }
    });
}