# Images in HTML

## **`<img>`** element
```HTML
<!-- <img> element is an empty HTML element. contains images in the HTML document -->
<!-- <img> element is associated with the below attributes primarily -->
<!-- src = absolute/relative url to the image
     alt = text that describes the image. used by screen readers and in cases where image fails to load.
     title = image title that browsers can display when hovered over the image
     width = width of the image container
     height = height of the image container 
Based on the width and height, the image will be resized to fit in to the new container size.
By default <img> tag takes the size of the image it is pointing to.-->
<img src="http://lorempixel.com/150/200/" alt="Pokemon image with Pikachu" title="Pokemon">

<img src="http://lorempixel.com/150/200/" alt="Pokemon image with Pikachu" title="Pokemon" width="300" height="500">
```

## Captioning images
**&lt;figure&gt;** element along with **&lt;figcaption&gt;** can provide captions to the image. **&lt;figure&gt;** can contain many images, audio, video, code (enclosed in **&lt;pre&gt;**), equations, tables.
```HTML
<figure>
  <img src = "http://lorempixel.com/150/200/" alt = "T-Rex skeleton" >
  <img src = "http://lorempixel.com/150/200/" alt = "T-Rex skeleton" width = "500" height = "500" >
  <figcaption>T-Rex dinosaurs</figcaption>
 </figure>
```

* Images can be set as the background of html elements using the CSS property `background-image`.
```CSS
div {
  background-image: url('http://lorempixel.com/150/200/');
}
```

## References:
* [Images in HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)