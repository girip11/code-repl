# Native form widgets

## Common attributes

| Attribute | default value | description                                               |
| --------- | ------------- | --------------------------------------------------------- |
| autofocus | false         | only one form element can have this attribute set to true |
| disabled  | false         | disables user action on widget                            |
| form      |               | id of the form to which the widget is associated with     |
| name      |               | fieldname  that will be sent when the form is submitted   |
| value     |               | field value                                               |

## Text input fields
`<input>` element. Common attributes
* readonly
* disabled
* placeholder
* size
* length
* spellcheck

### Single line text fields
```HTML
<input type="text" id="mail_subject" name="subject" placeholder="email subject">
```

### Email field
```HTML
<input type="email" id="email" name="email" placeholder="user@example.com">
```
With **multiple** attribute, the field can accept many email addresses separated by commas.

### Password field
Entered text will be visible as dots.
```HTML
<input type="password" id="password" name="user_pwd">
```

### Search field
values entered saved for autocomplete later. styled differently compared to a normal text field.
```HTML
<input type="search" id="search" name="search" placeholder="Type here">
```

### Phoen number field
No special validation provided.
```HTML
<input type="tel" id="tel" name="tel" placeholder="Enter mobile number here">
```

### URL field
URL validation provided.
```HTML
<input type="url" id="url" name="url" placeholder="Enter URL here">
```

## Multiline text fields
`<textarea>` - accepts only plain text content and renders as plain text content.

Commonly used attributes
* rows - number of visible lines
* cols - default is 20
* wrap - default is **soft**. 

## Dropdown content

### Select box

```HTML
<label for="selection">selection label</label>
<select id="selection" name="selection" multiple>
<!--  if value attribute is set for an option, that value will be sent on form submission, else the content of the option element -->
  <option value="option1" selected>Option1<option>
  <option value="option2">Option2 <option>
  <option>Option3<option>
  <option>Option4<option>
</select>

<!-- grouping related options -->
<select id="selection" name="selection">
  <optgroup label="Group1">
    <option selected>Option1<option>
    <option>Option2 <option>
  </optgroup>
  <optgroup label="Group2">
    <option>Option3<option>
    <option>Option4<option>
  </optgroup>
</select>
```

### Autocomplete box
**Note**: According to the HTML specification, the list attribute and the `<datalist>` element can be used with any kind of widget requiring a user input.

```HTML
<label for="myFruit">What's your favorite fruit?</label>
<input type="text" name="myFruit" id="myFruit" list="mySuggestion">
<datalist id="mySuggestion">
  <option>Apple</option>
  <option>Banana</option>
  <option>Blackberry</option>
  <option>Blueberry</option>
  <option>Lemon</option>
  <option>Lychee</option>
  <option>Peach</option>
  <option>Pear</option>
</datalist>
```

## Checkable items
checkbox and radiobutton. Both have **checked** attributes associated with them. Values are sent only when they are checked. Value for these widgets provided using the **value** attribute.

