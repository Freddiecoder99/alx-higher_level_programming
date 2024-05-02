#!/usr/bin/node

$(document).ready(function() {
  $("#btn_translate").click(function() {
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
  });
});
