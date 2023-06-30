$(function () {
  var loc = window.location.pathname.split("/")[1];
  if (loc = 'panel') {
    $(document).ready(function () {
      $("header.header-area").addClass("background-header");
      $('.li-home a').removeClass('active');
      $('.li-student a').addClass('active');
    });
  }
  $('a.menu-trigger').click(function () {
    $('ul.nav').toggle();
    $("#user_button").css({
      display: 'block',
    });
    $('a.menu-trigger').toggleClass('active')
  })
});
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

//   Note Search
var searchBar = document.getElementById("notesearch");
searchBar.addEventListener("input", filterData);
function filterData() {
  var searchTerm = searchBar.value.toLowerCase(); // Get the search term and convert to lowercase
  var rows = document.getElementById("notesTableBody").getElementsByTagName("tr"); // Get the rows to filter

  // Loop through each row and hide/show based on the search term
  for (var i = 0; i < rows.length; i++) {
    var row = rows[i];
    var rowData = row.textContent.toLowerCase();

    if (rowData.includes(searchTerm)) {
      row.style.display = "table-row"; // Show the row
    } else {
      row.style.display = "none"; // Hide the row
    }
  }
}

// Modal Form Handle
$(document).ready(function () {
  $('#myForm').submit(function (e) {
    e.preventDefault();

    course = $("#course").val()
    semester = $("#semester").val()
    csrfToken = getCookie('csrftoken')
    // Send an AJAX POST request to the notesdownload endpoint
    $.ajax({
      type: 'POST',
      url: '/notesdownload',
      headers: { 'X-CSRFToken': csrfToken },
      data: {
        'semester': semester,
        'course': course,
      },
      success: function (response) {
        // Handle the successful response and update the table
        console.log(response.status)
        data = response.usernotes
        console.log(response.usernotes)
        $('#notesTableBody').empty();
        // Loop through the response data and create table rows
        if (data.length == '') {
          var row = '<tr>' +
            '<td colspan="5" class="text-center"><img width="40" height="40" class="center-image" src="https://img.icons8.com/external-smashingstocks-mixed-smashing-stocks/68/external-404-error-cloud-computing-smashingstocks-mixed-smashing-stocks.png" alt="external-404-error-cloud-computing-smashingstocks-mixed-smashing-stocks"/>Data Not Found</td>' +
            '</tr>';
          // Append the row to the table body
          $('#notesTableBody').empty();
          $('#notesTableBody').append(row);
          console.log("done" + row);
        } else {
          for (var i = 0; i < data.length; i++) {
            var row = `<tr>
            <td> ${i + 1} </td>
            <td> ${data[i].title}</td>
            <td> ${data[i].course} </td>
            <td> ${data[i].semester} </td>
            <td><a href="${data[i].file}" class="btn btn-outline-primary"  download>Download</a></td>
            </tr>`;
            $('#notesTableBody').append(row);
            console.log("done" + row);
          }
        }
        // Close the modal

      },
      error: function (xhr, status, error) {
        // Handle any error during the AJAX request
        console.log(error);
      }
    });
  });
});
