$(document).ready(function () {
    // Confguração global
    $.fn.datepicker.defaults.format = 'dd/mm/yyyy';
    $.fn.datepicker.defaults.useCurrent = true;
    $.fn.datepicker.defaults.todayHighlight = true;
    $.fn.datepicker.defaults.autoclose = true;
    $.fn.datepicker.defaults.language = 'pt-BR';
    $.fn.datepicker.defaults.clearBtn = true;
    $.fn.datepicker.defaults.forceParse = true;

    aplicarDatepicker();

    // $('.datetimepicker').datetimepicker({
    //     format: 'DD/MM/YYYY HH:mm',
    //     // locale: 'pt-br',
    //     icons: {
    //         time: 'fa fa-clock-o',
    //         date: 'fa fa-calendar',
    //         up: 'fa fa-chevron-up',
    //         down: 'fa fa-chevron-down',
    //         previous: 'fa fa-chevron-left',
    //         next: 'fa fa-chevron-right',
    //         today: 'fa fa-dot-circle-o',
    //         clear: 'fa fa-trash',
    //         close: 'fa fa-times'
    //     }
    // })
});

function aplicarDatepicker() {

    let datepicker = $('.datepicker');

    datepicker.datepicker('destroy');

    datepicker.datepicker();

    // Remove o autocomplete dos campos, para evitar o surgimento das datas já usadas
    // em outros formulários, que o browser sugere.
    datepicker.on('focus', function (e) {
        e.preventDefault();
        $(this).attr("autocomplete", "off");
    });
}

function aplicarDatepickerFormset() {

    setTimeout(function () {
        let datepicker = $('.datepicker-formset');

        datepicker.datepicker('destroy');

        datepicker.datepicker();

        // Remove o autocomplete dos campos, para evitar o surgimento das datas já usadas
        // em outros formulários, que o browser sugere.
        datepicker.on('focus', function (e) {
            e.preventDefault();
            $(this).attr("autocomplete", "off");
        });
    }, 200);

}