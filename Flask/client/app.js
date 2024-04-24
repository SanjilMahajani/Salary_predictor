$(document).ready(function() {
    $('.submit').click(function() {
        onClickedEstimatePrice();
    });
});

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var company = $('#uiCompany').val();
    var title = $('#uiTitle').val();
    var YOE = $('#uiYOE').val();
  
    var url = "http://127.0.0.1:5000/salary"; //Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/salary"; 

    $.post(url, {
        Company: company,
        Title: title,
        Experience: parseInt(YOE)
        
    }, function(data, status) {
        console.log(data.estimated_salary);
        $('#uiEstimatedPrice').html("<h2>" + data.estimated_salary.toString() + " Lakh</h2>");
        console.log(status);
    });
}
