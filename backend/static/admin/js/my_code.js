$(document).ready(function () {
    let $ = django.jQuery;
    $(".invoice").click(function () {
        let content = $(".breadcrumbs").text();
        let order_id = Number(content.match(/\d+/)[0]);
        $.ajax({
            url: "http://localhost:8000/app/invoice",
            method: 'get',
            dataType: 'json',
            data: {order_id: order_id},
            success: function(){
                alert("data");
            }
        });
        console.log(order_id);
    })
})