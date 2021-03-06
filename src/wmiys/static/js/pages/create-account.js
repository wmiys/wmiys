import { ApiWrapper }      from "../classes/API-Wrapper";
import { CommonHtml }      from "../classes/Common-Html";
// import { LocalStorage }    from "../classes/LocalStorage";/
import { Utilities }       from "../classes/Utilities";

// Page elements
const e_formCreateAccount = $('#form-create-account');
const e_inputFirstName    = $('#form-create-account-name-first');
const e_inputLastName     = $('#form-create-account-name-last');
const e_inputDob          = $('#form-create-account-dob');
const e_inputEmail        = $('#form-create-account-email');
const e_inputPassword     = $('#form-create-account-password');
const e_btnSubmit         = $('#form-create-account-submit');

/**********************************************************
Main logic
**********************************************************/
$(document).ready(function() {
    // LocalStorage.clear();
    addListeners();
});


/**********************************************************
Add all the event listeners to the page
**********************************************************/
function addListeners() {
    $(e_btnSubmit).on('click', createAccount);
    
    $(e_formCreateAccount).find('input').on('keypress', function(e) {
        if (e.keyCode == 13) {
            e.preventDefault();
            createAccount();
        }
    });
}


/**********************************************************
Initialize the flat pickr elements
**********************************************************/
function loadFlatpickr() {
    $(e_inputDob).flatpickr({
        altInput: true,
        altFormat: "F j, Y",
        dateFormat: "Y-m-d",
    });
}


/**********************************************************
Create a new account actions
**********************************************************/
async function createAccount() {
    disableSubmitButton();

    // ensure all the input fields are valid 
    if (!Utilities.validateForm(e_formCreateAccount)) {
        enableSubmitButton();
        return;
    }

    let inputValues = getInputValues();
    const apiResponse = await ApiWrapper.requestPostUser(inputValues);

    apiResponse.ok ? createAccountSuccess() : createAccountError(apiResponse.text);
}


/**********************************************************
Actions to take when the user successfully created an account
**********************************************************/
function createAccountSuccess() {
    enableSubmitButton();
    window.location.href = '/';
}

/**********************************************************
Actions to take when the user unsuccessfully created an account
**********************************************************/
function createAccountError(error) {
    enableSubmitButton();
    console.log(error);
    Utilities.displayAlert('Error.');
}

/**********************************************************
Disables the submit button. Waiting for API response
**********************************************************/
function disableSubmitButton() {
    $(e_btnSubmit).html(CommonHtml.spinnerSmall);
    $(e_btnSubmit).prop('disabled', true);
}


/**********************************************************
Enables the submit button
**********************************************************/
function enableSubmitButton() {
    $(e_btnSubmit).html('Create account').prop('disabled', false);
}

/**********************************************************
Returns the form input values
**********************************************************/
function getInputValues() {
    const values2 = {
        name_first: $(e_inputFirstName).val(),
        name_last:  $(e_inputLastName).val(),
        birth_date: $(e_inputDob).val(),
        email:      $(e_inputEmail).val(),
        password:   $(e_inputPassword).val(),
    };

    return values2
}




