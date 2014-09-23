var app = (function(app){
    app.GameViewModel = function() {
        var self = this;
        var name = $("#gameType").val();
        self.name = ko.observable(name);
        self.numbers = ko.observableArray([]);
        self.start_date = ko.observable(new Date());
        self.end_date = ko.observable(new Date());
        self.resolution = ko.observableArray(["low", "medium", "high"]);
        self.init = function () {
            $("#successAlert").hide();
            $("#warningAlert").hide();
            $("#fetchingAlert").hide();

        };

        self.removeAll = function(){
            if(self.numbers){
                self.numbers.removeAll();
                window.scrollTo(0,0);
            }
        };

        self.getNumbers = function(most_common, game){
            var start_date = $("#startDatePicker").val();
            var end_date = $("#endDatePicker").val();
            var resolution = $("#resolution").val();
            var url = "/api/lotto?game="+game+"&start_date=" + start_date+"&end_date="+end_date+"&most_common="+most_common+"&resolution="+resolution;
            $("#successAlert").hide();
            $("#warningAlert").hide();
            $("#fetchingAlert").show();
            $("#mostButton").prop("disabled", true);
            $("#leastButton").prop("disabled", true);
            $("#clearButton").prop("disabled", true);
            $.getJSON(url, function (data) {
                self.name(data.name);
                self.start_date(data.start_date);
                self.end_date(data.end_date);
                if(self.numbers){
                    self.numbers.removeAll();
                }

                data.numbers.forEach(function (row) {
                    self.numbers.push(new LottoRow(row));
                });
            }).done(function(){
                $("#successAlert").show();
                $("#warningAlert").hide();
                $("#fetchingAlert").hide();
                setTimeout(function(){
                    $("#successAlert").fadeOut();
                }, 6000)
            }).fail(function(){
                $("#successAlert").hide();
                $("#warningAlert").show();
                $("#fetchingAlert").hide();
                setTimeout(function(){
                    $("#warningAlert").fadeOut();
                },6000);
            }).always(function(){
                $("#mostButton").prop("disabled", false);
                $("#leastButton").prop("disabled", false);
                $("#clearButton").prop("disabled", false);
            })
        };
    };
    return app;
}(app || {}));





function LottoRow(data) {
    this.cell1 = data[0];
    this.cell2 = data[1];
    this.cell3 = data[2];
    this.cell4 = data[3];
    this.cell5 = data[4];
    this.cell6 = data[5];
    this.cell7 = data[6];
}
