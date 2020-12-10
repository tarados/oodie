$(document).ready(function () {
    let $ = django.jQuery;
    $(".invoice").click(function (evt) {
        evt.preventDefault();
        let content = $(".breadcrumbs").text();
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