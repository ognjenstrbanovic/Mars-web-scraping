# web-scraping-Mars-challenge

![Mission to Mars Image](https://github.com/RutgersCodingBootcamp/RU-JER-DATA-PT-01-2020/raw/master/02-Homework/12-Web-Scraping-and-Document-Databases/Instructions/Images/mission_to_mars.png)  


Assignment (a challenging one for me, as I think I was still adjusting to the class being held exclusively online because of the COVID-19 pandemic): Create a web application that scrapes various websites for data and displays the information in a single HTML page...  
To do the initial scraping in Step 1, I used Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.  
First, I scraped the NASA Mars News site to collect the latest "News Title" and "Paragraph Text".  
Second, I used "splinter" to navigate the JPL Mars Space Images site and find the full-size image URL for the current featured Mars image.  
Third, visiting the Twitter page for "Mars Weather", I scraped the latest tweet from the page, and saved it to a newly-created variable.  
Fourth, I used Pandas to scrape the table containing facts about Mars - this was found on the "Mars Facts" webpage that was provided to us. Pandas was used to convert the table to HTML format.  
Fifth, and finally for this part of the homework, I went to USGS Astrology website to obtain high-resolution images of each of Mars' hemispheres. Saving both the image URL string and the hemisphere name multiple times, the next step was to append this information to a Python list of dictionaries.  
Now for Step 2... I used MongoDB with Flask templating to, at last, create the new HTML page displaying all of the scraped information.  
One, I created a scrape function that returned one Python dictionary with all of the freshly scraped data, and stored the value in MongoDB.  
And two, a root (/) route was made to query the database and pass the data into the HTML template to display said data.  
That is it, thank you for reading!!!
```
Objectives for Web Scraping and Documenting Databases Unit:
- Create and connect to local MongoDB databases.
- Create, read, update, and delete MongoDB documents using the Mongo Shell.
- Create simple Python applications that connect to and modify MongoDB databases using the PyMongo library.
- Use Beautiful Soup to scrape their own data from the web.
- Save the results of web scraping into MongoDB.
- Become comfortable rendering templates with Flask using data retrieved from a Mongo database.
- Use Beautiful Soup to scrape data.
- Use PyMongo to save data to a Mongo database.
- Use Flask to render templates.
```
