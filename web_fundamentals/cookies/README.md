What are cookies?

Cookies are small bits of data that are stored in your browser. Each browser will store them separately, so cookies in Chrome won't be available in Firefox. They have a huge number of uses, but the most common are either session management or advertising (tracking cookies). Cookies are normally sent with every HTTP request made to a server.

Why Cookies?

Because HTTP is stateless (Each request is independent and no state is tracked internally), cookies are used to keep track of this. They allow sites to keep track of data like what items you have in your shopping cart, who you are, what you've done on the website and more.

Cookies can be broken down into several parts. Cookies have a name, a value, an expiry date and a path. The name identifies the cookie, the value is where data is stored, the expiry date is when the browser will get rid of the cookie automatically and the path determines what requests the cookie will be sent with. Cookies are normally only sent with requests to the site that set them (Weird things happen with advertising/tracking).

The server is normally what sets cookies, and these come in the response headers ("Set-Cookie"). Alternatively, these can be set from JavaScript inside your browser.

Using cookies

When you log in to a web application, normally you are given a Session Token. This allows the web server to identify your requests from someone else's. Stealing someone else's session token can often allow you to impersonate them.

Manipulating cookies

Using your browser's developer tools, you can view and modify cookies. In Firefox, you can open the dev tools with F12. In the Storage tab, you can see cookies that the website has set. There's also a "+" button to allow you to create your own cookies which will come in handy in a minute. You can modify all cookies that you can see in this panel, as well as adding more.

Alternatives - useful to know

Slowly, for some uses, LocalStorage and SessionStorage are used instead. This has a similar functionality but isn't sent with HTTP requests by default. These are HTML5 features.

More on cookies

https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies

Read and try and understand this information. Check out the link for extra information

