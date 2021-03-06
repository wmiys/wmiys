import { AlertTop }        from "../../classes/AlertTop";
import { ALERT_TOP_TYPES } from "../../classes/AlertTop";
import { ApiWrapper }      from "../../classes/API-Wrapper";
import { SpinnerButton }   from "../../classes/SpinnerButton";
import { UrlParser }       from "../../classes/UrlParser";

const ePasswordResetForm = {
    form: '.password-reset-form',
    inputClasses: '.password-reset-input',
    submitButton: '.password-reset-btn',
    inputs: {
        new: '#password-reset-input-new',
        confirm: '#password-reset-input-confirm',
    },
}

const containers = {
    form: '.password-reset-container-form',
    success: '.password-reset-container-success',
}

const mErrorMessages = {
    required: 'Required',
    noMatch: 'Passwords do not match',
}

const mSpinnerButton = new SpinnerButton(ePasswordResetForm.submitButton, $(ePasswordResetForm.submitButton).text());

// password reset id located in the URL
const mPasswordResetID = UrlParser.getPathValue(1);


/**********************************************************
Main logic
**********************************************************/
$(document).ready(function() {
    addEventListeners();
});


/**********************************************************
Add the event listeners to the page
**********************************************************/
function addEventListeners() {
    $(ePasswordResetForm.submitButton).on('click', function() {
        resetPassword();
    });

    $(ePasswordResetForm.inputClasses).on('keydown', function() {
        removeInvalidFeedback(this);
    });

    // user hits enter while an text input is active
    $(ePasswordResetForm.inputClasses).on('keypress', function(e) {
        if (e.keyCode == 13) {
            e.preventDefault();
            resetPassword();
        }
    });
}


/**********************************************************
Attempt to reset the user's password
**********************************************************/
async function resetPassword() {
    mSpinnerButton.showSpinner();
    
    if (!validateForm()) {
        mSpinnerButton.reset();
        return;
    }

    const newPassword = $(ePasswordResetForm.inputs.new).val();
    
    let apiResponse = await ApiWrapper.requestPutPasswordReset(mPasswordResetID, newPassword);

    if (apiResponse.ok) {
        toggleContainers();
    } 
    else {
        mSpinnerButton.reset();
        
        const alertTop = new AlertTop(ALERT_TOP_TYPES.DANGER, 'Something went wrong! Password was not updated.');
        alertTop.show();
    }
}


function toggleContainers() {
    $('.container').toggleClass('d-none');
}



/**********************************************************
Make sure the form is valid before sending the update request
**********************************************************/
function validateForm() {

    if (!inputsHaveValues()) {
        return false;
    } 
    else if (!inputValuesMatch()) {
        return false;
    }

    return true;
}


/**********************************************************
Checks if both inputs have a value.

Returns a bool:
    true: both inputs have a value
    false: an input is empty
**********************************************************/
function inputsHaveValues() {
    // new
    const inputValueNew = $(ePasswordResetForm.inputs.new).val();
    if (inputValueNew.length < 1) {
        displayInvalidFeedback(ePasswordResetForm.inputs.new, mErrorMessages.required);
        return false;
    }

    // confirm
    const inputValueConfirm = $(ePasswordResetForm.inputs.confirm).val();
    if (inputValueConfirm.length < 1) {
        displayInvalidFeedback(ePasswordResetForm.inputs.confirm, mErrorMessages.required);
        return false;
    }

    return true;
}

/**********************************************************
Checks if both input values match.

Returns a bool:
    true: inputs match
    false: inputs do not match
**********************************************************/
function inputValuesMatch() {
    const inputValueNew = $(ePasswordResetForm.inputs.new).val();
    const inputValueConfirm = $(ePasswordResetForm.inputs.confirm).val();

    if (inputValueNew == inputValueConfirm) {
        return true;
    } else {
        displayInvalidFeedback(ePasswordResetForm.inputs.confirm, mErrorMessages.noMatch);
        return false;
    }
}


/**********************************************************
Display an invalid feedback message on the screen.

Inputs:
    invalidInput: input element that is invalid
    message: message to be displayed
**********************************************************/
function displayInvalidFeedback(invalidInput, message) {
    $(invalidInput).addClass('is-invalid').closest('.form-group').find('.invalid-feedback').text(message);
}

/**********************************************************
Remove an invalid feedback message display.

Parms:
    invalidInput: the input whose invalid feedback needs to be removed
**********************************************************/
function removeInvalidFeedback(invalidInput) {
    $(invalidInput).removeClass('is-invalid');
}