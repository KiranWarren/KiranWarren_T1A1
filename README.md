# Project - Workbook (Term 1)

### Kiran Warren

## Question 1 - Identify and explain common and important components and concepts of web development markup languages.

Markup is used to annotate text within a document. Markup could be as simple as using a highlighter while researching signify that highlighted sections of the text are important. When the rules used for markup become codified, it then becomes a markup language.

In the context of web development, markup languages may refer to XML (extensible markup language), HTML (hypertext markup language) or XHTML (extended hypertext markup language.) These three languages are based on SGML (standard generalized markup language), which is a language used for defining markup languages.

HTML is now the primary language used for web development, and all modern websites will contain some form of HTML. It was first released back in 1991, and was created by the inventor of the World Wide Web, Tim Berners-Lee. Since then, multiple versions of HTML have been released. The current version is HTML5, which provides the most flexible rules compared to other markup languages. HTML5 also allows any future additions or changes to be added to the language without the need for a new superseding version to be released.

As HTML was developed, the language became too complicated and there was a need for the web page content to be separated from the web page styling. While styling can still be described within the HTML document, the CSS (cascading style sheets) document was created to contain the web page styling.

Documents created in web development markup languages are used to instruct the web browser how the content within the document is displayed or printed. It does this by labelling contents within opening and closing tags. Tags are indicated using angle brackets (< and >) For example:

```HTML
<label>Web page content</label>
```

Labels can be nested within each other to label the content with multiple tags. For example, a section of text that we wanted to communicate to the browser was both paragraph text and bold font weight:

```HTML
<p><b>This text is bold paragraph text!</b><p>
```

HTML allows some flexibility with how tags are used. For example, in the bold paragraph text, even though the bold tag is nested within the paragraph tag, we are still able to close the paragraph tag first without confusing the web browser. This kind of flexibility is not allowed in more stricter markup languages:

```HTML
<p><b>This text is bold paragraph text!</p><b>
```

HTML documents have a basic structure consisting of 4 main elements:

- Document type declaraction - This is the first line of code of a html document, and declares what type of document it is.
- html tag - This tag contains all of the document contents (except for the doctype declaration), and communicates to the web browser that all information contained within the open and close tag is HTML-coded content.
- head tag - This tag contains meta information that is not viewable on the web page itself but can give the browser more information about the document.
- body tag - This tag contains all of the visible content of the webpage.

An example of the HTML document structure is as follows:

```
<!DOCTYPE HTML>
<html>
    <head>
        <title>Example Document</title>
    </head>

    <body>
        <h1>A Heading</h1>
        <p>Some paragraph text</p>
    </body>
</html>

```

In the example above, indentations are used to help the coder or whoever may be viewing the HTML code, to visually see the heirachy of the HTML tags. The html tag is the overarching label for the document, so all of the elements nested within it are indented. Similarly, the title is an element nested within the head, and therefore is indented to show this. The indentations are purely for the readability of the document, and does not affect how the web browser interprets the information.

As previously described, the head element contains meta information that is not viewed on the web page. Some of the elements that may be nested within the head tag include:

- title - The document title is a required element that must be present for the web page to be displayed correctly. It will be seen in the web browser tab and in search engine results.
- link - The link tag is used to reference an external document or asset. A common usage is to link a CSS document to the HTML document, so that the style described within the CSS document is applied to the web page. The link tag may also reference an image to be used as the favicon (displayed next to the document title in the web browser tab) or reference a font family that will be used in the webpage.
- meta - The meta tag is used to contain any metadata for the webpage. This may include webpage author, search engine keywords, a decsription of the document, the viewport to be used, etc. The viewport is an important piece of metadata to include, as this will assist the web browser in displaying the web page appropriately on different devices (e.g. PC, tablet, mobile phone).

After the head section will be the body section, which contains all of the content that is displayed on the webpage. As this is the content that the user will be viewing and interacting with, it will be the majority of the HTML code in most cases. Some of the common body elements used include:

- Text Elements
  - headings - Headings within the content are marked up with heading tags, h1 - h6, with h1 being the largest heading by default and h6 the smallest.
  - paragraphs - Paragraphs are marked up with p tags.
  - quotes - Quoted pieces of text can be tagged with q tags.
