# Video and Audio content in HTML

## Video content in HTML
```HTML
<!-- <video> element contains the video content in a HTML document.
    Important attributes associated with <video> element are  
    src = absolute/relative video url 
    controls = when specified, adds start,stop, volume controls
    autoplay = boolean attribute automatically starts playing the video.Not recommended to be set as default
    loop = boolean attribute. start the video again on completion. Not recommended to be set as default
    poster = image url that appears as the video poster. Displayed till the video is played
    muted = boolean attribute. mutes the video.
    preload = "metadata, auto, none" are accepted values. auto downloads the content, metadata downloads only the video metadata.
    width and height attributes can be specified. Video always tries to maintain its aspect ratio and correspondingly expands horizontally incase width and height attributes are specified.-->
<video src="https://github.com/mdn/learning-area/blob/master/html/multimedia-and-embedding/video-and-audio-content/rabbit320.webm" controls muted>
  <!-- This text gets displayed when the browser is unable to play the video in the source -->
  <p> Rabbit in a video </p>
</video>
```

Different browsers support different video formats. For instance firefox and chrome support webm, while IE and safari support mp4, due to video format patents. For the video to be playable in all browsers, we can specify multiple video formats using the **&lt;source&gt;** element.
```HTML
<video controls muted>
<!-- <source> is an empty HTML element. type attribute is optional, but helps the browser decide faster which video is playable, otherwise browser has to figure out by playing different formats-->
  <source src = "https://github.com/mdn/learning-area/blob/master/html/multimedia-and-embedding/video-and-audio-content/rabbit320.webm" type = "video/webm">
  <source src = "https://github.com/mdn/learning-area/blob/master/html/multimedia-and-embedding/video-and-audio-content/rabbit320.mp4" type = "video/mp4">

  <!-- This text gets displayed when the browser is unable to play the video in the source -->
  <p> Rabbit in a video </p>
</video>
```

## Audio in HTML
```HTML
<!-- <audio> element contains the audio content in a HTML document.
    Important attributes associated with <audio> element are  
    src = absolute/relative video url 
    controls = when specified, adds start,stop, volume controls
    autoplay = boolean attribute automatically starts playing the video.Not recommended to be set as default
    loop = boolean attribute. start the video again on completion. Not recommended to be set as default
    muted = boolean attribute. mutes the video.
    preload = "metadata, auto, none" are accepted values. auto downloads the content, metadata downloads only the video metadata.-->
<audio src="https://github.com/mdn/learning-area/blob/master/html/multimedia-and-embedding/video-and-audio-content/viper.mp3" controls muted>
  <!-- This text gets displayed when the browser is unable to play the audio in the source -->
  <p> Audio </p>
</audio>
```

Similar to **&lt;video&gt;**, this element also supports multiple audio file formats using the **&lt;source&gt;** element.
```HTML
<!-- <audio> element contains the audio content in a HTML document.
    Important attributes associated with <audio> element are  
    src = absolute/relative video url 
    controls = when specified, adds start,stop, volume controls
    autoplay = boolean attribute automatically starts playing the video.Not recommended to be set as default
    loop = boolean attribute. start the video again on completion. Not recommended to be set as default
    muted = boolean attribute. mutes the video.
    preload = "metadata, auto, none" are accepted values. auto downloads the content, metadata downloads only the video metadata.-->
<audio controls muted>
  <source src="https://github.com/mdn/learning-area/blob/master/html/multimedia-and-embedding/video-and-audio-content/viper.mp3" type = "audio/mp3" >
  <source src="https://github.com/mdn/learning-area/blob/master/html/multimedia-and-embedding/video-and-audio-content/viper.ogg" type = "audio/ogg" >

  <!-- This text gets displayed when the browser is unable to play the audio in the source -->
  <p> Audio </p>
</audio>
```

## Video tracks
**&lt;track&gt;** element can contain teh track of the video. This element has mainly **src**, **kind** and **srclang** attributes. **kind** attribute can have the following values **subtitles, captions and descriptions**. **src** contains the url to VTT transcript file which follows WebVTT format. **srclang** contains the track transcript language.
```HTML
<video controls muted>
<!-- <source> is an empty HTML element. type attribute is optional, but helps the browser decide faster which video is playable, otherwise browser has to figure out by playing different formats-->
  <source src = "example.webm" type = "video/webm">
  <source src = "example.mp4" type = "video/mp4">
  <track kind="subtitles" src="subtitles_en.vtt" srclang="en">

  <!-- This text gets displayed when the browser is unable to play the video in the source -->
  <p> Rabbit in a video </p>
</video>
```

## References:
* [Video and Audio in HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Video_and_audio_content)
