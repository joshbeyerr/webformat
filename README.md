# webformat
Allows you to easily format, edit and work with headers and cookies when using the request library in python

Where I most frequently use this code is when webscraping and trying to work around with headers to see what is required to send a request.
To work with headers using this library, create a text file and copy and paste the headers from your request in devtools into the text file. Next create a CookieWork object, and call get_headers(file) passing through the name of the text file. The response will be a formatted dict of all headers that you can now send through with your request 
