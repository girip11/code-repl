# Global Attributes in Html
Global attributes as defined in the mozilla developers site.
> Global attributes are attributes common to all HTML elements; they can be used on all elements, though they may have no effect on some elements.

## Useful html global attributes 
Below is the list of attrubutes that we endup using frequently. Exhaustive list is in the **references section**.

* [class attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class) - Html elements can have multiple class attributes which can be used in CSS for styling the element.
    ```HTML
    <!--Assume other standard html elements are present to make this a valid html document.-->
    <!-- Styling based on class attribute -->
    <style>
        .class1 {
            font-style: italic;
            font-weight: bold;
        }
        .class2 {
          width: 100%;
          height: 100%;
        }
    </style>

    <div class = "class1 class2">
    ```

* [contenteditable attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/contenteditable) - enumerated attribute which makes specifynig a value mandatory.can make the element editable. Values are true or empty string to make it editable otherwise false to disallow editing.
    ```HTML
    <blockquote contenteditable="true">
        <p>Edit this content to add your own quote</p>
    </blockquote>

    <cite contenteditable="true">-- Write your own name here</cite>
    ```

* [data-* attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/data-*) - Used for defining custom atrributes that ca store applicaiton specific data. All custom attributes have the prefix **data-**. We can access these attributes in JS using **HTMLElement.dataset**.
    ```HTML
    <div data-id = "custom_id" data-env="APPLICATION ENVIRONMENT">
        <p> This is a paragraph.</p>
    </div>
    ```

* [draggable attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/draggable) - enumerated attribute with true or false as accepted values. Default value is **auto**.Indicates whether an element can be dragged or not.

* [hidden attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/hidden) - boolean attribute. Can show or hide html elements.
    ```HTML
        <p hidden>This content is not relevant to this page right now, so should not be seen. Nothing to see here. Nada.</p>
    ```

* [id attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id) - Defines a unique identifier (ID) which must be unique in the whole document. This attribute can be used in javascript to fetch the HTML element. 

* [style attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/style) - use it to apply styling to the html element. Use this **only** for testing purposes. Good practice is to always have CSS styles put in a separate file so that it can be reused across many HTML pages and many elements within same page and also allows the developer to make changes at few places. 
    ```HTML
    <div style="background: #ffe7e8; border: 2px solid #e66465;">
    <p style="margin: 15px; line-height: 1.5; text-align: center;">
        Well, I am the slime from your video<br>
        Oozin' along on your livin' room floor.</p>
    </div>
    ```

* [title attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title) - Contains a text representing advisory information related to the element it belongs to. Such information can typically, but not necessarily, be presented to the user as a **tooltip**.

## References:
* [Html Global Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes)
