$("#chainlist_1").change(function () {
    $("#brancher").toggle(!isNaN(+$(this).val()));
})