# HTML forms

## `<form>` element

```HTML
<form action="/formdata_handler" method="post">
<!-- form body -->
</form>
```

## `<label>` element
* `<label>` element has **for** attribute. The value of this attribute should match the **id** attribute of the corresponding form widget.

## `<input>` element
Important attributes are

* type - type of the `<input>` element 
* id - id of the `<input>` element
* name - this field is passed as the field name to the server when the form is submitted.
* value - holds value of the field. 
* placeholder - holds user tip

There are other attributes that may be relevant to specific types of `<input>` element.

## `<textarea>` element
Holds multiline text. **id** and **name** attributes are provided often. This is not an empty element like `<input>`. Default value goes inside the `<textarea>` element.

Important attributes associated with this element are
* **disabled** - User cannot access/control this element. The content is also not submitted during form submission.
* **rows** - number of visible lines
* **cols** - visible width
* **minlength** - minimum text content size
* **maxlength** - maximum text content size.
* **required** - content cannot be empty
* **wrap** - wraps the text content
* **placeholder** - hint to the user
* **readonly** - content cannot be modified. Content is submitted

## `<button> element`
**type** attribute is the most important one.
 Possible values for the attribute are

 * **submit** - submits the form.
 * **reset** - resets the fields to default value
 * **button** - does nothing. just a button

## `<input type="submit"` vs `<button type="submit">`
Both the elements produce a button that submits the form on clicking. `<input>` allows only plain text as its label, while `<button>` element allows any HTML content.

## Example form
```HTML
<form action="/my-handling-form-page" method="post">
  <div>
    <label for="name">Name:</label>
    <input type="text" id="name" name="user_name">
  </div>
  <div>
    <label for="mail">E-mail:</label>
    <input type="email" id="mail" name="user_mail">
  </div>
  <div>
    <label for="msg">Message:</label>
    <textarea id="msg" name="user_message"></textarea>
  </div>
</form>
```

---

## References:
* [HTML Forms introduction](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Your_first_HTML_form)