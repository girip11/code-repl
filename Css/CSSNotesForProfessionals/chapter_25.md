# Styling Tables

## Table layout
`table-layout` property - changes the layout of the table.

* auto - resizes cells based on the content
* fixed - no resizing. follows allocated width. content overflows outside the table

```HTML
<!-- change the table-layout to auto to see how the table resizes -->
<style>
div {
  border: 1px solid black;
}

table {
  margin: 10px;
  width: 150px;
  table-layout: fixed;
  border: 1px solid green;
}
</style>

<body>
  <div>
    <table>
      <thead>
        <tr>
          <th scope="col"> Column1 Heading </th>
          <th scope="col"> Column2 Heading </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>&nbsp;</td>
          <td> in optio aliquam quis </td>
        </tr>
        <tr>
          <td> elit. Laudantium quod </td>
          <td> Lorem ipsum dolor sit amet consectetur</td>
        </tr>
      </tbody>
    </table>
  </div>
</body>
```

## Showing or hiding empty cells
`empty-cells` property
* show - default value
* hide - hides empty cells

This property has effect only when `border-collapse` is set to **separate**

```HTML
<style>
div {
  border: 1px solid black;
}

table {
  margin: 10px;
  border-collapse: separate;
}

table, th, tr {
  border: 1px solid blue;
}
</style>

<div>
  <table>
    <thead>
      <tr>
        <th scope="col"> Column1 Heading </th>
        <th scope="col"> Column2 Heading </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>&nbsp;</td>
        <td>option</td>
      </tr>
      <tr>
        <td></td>
        <td>Lorem</td>
      </tr>
    </tbody>
  </table>
</div>
```

## `border-collapse` property
table borders should be merged with table cell borders.
* separate - default value. Each table cell has its own border
* collapse - borders merged

```HTML
<style>
div {
  border: 1px solid black;
}

table {
  margin: 10px;
  border-collapse: collapse;
}

table, th, tr {
  border: 1px solid blue;
}
</style>

<div>
  <table>
    <thead>
      <tr>
        <th scope="col"> Column1 Heading </th>
        <th scope="col"> Column2 Heading </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>&nbsp;</td>
        <td>optio</td>
      </tr>
      <tr>
        <td></td>
        <td>Lorem</td>
      </tr>
    </tbody>
  </table>
</div>
```

## `border-spacing` property
Determines the spacing between the cells. This property has effect only when the `border-collapse` is set to **separate**.

```HTML
<style>
div {
  border: 1px solid black;
}

table {
  margin: 10px;
  border-collapse: separate;
  border-spacing: 5px;
}

table, th, tr {
  border: 1px solid blue;
}
</style>

<div>
  <table>
    <thead>
      <tr>
        <th scope="col"> Column1 Heading </th>
        <th scope="col"> Column2 Heading </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>&nbsp;</td>
        <td>optio</td>
      </tr>
      <tr>
        <td></td>
        <td>Lorem</td>
      </tr>
    </tbody>
  </table>
</div>
```


## `caption-side` property
Location to display the table caption
* top - default. display caption above the table.
* bottom - displays caption below the table

```HTML
<style>
div {
  border: 1px solid black;
}

table {
  margin: 10px;
  border-collapse: collapse;
  caption-side: bottom;
}

table, th, tr {
  border: 1px solid blue;
}
</style>

<div>
  <table>
    <caption>Example table</caption>
    <thead>
      <tr>
        <th scope="col"> Column1 Heading </th>
        <th scope="col"> Column2 Heading </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>&nbsp;</td>
        <td>optio</td>
      </tr>
      <tr>
        <td></td>
        <td>Lorem</td>
      </tr>
    </tbody>
  </table>
</div>
```


---

## References:
* [CSS notes for professionals](https://books.goalkicker.com/CSSBook/)