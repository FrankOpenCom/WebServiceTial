function validateForm() {
  var co_presenter = document.forms["topic"]["Co-Presenter"].value;
  var co_email = document.forms["topic"]["Co-Email"].value;
  if (co_presenter != "" && co_email == "") {
    alert("Co-presenter Email must be filled out");
    return false;
  }
}

function Warning() {
  return confirm('Are you sure?');
}