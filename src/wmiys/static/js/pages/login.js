import { ApiWrapper } from "../classes/API-Wrapper";
import { CommonHtml } from "../classes/Common-Html";
import { Utilities } from "../classes/Utilities";

// Page elements
const e_formLogin         = $('#form-login');
const e_inputEmail        = $('#form-login-email');
const e_inputPassword     = $('#form-login-password');
const e_btnSubmit         = $('#form-login-submit');


/**********************************************************
Main logic
**********************************************************/
$(document).ready(function() {
    addListeners();
});


/**********************************************************
Add all the event listeners to the page
**********************************************************/
function addListeners() {
    $(e_btnSubmit).on('click', attemptLogin);

    $('.form-control').on('keypress', function(e) {
        if (e.keyCode == 13) {
            e.preventDefault();
            attemptLogin();
        }
    });

    $(e_formLogin).find('.form-control').on('keypress', clearInvalidInputClass);
}

/**********************************************************
Attempt to login 
**********************************************************/
async function attemptLogin() {
    disableSubmitButton();

    // ensure all the input fields are valid 
    if (!Utilities.validateForm(e_formLogin)) {
        enableSubmitButton();
        return;
    }

    const inputValues = getInputValues();
    const apiResponse = await ApiWrapper.requestLogin(inputValues);

    if (apiResponse.ok) {
        loginSuccess();
    } 
    else {
        loginError();
    }

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
    $(e_btnSubmit).html('Log in').prop('disabled', false);
}

/**********************************************************
Returns the form input values
**********************************************************/
function getInputValues() {
    const values = {};
    values.email      = $(e_inputEmail).val();
    values.password   = $(e_inputPassword).val();

    return values;
}

/**********************************************************
Actions to take when the user successfully logged in
**********************************************************/
function loginSuccess(result,status,xhr) {
    // enableSubmitButton();

    // go to the home page
    window.location.href = window.location.origin;
}

/**********************************************************
Actions to take when the user unsuccessfully tried to log in
**********************************************************/
function loginError(xhr, status, error) {
    console.error(xhr);
    console.error(status);
    console.error(error);

    enableSubmitButton();
    Utilities.displayAlert('Invalid login credentials.');

    $(e_inputPassword).val('');
    $(e_formLogin).find('.form-control').addClass('is-invalid');
}

/**********************************************************
Clear the invalid input classes
**********************************************************/
function clearInvalidInputClass() {
    $(e_formLogin).find('.form-control').removeClass('is-invalid');
}
