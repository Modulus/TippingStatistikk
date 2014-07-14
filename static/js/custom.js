/**
 * Created by Modulus on 25/04/2014.
 */
$(document).ready(function(){
//    $("#lotto").preventDefault();
//    $("#viking_lotto").preventDefault();
//    $("#extra").preventDefault();
//    $("#keno").preventDefault();

    $("#lotto").click(function(event){
        event.preventDefault();
        lottoViewModel = new LottoViewModel();

        ko.applyBindings(lottoViewModel);
        lottoViewModel.init();
    });

//    $("#fromDatePicker").datepicker();

//    $("#viking_lotto").click(function(event){
//       event.preventDefault();
//        lottoViewModel = new LottoViewModel("viking_lotto");
//        ko.applyBindings(lottoViewModel);
//        lottoViewModel.init();
//    });
});