- Images - Images are linked in the document by using the img tag. An img tag will include a source attribute (src) that will contain the URL and an alternate text attribute (alt) that will be displayed if the image cannot be retrieved. Image tags do not have closing tags.
- Hyperlinks - Links or anchor tags (a) are used to transform a piece of content into a clickable hyperlink that will navigate the web browser to the designated location when pressed. The a tag will have a hyperlink reference attribute (href) that gives the URL of the hyperlink.
- Lists - HTML allows ordered and unordered lists with the ol and ul tags. Individual list items are nested within the ol/ul tags by using li tags.
- Forms - HTML forms are a way for the user to input information into the webpage that can then be collected. There are two main types of form elements:

  - input - An input element is the piece of content that the user interacts with in various ways depending on the input type attribute that is designated. These may include text fields, radio buttons, checkboxes, submit form buttons, etc.
  - label - The label tag will be associated to a specific input element or elements within a form. The label tag gives meaning to what the related input tag requires or describes. The for attribute of the label tag should be equal to the id attribute of the element or elements that it is describing.

When configuring how the HTML is to be displayed, the use of the style attribute is employed. Styling has a vast number of properties that change the way any element within the body is displayed. Some properties include its color, size, shape, how and where its placed on the page, animations, etc. An example of how it is employed within the HTML document is shown below:

```html
<p>This paragraph text is the default colour of black.</p>
<p style="color:red;">This paragraph text has been styled as red.</p>
```

Depending on the complexity of the page, the styling may be the majority of the webpage coding. This brought about the need for the styling to be separated from the HTML document. A separate type of document is created (CSS), which is then linked in the HTML document header.

With most of the styling removed from the HTML document, there may come a need to apply different styling properties to the same HTML tag types. Like the example above, maybe one paragraph element needs to have red text, while all the others remain default. To give greater granularity to the application of markup in the HTML document, the use of IDs and classes can be used.

- id - One element on a webpage may be given a unique id property. This allows for the styling of that id to override any overlapping styling given to that element tag. The id tag can also be used as a bookmark on a webpage. For example, a webpage may have a contents list near the top of the content to outline was is contained on the page. Each section listed in the contents can be given a unique id. We can then use anchors tags in the contents list to navigate to any of the sections by adding the #id to the end of the hyperlink reference.
- class - Multiple elements on a webpage may be given a class property. This makes it much easier to apply the desired styling properties to all of the specific HTML elements that require it.

HTML has some semantic elements that give greater meaning to what is contained within the tags. An exmaple of a semantic element would be the nav tag. A section of the webpage containing a list of navigation links can be contained within the nav tags to describe to the web browser and other developers what the purpose of that element is. A non-semantic alternative would be to have the list of navigation links within a span element, which does not describe the purpose of that particular section.

### References

- 1
- 2

## Question 2 - Define the features of the following technologies that are essential in terms of the development of the internet:

## - Packets

All data transmitted over the internet is broken up into smaller pieces called "packets". The internet is a "packet-switched" network, meaning it is designed for the transmission of packets across multiple routes from the source to the destination.

Paul Baran and Donald Davies are attributed with inventing the concept of packet switching networks in the 1960s. Paul Baran first created the concept while researching survivable network communications systems for the US Airforce. A survivable network needed to maintain end-to-end communications between two devices after destruction of network equipment within the network. Davies later arrived at the same concept a few years later, independently of Baran. The term "packet switching" was taken from Davies work, as it was more intuitive than Baran's term for the same concept, "distributed adaptive message block switching."

As an example, an email may be sent from one device to a receiving device. The email will be broken up into fixed-size chunks of data, i.e. packets, by the sending device. The packets are then sent across the internet to the destination using the best available route. The receiving device is then responsible for interpreting the packets and reforming them back into the original email. Each packet will contain the following, as dictated by the IP (internet protocol):

- Header - Information about the packet, including the source address and the destination address.
- Payload - The chunk of data that is being transmitted.
- Trailer - Similar to the header, the trailer also contains information about the packet. However, trailers are only used by some network types.

The use of packets means that there does not need to be a dedicated line of transmission between a source and a destination. The packets will take the best available route across the network to reach their destination. A single router/switch within the network is able to process packets from different devices independently of each other. In contrast, if packets were not used, then only one device could use a path to the destination at a time until the whole piece of data was transmitted, and all other computers on the network would have to wait their turn. This is beyond impractical for a network on the scale of the internet.

### References -

- d
- d

## - IP addresses (IPv4 and IPv6)

The IP (internet protocol) address is a unique identifier given to a device that is connected to the internet or a local network. The device is also called a host, which could be a computer, printer, etc. Data packets sent across the network will be given a destination address in the form of an IP address, which tells network equipment the location of the destination device. IP addresses form the basis of the internet, and allow two devices across different networks to communicate with each other.

