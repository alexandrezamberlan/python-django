$(document).ready(function () {

    aplicarMascaras();

});

function aplicarMascaras() {
    $('.mask_cpf').mask('999.999.999-99', {placeholder: ""});
    $('.mask_data').mask('99/99/9999', {placeholder: ""});
    $('.mask_data_hora').mask('99/99/9999 99:99', {placeholder: ""});
    $('.mask_cep').mask('99.999-999', {placeholder: ""});
    $('.mask_tel_fixo').mask('99-9999-9999', {placeholder: ""});
    $('.mask_tel_celular').mask('99-99999-9999', {placeholder: ""});
    $('.mask_tel_celular_internacional').mask('+99?9-99-99999-9999', {placeholder: ""});
    $('.mask_inscricao_estadual').mask('999/9999999', {placeholder: ""});
    $('.mask_cnpj').mask('99.999.999/9999-99', {placeholder: ""});

    /* Maskmoney */
    //permite somente moedas positivas
    // $('.mask_moeda').maskMoney({allowNegative: false, allowZero: true, thousands: '.', decimal: ','});
    // $('.mask_moeda_3_decimais').maskMoney({allowNegative: false, allowZero: true, thousands: '.', decimal: ',', precision:3});
    // //permite moedas negativas e positivas
    // $('.mask_moeda_negativa').maskMoney({allowNegative: true, allowZero: true, thousands: '.', decimal: ','});
    // $('.mask_moeda_negativa_3_decimais').maskMoney({allowNegative: true, allowZero: true, thousands: '.', decimal: ',', precision:3});
}