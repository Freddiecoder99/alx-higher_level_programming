#!/usr/bin/node

$(document).ready(function() {
  // Handle translation on button click
  $("#btn_translate").click(function() {
    fetchTranslation();
  });

  // Handle translation on ENTER key press
  $("#language_code").keypress(function(event) {
    if (event.which === 13) { // Check for ENTER key (key code 13)
      fetchTranslation();
    }
  });

  function fetchTranslation() {
    const languageCode = $("#language_code").val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

    $.ajax({
      url,
      success: function(data) {
        $("#hello").text(data.translations[0].text);
      },
      error: function(error) {
        $("#hello").text("Error fetching translation");
      },
    });
  }
});
