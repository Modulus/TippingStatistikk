/**
 * Created by Modulus on 25/04/2014.
 */


$(document).ready(function(){

    var getTodaysDate = (function () {
        var local = new Date();
        return local.toJSON().slice(0, 10);
    });

    var getYesterDay = (function(){
        var local = new Date();
        local.setDate(local.getDate() -1 );
        return local.toJSON().slice(0,10);
    });

    var getOlderDate = (function(year){
        var local = new Date();
        local.setYear(year)
        return local.toJSON().slice(0,10);
    });


    $("#lottoStartDatePicker").val(getOlderDate(2004));
    $("#lottoEndDatePicker").val(getTodaysDate);

    $("#lottoStartDatePicker").attr("max", getYesterDay());
    $("#lottoEndDatePicker").attr("max", getTodaysDate());


//    $("#lotto").preventDefault();
//    $("#viking_lotto").preventDefault();
//    $("#extra").preventDefault();
//    $("#keno").preventDefault();

//   $("#lottoLeastButton").click(function(event){

  //      alert("Clicked");
    //    event.preventDefault();
     //   lottoViewModel = new LottoViewModel();

      //  ko.applyBindings(lottoViewModel);
       // lottoViewModel.init();
    //});

//    $("#fromDatePicker").datepicker();

//    $("#viking_lotto").click(function(event){
//       event.preventDefault();
//        lottoViewModel = new LottoViewModel("viking_lotto");
//        ko.applyBindings(lottoViewModel);
//        lottoViewModel.init();
//    });
});