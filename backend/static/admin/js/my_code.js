$(document).ready(function () {
    let $ = django.jQuery;
    let order_id = $(".breadcrumbs > a:last-child ").text();
    console.log(order_id);
    $(".invoice").click(function () {
        // $.ajax({
        //     type: "POST",
        //     url: "/edit_favorites/",
        //     data: {
        //         'video': $('#test').val() // from form
        //     },
        //     success: function () {
        //         $('#message').html("<h2>Contact Form Submitted!</h2>")
        //     }
        // });
        console.log('ddd');
    })
})