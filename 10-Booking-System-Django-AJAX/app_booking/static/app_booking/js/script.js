"use strict";

const formatTimeToAMPM = (time) => {
    const ampm = time < 12 ? 'AM' : 'PM';
    const t = time < 12 ? time : time > 12 ? time - 12 : time;
    const label = `${t} ${ampm}`; 
    return label;
}; 

const getCRSFToken = (formID) => {
    const form = document.getElementById(formID);
    if (!form) {return null;}
    const csrfToken = form.querySelector('input[name="csrfmiddlewaretoken"]').value;
    return csrfToken; 
}

// rest javascript code in the html templates files !
