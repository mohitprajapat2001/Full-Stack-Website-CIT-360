$(function () {
  var loc = window.location.pathname.split("/")[1]; // returns the full URL
  if (loc = 'profile') {
    $(document).ready(function () {
      $('.li-home a').removeClass('active');

      // Add "active" class to li-accounts
      $('.li-accounts a').addClass('active');
    });
  }// Remove "active" class from li-home

  $('a.menu-trigger').click(function () {

    $('ul.nav').toggle();
    $("#user_button").css({
      display: 'block',
    });
    $('a.menu-trigger').toggleClass('active')
  })
});

// SignIn SignUp
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
  container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
  container.classList.remove("right-panel-active");
});

function validateForm() {
  var roleSelect = document.getElementById("roleSelect");
  var emailInput = document.getElementById("register_email");

  // Check if the selected role is "faculty" and validate the email
  if (roleSelect.value === "faculty") {
      var email = emailInput.value;

      // Perform the validation based on the email domain
      if (!email.endsWith("@cit.ac.in")) {
          alert("Faculty email must end with @cit.ac.in");
          return false; // Prevent form submission
      }
  }

  return true; // Allow form submission
}