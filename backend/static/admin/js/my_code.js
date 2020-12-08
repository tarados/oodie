$(document).ready(function () {
    let $ = django.jQuery;
    let content = $(".breadcrumbs").text();
    let order_id = Number(content.match(/\d+/)[0]);
    $(".invoice").click(function () {
        console.log(order_id);
        $.ajax({
            type: "GET",
            url: "app/invoice/2",
            success: function () {
                $('#message').html("<h2>Contact Form Submitted!</h2>")
            }
        });
        console.log('ddd');
    })
})