### Checkbox
Multiple checkboxes can be in checked state.
[Associated checkboxes grouped](http://html.cita.illinois.edu/nav/form/checkbox/index.php?example=6) under `<fieldset>`

```HTML
<input type="checkbox" checked id="remember_selection" name="remember_selection" value="remember">

<!-- Pizza toppings selection -->
<fieldset class="group">
  <legend>Select standard pizza toppings</legend>
  <ul class="checkbox">
    <li><input type="checkbox" id="cb1" value="pepperoni" checked /><label for="cb1">Pepperoni</label></li>
    <li><input type="checkbox" id="cb2" value="sausage" /><label for="cb2">Sausage</label></li>
    <li><input type="checkbox" id="cb3" value="mushrooms" /><label for="cb3">Mushrooms</label></li>
    <li><input type="checkbox" id="cb4" value="onions" /><label for="cb4">Onions</label></li>
    <li><input type="checkbox" id="cb5" value="gpeppers" /><label for="cb5">Green Peppers</label></li>
    <li><input type="checkbox" id="cb6" value="xcheese" checked /><label for="cb6>">Extra Cheese</label></li>
  </ul>
</fieldset>
```

### Radio button
Only one radio button in a group can be in checked state at any point in time.

```HTML
<fieldset>
  <legend>Who has won the most grandslams in tennis as of 2019?</legend>
  <div>
    <input type="radio" id="rb1" name="answer" value="Rafael Nadal">
    <label for="rb1">Rafael Nadal</label>
  </div>
  <div>
    <input type="radio"  id="rb2" name="answer" value="Roger Federer">
    <label for="rb2">Roger Federer</label>
  </div>
  <div>
    <input type="radio"  id="rb3" name="answer" value="Novak Djokovic">
    <label for="rb3">Novak Djokovic</label>
  </div>
</fieldset>
```

## Buttons

```HTML
<!-- type=submit -->
<!-- sends the from data to server -->
<button type="submit"> <img src="" alt="Submit Image"> Submit</button>
<!-- below is also same -->
<input type="submit" value="Submit">

<!-- type=reset -->
<!-- resets the form widgets to default values -->
<button type="reset">Reset</button>
<!-- below is also same -->
<input type="reset" value="Reset">

<!-- type=button -->
<button type="button" onclick="validate()">Validate</button>
<!-- below is also same -->
<input type="button" onclick="validate()" value="Validate">
```

## Advanced form widgets

### Numbers
Allows only floating point numbers.

```HTML
<input type="number" id="available" name="available" value="50" min="1" max="100" step="1">
```

### Sliders for range
Another way to pick a number.
```HTML
<label for="volume">Adjust Volume</label>
<input type="range" id="volume" name="volume" value="50" min="1" max="100" step="1">
```

### Datetime picker
Time format used i as per [valid date time format in HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Date_and_time_formats)
```HTML
<!-- type = time -->
<!-- A control for entering a time value (hours,minutes and optionally seconds) with no time zone -->
<input type="time" id="time" name="time" min=02:10:00" max="20:45:00" value="16:30:00">

<!-- type = week -->
<!-- A control for entering a date consisting of a week-year number and a week number with no time zone. Format: YYYY-W[WeekNumber from 1 - 52]-->
<input type="week" id="week" name="week" min="2018-W1" max="2018-W52" value="2018-W20">

<!-- type = month -->
<!-- A control for entering a month and year, with no time zone. format: yyyy-mm-->
<input type="month" id="month" name="month" min="2011-01" max="2019-12" value="2015-10" >

<!-- type = date-->
<!-- A control for entering a date (year, month, and day, with no time).(dd/mm/yyyy format) -->
<input type="date" id="date" name="date" min="2013-06-01" max="2018-08-31" value="2019-02-10">

<!-- time = datetime-local -->
<!-- A control for entering a date and time, with no time zone. -->
<input type="datetime-local" id="meeting-time"
       name="meeting-time" value="2018-06-12T19:30"
       min="2018-06-07T00:00" max="2018-06-14T00:00">
```

### Color picker

```HTML
<!-- value provided in six digit hexcode -->
<input type="color" id="color-picker" name="color" value="#ffffff">
```

### File picker
Important attributes are
* accept - filter of file extensions of accepted files
* multiple - boolean attribute to allow multiple files upload.

```HTML
<input type="file" id="profile_picture" name="profile_picture" accept="image/*">

<!-- accept only png and jpeg -->
<input type="file" id="images" name="iamges" accept="image/png, image/jpeg" multiple>
```

### Hidden
Invisible form widget. **name** and **value** attributes should be set. Field will be sent to server when form is submitted.

```HTML
<!-- some information internal to server -->
<input type="hidden" id="answer-type" name="answer-type"  value="text">
```

### Image Button
Displayed like `<img>` element but behaves like a **submit button**. When submitted, (x,y) coordinates of the click on the image(coordinates relative to image) are sent as two key value pairs.

```HTML
<input type="image" src="http://lorempixel.com/100/50/" alt="Random image"  width="100" height="50" name="pos" id="click-pos">
<!-- server receives the value as pos.x=78, pos.y=45 -->
```

## Progress bar

```HTML
<!-- content inside progress element is for assistive technologies to read it -->
<progress max="100" value="50">50/100</progress>
```

## Meter
Meter bar - represents fixed value in a range(min, max)

* **low** and **high** attribute values divide the range in to 3 parts
* min-low  - lower part of the range
* low-high - medium part of the range
* high-max - higher part of the range

**value** attribute contains the current value.
**optimum** attribute contains optimum value for the `<meter>` element.

* preferred part - part containing optimum value. colored green
* average part - colored yellow
* worst part - colored red

Whichever part out of the 3 parts contains the optimum value is considered as the preferred part.

```HTML
<meter min="0" max="100" value="75" low="33" high="66" optimum="50">75</meter>
```

---
## References:
* [Native form widgets](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/The_native_form_widgets)