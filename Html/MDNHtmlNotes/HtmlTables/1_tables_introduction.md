# HTML Table Basics

HTML tables- used for representing tabular data. **Donot use** tables for web page layouts.

**NOTE**: A table cell contains the data and can span over multiple rows or columns.

## HTML table
Table is enclosed within **&lt;table&gt;** tag. **&lt;td&gt;** represents a table cell containing **table data**. **&lt;tr&gt;** for **table row**.

```HTML
<table>
  <tr>
    <th>Planet</th>
    <th>Position from Sun</th>
  </tr>
  <tr>
    <td>Mercury</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Venus</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Earth</td>
    <td>3</td>
  </tr>
</table>
```

## Table headers
**&lt;th&gt;** element for defining **table headers**. **scope** attribute associates row or column with the data they span. This attribute makes the table more **accessible**.

```HTML
<!-- "th" can be placed alongside "td" and headers can be part of rows or columns -->
<table>
  <tr>
    <td></td>
    <th scope="col">Mercury</th>
    <th scope="col">Venus</th>
    <th scope="col">Earth</th>
  </tr>
  <tr>
    <th scope="row">Position From Sun</th>
    <td>1</td>
    <td>2</td>
    <td>3</td>
  </tr>
  <tr>
    <th scope="row">Distance From Sun(in AU)</th>
    <td>0.39</td>
    <td>0.723</td>
    <td>1</td>
  </tr>
</table>
```

## Table cells to span multiple rows and columns
**colspan** and **rowspan** attributes help define how many columns and rows should a table cell occupy. These attributes can be applied to **th** and **td** elements.

```HTML
<table>
  <tr>
    <th colspan="2">Animals</th>
  </tr>
  <tr>
    <th colspan="2">Hippopotamus</th>
  </tr>
  <tr>
    <th rowspan="2">Horse</th>
    <td>Mare</td>
  </tr>
  <tr>
    <td>Stallion</td>
  </tr>
  <tr>
    <th colspan="2">Crocodile</th>
  </tr>
  <tr>
    <th rowspan="2">Chicken</th>
    <td>Hen</td>
  </tr>
  <tr>
    <td>Rooster</td>
  </tr>
</table>
```

## Common styling to columns
**&lt;col&gt;** and **&lt;colgroup&gt;** elements. Helps reuse styling. **&lt;colgroup&gt;** consists of **&lt;col&gt;** elements, where each **&lt;col&gt;** represents a column(not a cell) in the table. 

**&lt;col&gt;** element also contains **span** attribute that contains the consecutive columns this element spans.

**NOTE**: Styling applied to **&lt;col&gt;** elements is applied to all columns as mentioned with the **span** attribute. Default value for span is 1, which makes **&lt;col&gt;** element represent a single table column(not table cell) by default.

```HTML
<style>
  .yellow-bg {
    background-color: yellow;
  }
</style>

<table>
  <colgroup>
    <!--Empty element i needed for those cells that dont require any stying.  -->
    <col>
    <!-- This makes columns 2 and 3 in the table have yellow background color  -->
    <col span="2" class="yellow-bg">
  </colgroup>
  <tr>
    <th>Data 1</th>
    <th>Data 2</th>
    <th>Data 3</th>
  </tr>
  <tr>
    <td>Calcutta</td>
    <td>Orange</td>
    <td>City</td>
  </tr>
  <tr>
    <td>Robots</td>
    <td colspan="2">Jazz</td>
  </tr>
</table>
```

## References:
* [HTML table basics](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Basics)