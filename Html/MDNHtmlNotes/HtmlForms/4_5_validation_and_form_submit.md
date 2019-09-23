# Form validation and submission

* built-in form validation
* client side javascript validation
* server side validation

## Builtin form validation

* required attribute
* pattern attribute - accepts **regex** as its value.
* minlength, maxlegth attributes with `<input>`(type=text) and `<textarea>`
* min, max attributes


## Javascript validation libraries
* [validate.js](http://rickharrison.github.com/validate.js/)
* [jquery validation plug in ](http://bassistance.de/jquery-plugins/jquery-plugin-validation/)

## Sending the form

* form submit button click
* send using `XMLHttpRequest` when form's button clicked.

## [Sending form with files](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Sending_and_retrieving_form_data#A_special_case_sending_files)
Form should have the **enctype** attribute with value **multipart/form-data**, if the form contains any input widget of type **file**

---

## References
*  Form Submission
*  [Form Validation](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Form_validation)