An IPv4 address is represented by four 8-bit (0 - 255) numbers, separated by periods (example: 127.0.0.1). The first three numbers of the IP address are the network ID and the last number is the host ID. The 32-bit IPv4 address offers a total of approximately 4.3 billion unique addresses (2<sup>32</sup>). This amount likely seemed sufficient when the IPv4 address was first launched in 1983, however, the ubiquity of the internet and the sheer number of devices that are now connected presents a real possibility of running out of addresses.

An IPv6 address is represented by eight hexadecimal (a - f, 0 - 9) 16-bit alphanumerics, separated by colons (example: 4000:0000:0000:0000:1be5:3020:a00e:2001). This address format provides an astronomical 340 undecillion unique addresses (2<sup>128</sup> or 3.4 x 10<sup>38</sup>). IPv6 also provides some additional technical differences to IPv4, including larger packet headers than IPv4 addresses (approximately double the size) and the elimination of NAT (network address translation).

### References

- d
- d

## - Routers and routing

Routers are a network device that are responsible for receiving packets from a device and forwarding it towards the destination device using the most efficient path. The router is the traffic controller for packets, directing them where to go to avoid congestion. Routers connect networks together, forwarding data packets between them. Communication of two devices on different networks across the internet is managed by a series of routers.

Routing is performed by the router by reading the header information of a data packet to see where the destination device is. The router will consult its routing table to determine the most efficient pathway for the packet to take to reach its destination. Information within the routers routing table can be manually configured or learning by dynamic routing protocols. Congestion can occur over the network intermittently at different locations, so it is the routers job to balance the load across various connections to ensure efficient delivery of data.

### References

-d
-d

## - Domains and DNS

Computer networks use IP addresses to send data packets from one device to the other. While this is perfectly fine for computers to communication, it becomes hard for humans to interpret and remember specific addresses. Domain names provide a readable and meaningful address for websites that are much easier for people to use.

A domain name can contain several strings, separated by periods. Each string can denote information about that domain. For example:

> https://coderacademy.edu.au

This is the homepage for Coder Academy's website, which is clearly evident by reading the domain name. The last string "au" is called the top-level domain and is assigned to the domain name by the domain name authority in Australia. The "edu" string is called the second level domain in this instance, and refers to schools and educational institutions.

When a domain name is entered into a web browser, the web browser will need to then resolve the domain name into an IP address that can be used by networking devices. It does this through the use of the DNS (domain name system). The web browser will send off a request to a DNS server, requesting the IP address for the domain name that was entered. If the domain name could not be matched in the server, the request will be forwarded onto another DNS server to be resolved. If the domain name cannot be found, the web browser will return an error (example: ERR_NAME_NOT_RESOLVED).

### References

- d

## Questions 3 - Define the features of the following technologies that are essential in terms of the development of the internet:

## - TCP

TCP stands for transmission control protocol, and is a transport protocol that works in conjunction with the internet protocol to ensure that data packets are received without error and in the correct order. The IP ensures that each packet of a given piece of data arrives at the required destination, and the TCP ensures that those packets are assembled into the right order and have not been corrupted. The TCP information (TCP header) is contained within the payload of the packet.

While IP is a connectionless protocol only concerned with each packet being routed to the destination, TCP maintains a connection between a client and a server for the transmission of the data. Reusing the email example, an email is sent from a client computer to a receiving server:

- The source device will send an initial request (SYN or synchronisation) packet to the server.
- Upon receiving the request, the server will send back a packet to agree to the process (SYN/ACK or synchronisation/acknowledgement).
- Upon receiving the SYN/ACK packet, the source device will then send back another packet to confirm the process (ACK or acknowledgement).
- The email is then broken up into packets and sent over the network. Each packet requiring an ACK from the server to confirm that the packet was received and without error. A packet may be re-sent if no ACK was received or if the checksum within the TCP header received by the server notified that the packet payload was corrupted.
- The server will reassemble the packets back into the original email using the TCP implementation.

### References

- f

## - HTTP and HTTPS

HTTP, or hypertext transfer protocol, is an application layer protocol designed for the transmission of data between web browsers and servers. It is a client-server protocol, with the client sending requests to the server, and the server sending back responses.

When a webpage is requested by a user, the web browser will translate this into HTTP requests and send these to the corresponding web server(s).

## - Web browsers (requests, rendering and developer tools)

response
