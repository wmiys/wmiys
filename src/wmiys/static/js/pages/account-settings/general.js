import { ApiWrapper }      from "../../classes/API-Wrapper";
import { SpinnerButton }   from "../../classes/SpinnerButton";


/************************************************
This object represents the General Information form.
It includes all of its inputs and buttons.
*************************************************/
const eFormBasic = {
    form: $('.form-account-settings-basic'),

    inputs: {
        nameFirst: '#form-account-settings-basic-name-first',
        nameLast : '#form-account-settings-basic-name-last',
        email    : '#form-account-settings-basic-email',
        dob :      '#form-account-settings-basic-dob',
    },

    buttons: {
        submit: '#form-account-settings-basic-submit',
    },

    inputClassIdentifier: '.form-account-settings-basic-input',

    getValues: function() {
        const values = {};

        for (const inputKey of Object.keys(eFormBasic.inputs)) {
            values[inputKey] = $(eFormBasic.inputs[inputKey]).val();
        }

        return values;
    },
}

// button to update their password
const eBtnUpdatePassword = '#btn-update-password';


const eSideNav = {
    container: $('.card-account-settings-sidenav'),

    profileSection: {
        picture: $('.img-profile-pic'),
        nameFirst: $('.profile-info-name-first'),
        nameLast: $('.profile-info-name-last'),
    }
}

/************************************************
Represents the alert display section.
*************************************************/
const eAlertDisplay = {
    alert: '.alert-top',
    close: '.btn-close-alert',
}

/************************************************
Main logic
*************************************************/
$(document).ready(function() {
    addEventListeners();
    activateSidelink();
});

/************************************************
Registers all of the page event listeners.
*************************************************/
function addEventListeners() {

    $(eFormBasic.buttons.submit).on('click', function() {
        updateUserInfo();
    });

    // hide the alert display
    $(eAlertDisplay.close).on('click', function() {
        $(this).closest('.alert').prop('hidden', true);
    });

    // update password
    $(eBtnUpdatePassword).on('click', function() {
        updatePassword();
    });
}


function activateSidelink() {
    $('#v-pills-general-tab').addClass('active');
}


/************************************************
Sends an update request to the api
*************************************************/
async function updateUserInfo() {
    disableSaveButton();

    const formattedData = getUserDataForApiRequest();
    const apiResponse = await ApiWrapper.requestPutUser(formattedData);

    if (apiResponse.ok) {
        updateUserInfoSuccess();
    }
    else {
        updateUserInfoError(await apiResponse.text());
    }
}

/************************************************
Get a JS object containing all the update user form data with correct keys.
*************************************************/
function getUserDataForApiRequest() {
    const formValues = eFormBasic.getValues();

    const dataWithValidKeys = {
        email: formValues.email,
        name_first: formValues.nameFirst,
        name_last: formValues.nameLast,
        birth_date: formValues.dob,
    }

    return dataWithValidKeys;
}




/************************************************
Callback for a successful api request to update the user info
*************************************************/
function updateUserInfoSuccess() {
    enableSaveButton();
    displayAlert('Updated successfully.', 'success');
}


/************************************************
Callback for an unsuccessful api request to update the user info
*************************************************/
function updateUserInfoError(responseText) {
    enableSaveButton();
    console.error('updateUserInfoError');
    console.error(responseText);
}

/************************************************
Disabled the save changes button
*************************************************/
function disableSaveButton() {
    const initWidth = $(eFormBasic.buttons.submit).width();
    $(eFormBasic.buttons.submit).prop('disabled', true).width(initWidth);
}

/************************************************
Enables the save changes button
*************************************************/
function enableSaveButton() {
    const initWidth = $(eFormBasic.buttons.submit).width();
    $(eFormBasic.buttons.submit).width(initWidth).prop('disabled', false);
}

/************************************************
Displays an alert on the screen
*************************************************/
function displayAlert(message='Success', alertType='success') {
    const alertClass = `alert-${alertType}`;
    $(eAlertDisplay.alert).prop('hidden', false).addClass(alertClass).find('.message').html(message);
}


/************************************************
Send a request to update a user's password
*************************************************/
async function updatePassword() {
    // disable the spinner button
    const buttonText = $(eBtnUpdatePassword).text();
    const spinnerBtn = new SpinnerButton(eBtnUpdatePassword, buttonText);
    spinnerBtn.showSpinner();
    
    // get the user's email
    const userData = await (await ApiWrapper.requestGetUser()).json();
    const email = userData.email;

    // tell the api that they want to update their password
    const apiResponse = await (await ApiWrapper.requestPostPasswordReset(email)).json();

    // redirect the user to the password reset page
    window.location.href = `/password-reset/${apiResponse.id}`;

    // spinnerBtn.reset();
}
