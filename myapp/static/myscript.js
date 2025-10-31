

function validateForm() {
    //alert("Hii")
    var firstname = document.querySelector("#firstname")
    var lastname = document.querySelector("#lastname")
    var phone = document.querySelector("#phone")
    var email = document.querySelector("#Email")
    var password = document.querySelector("#Password")

    var result = true

    //if (firstname.value == "") {
    //    alert("Please fill firstname")
    //     result = false
    //  }
    if (lastname.value == "") {
        alert("Please fill lastname")
        result = false;
    }
    else if (phone.value == "") {
        alert("Please fill phone number")
        result = false;
    }
    else if (email.value == "") {
        alert("Please fill email")
        result = false;
    }
    else if (password.value == "") {
        alert("Please fill password")
        result = false;
    }

    return result;

}


function valiateFirstname(firstname) {
    var errorLabel = document.querySelector("#error_lbl")
    errorLabel.style.color = "red"
    if (firstname.value < 10) {
        errorLabel.innerText = "Firsname should be more than 10 chars"
    }
    else{
        errorLabel.innerText = ""
    }

}