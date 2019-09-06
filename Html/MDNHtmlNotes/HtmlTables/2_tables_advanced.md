# HTML Table Advanced Features

## Table caption
**&lt;caption&gt;** element - caption to the table describing its contents. Caption element is both visible and accessible.

## Structuring table contents
**&lt;thead&gt;**, **&lt;tbody&gt;** and **&lt;tfoot&gt;** - elements for marking up header, body and footer of the table respectively. Useful in styling and layout.

```HTML
<style>
html {
  font-family: sans-serif;
}

table {
  border-collapse: collapse;
  border: 2px solid rgb(200,200,200);
  letter-spacing: 1px;
  font-size: 0.8rem;
}

td, th {
  border: 1px solid rgb(190,190,190);
  padding: 10px 20px;
}

th {
  background-color: rgb(235,235,235);
}

td {
  text-align: center;
}

tr:nth-child(even) td {
  background-color: rgb(250,250,250);
}

tr:nth-child(odd) td {
  background-color: rgb(245,245,245);
}

caption {
  padding: 10px;
}
.highlight {
  border: 2px solid black;
}
</style>
<!-- table complete example -->
<table>
  <caption>Data about the planets of our solar system</caption>
  <colgroup>
    <col span="2">
    <col class="highlight">       
  </colgroup>  
  <thead>
    <tr>
      <td colspan="2">&nbsp;</td>
      <th scope="col">Name</th>
      <th scope="col">Mass(10<sup>24</sup>kg)</th>
      <th scope="col">Diameter(km)</th>
      <th scope="col">Density(kg/m<sup>2</sup>)</th>
      <th scope="col">Gravity</th>
      <th scope="col">Length of day</th>
      <th scope="col">Distance from Sun</th>
      <th scope="col">Mean temperature</th>
      <th scope="col">Number of moons</th>
      <th scope="col">Notes</th>
    </tr>    
  </thead>
  <tbody>
    <tr>
      <th colspan="2" rowspan="4" scope="rowgroup">Terrestial Planets</th>
      <th scope="row">Mercury</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
        <tr>
      <th scope="row">Venus</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
        <tr>
      <th scope="row">Earth</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
        <tr>
      <th scope="row">Mars</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
        <tr>
      <th rowspan="4" scope="rowgroup">Jovian</th>
 <th rowspan="2" scope="rowgroup">Gas giants</th>
      <th scope="row">Jupiter</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
        <tr>
      <th scope="row">Saturn</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
        <tr>
 <th rowspan="2" scope="rowgroup">Ice giants</th>
      <th scope="row">Uranus</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
        <tr>
      <th scope="row">Neptune</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
        <tr>
      <th colspan="2" scope="rowgroup">Dwarf Planets</th>
      <th scope="row">Pluto</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
```

## Nesting tables
Achieved by placing complete structure inside another **&lt;table&gt;** element. Not recommended practice, but possible.

## Tables for visually impaired users
* using scope attribute in row and column headers.
 
* Assign every **th** element an **id** attribute and then associate those **id** attribute values in the **headers** attribute on each **td** element. **This approach is more verbose.**

## References:
* [HTML Table Advanced Features](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Advanced)