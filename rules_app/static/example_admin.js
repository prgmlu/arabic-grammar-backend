// static/example_admin.js
$(document).ready(function() {
    var sentence = $('#id_sentence').val();
    var displayDiv = $('#id_sentence-display');

    // Convert sentence into clickable spans
    for (var i = 0; i < sentence.length; i++) {
        var span = $('<span>').text(sentence[i]).data('index', i).click(onSpanClick);
        displayDiv.append(span);
    }
});

function onSpanClick() {
    var index = $(this).data('index');
    var highlightedIndices = $('#id_highlightedIndices').val().split(',');

    var indexPosition = highlightedIndices.indexOf(index.toString());
    if (indexPosition === -1) {
        highlightedIndices.push(index);
        $('#id_highlightedIndices').val(highlightedIndices.join(','));
        // Highlight the clicked span
        $(this).css('background-color', 'yellow');
    } else {
        highlightedIndices.splice(indexPosition, 1);
        $('#id_highlightedIndices').val(highlightedIndices.join(','));
        // Un-highlight the clicked span
        $(this).css('background-color', '');
    }
}

