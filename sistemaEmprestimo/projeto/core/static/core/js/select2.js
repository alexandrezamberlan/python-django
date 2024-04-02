$(document).ready(function () {

    iniciarSelect2()

});

function iniciarSelect2() {
    // Adicionando select2 sem busca em todos os selects que não possuem um select2 atribuido
    $('select').not('.select2').not('.select2_disabled').addClass('select2_sem_busca');

    // Opções globais do select2
    $.fn.select2.defaults.set("theme", "bootstrap4");

    $.fn.select2.defaults.set("width", "100%");

    $.fn.select2.defaults.set("selectOnClose", "true");

    $('.select2').select2();

    $('.select2_sem_busca').select2({
        minimumResultsForSearch: -1
    });
}

// Abre select2 on focus
$(document).on('focus', '.select2-selection.select2-selection--single', function (e) {
    $(this).closest(".select2-container").siblings('select:enabled').select2('open');
});

// Tira o focus no close
$('select.select2').on('select2:closing', function (e) {
    $(e.target).data("select2").$selection.one('focus focusin', function (e) {
        e.stopPropagation();
    });
});

function adicionarSelect2Option(select2, id, texto) {

    if (select2.find("option[value='" + id + "']").length) {
        select2.val(id).trigger('change');
    } else {

        var data = {
            id: id,
            text: texto
        };

        var newOption = new Option(data.text, data.id, true, true);
        select2.append(newOption).trigger('change');

        // Removendo option extra que é dicionada abaixo da div
        $('.select2-container--below option').remove();

        // Limpa o que foi digitado após a inserção
        $(".select2-search__field").eq(0).val('')

    }

}

function adcicionarOpcaoNovoCadastroSelect2(select2, idModal) {

    /* Adiciona a opção de novo cadastro quando o usuario clica no componente.
    Quando seleciona a opção de adicionar, abre a modal que corresponde ao id passado como parametro
    */
    select2.on('click', () => {
        $(".select2-results:not(:has(a))")
            .append('<div class="select2-link text-center">' +
                '<a href="#" onclick="$(' + '\'#' + idModal + '\'' + ').modal(\'show\');" ' +
                'style="padding: 6px;height: 20px;display: inline-table;' +
                ' align-content: center; cursor: pointer!important;">Novo Cadastro</a> </div>')
    });

}

function aplicarSelect2Formset() {

    setTimeout(function () {
        $('.select2_disabled').select2();
    }, 200);

}