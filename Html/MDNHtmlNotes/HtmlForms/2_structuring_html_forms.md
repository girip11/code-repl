# Structuring HTML forms

Nesting of forms forbidden. Form widgets can be placed outside the form. In this case, the `<form>` element should have an **id** attribute and widget can be linked to the form using the **form** attribute pointing to the form's **id** attribute.

```HTML
<form id="sample-form">
</form>
<label form="sample-form" for="user_name"> User Name</label>
<input form="sample-form" id="user_name" name="user_name" placeholder="Enter user name">
```

## `<fieldset>` and `<legend>`
Form elements with same purpose are grouped inside `<fieldset>` elements. Example radio buttons. `<fieldset>` is labelled using `<legend>` element.

```HTML
<form>
  <fieldset>
    <legend>Fruit juice size</legend>
    <p>
      <input type="radio" name="size" id="size_1" value="small">
      <label for="size_1">Small</label>
    </p>
    <p>
      <input type="radio" name="size" id="size_2" value="medium">
      <label for="size_2">Medium</label>
    </p>
    <p>
      <input type="radio" name="size" id="size_3" value="large">
      <label for="size_3">Large</label>
    </p>
  </fieldset>
</form>
```

## Common HTML structures used inside forms

* `<div>` or `<p>` to enclose label and its widget
* `<section>`, `<h1>`, `<h2>` - separate form functionality to logical sections

---

## References:
* [How to structure an HTML form](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/How_to_structure_an_HTML_form)