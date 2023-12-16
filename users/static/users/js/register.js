let selectedCountryId;
const citiesSelect = $('select[name="city"]');
citiesSelect.prop('disabled', true)

$('input[name="country"]').click(() => {
    if (citiesSelect.is(':disabled')) {
        citiesSelect.prop('disabled', false)
    }

    selectedCountryId = $('input[name="country"]:checked').val()
    $.get(`/locations/country/${selectedCountryId}/cities/`, {}, (data) => {
        citiesSelect.html('')
        data.forEach((city) => {
            citiesSelect.html(citiesSelect.html() + `<option value="${city['pk']}">${city['fields']['name']}</option>`)
        })
    })
})