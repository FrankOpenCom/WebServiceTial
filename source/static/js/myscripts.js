function validateForm() {
    var co_presenter = document.forms["topic"]["Co-Presenter"].value;
    var co_email = document.forms["topic"]["Co-Email"].value;
    if (co_presenter != "" && co_email == "") {
      alert("Email must be filled out");
      return false;
    }
  }