$(document).ready(function () {
    let $ = django.jQuery;

    let content = $(".breadcrumbs").text();
    $("input.invoice").css('display', 'block');
    $(".invoice").click(function (evt) {
        evt.preventDefault();
        let order_id = Number(content.match(/\d+/)[0]);
        $.ajax({
            url: "/app/invoice",
            method: 'get',
            data: {order_id: order_id},
            success: function () {
                location.reload();
            }
        });
    })
})
