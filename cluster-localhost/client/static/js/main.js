function make() { /// Wait till page is loaded

    $('#main').load("{{ url_for('update') }} #main", function () {
    });
}

$(document).ready(function () {
    $('#detailed').click(function () {
        $('#main').load("{{ url_for('update') }} #main", function () {

        });
    });
});