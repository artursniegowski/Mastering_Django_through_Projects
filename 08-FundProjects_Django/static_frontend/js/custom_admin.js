"use strict"
window.addEventListener('DOMContentLoaded', () => {
    const applyColorChangeField = (selectorCSS) => { 
        // changing the color of the project field
        const fieldsProjectToChange = document.querySelectorAll(selectorCSS);
        if (fieldsProjectToChange) {
            fieldsProjectToChange.forEach( element => {
                const value = element.innerText;
                try {
                    const parsedValue = parseFloat(value);
                    if (isNaN(parsedValue)) {
                        throw new Error("Invalid float value");
                    }
                    if (parsedValue<=0){
                        element.classList.add('gree-project-field');
                    } else {
                        element.classList.add('red-project-field');
                    }
                } catch (error) { 
                    console.log('Error parsing float value:', error.message);
                }  
            })
        } 
    }; 
    applyColorChangeField("#result_list tbody tr td.field-project_money_rest");
    
    // adding functionality to the buttons 
    const handleButtonClicks = (buttonElementsAll, csrfToken) => {
        buttonElementsAll.forEach(reactivateButtonProjectElement => {
            reactivateButtonProjectElement.addEventListener('click', () => {
                reactivateButtonProjectElement.disabled = true;
                const url = reactivateButtonProjectElement.dataset.url;
                fetch(url, {
                    headers: {
                        'Accept':'application/json',
                        'Content-Type':'application/json',
                        'X-CSRFToken':csrfToken,
                    },
                    method: 'POST',
                    credentials: 'same-origin',
                }) 
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // console.log("OK - data")
                        // console.log(data)
                        // or update value with javascript ??
                        setTimeout( () => {
                            reactivateButtonProjectElement.disabled = false;
                            location.reload();
                        },200);
                    } else {
                        console.log("Error - data");
                        console.log(data.error);
                        reactivateButtonProjectElement.classList.add("red-project-field");
                        setTimeout( () => {
                            reactivateButtonProjectElement.classList.remove("red-project-field");
                            reactivateButtonProjectElement.disabled = false;
                        },300);
                        // console.log(data)
                    }
                })
                .catch( error => {
                    console.log(error);
                    reactivateButtonProjectElement.disabled = false;
                });
            });
        
        });
    };

    // fetch request for the reactivateButtonProject
    const reactivateButtonProjectElements = document.querySelectorAll(".field-button_reactivate button.reactivateButton");
    const bookingButtonRequestElements = document.querySelectorAll(".field-button_book_request button.bookRequestButton");
    const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;

    // functionality for reactivateButtons
    handleButtonClicks(reactivateButtonProjectElements, csrfToken);
    // functionalyt fir book request buttons
    handleButtonClicks(bookingButtonRequestElements, csrfToken);

});
