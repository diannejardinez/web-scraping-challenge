# Web Scraping - Mission to Mars

**Objectives:**
1. Create webscraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter
2. Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped

**Part 1: Scraping**

- `scrape_planet.py` includes the following below:
    - [NASA Mars News Site](https://mars.nasa.gov/news/) latest news Title, Paragraph Text, and news Date
    - [JPL Mars Space Images](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) featured Image
    - [Mars Weather twitter](https://twitter.com/marswxreport?lang=en) latest Mars weather tweet 
    - [Mars Facts](https://space-facts.com/mars/ ) from the Space Facts table webpage 
    - [Mars Hemispheres](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) high resolution images for each of Mar's hemispheres from the USGS Astrogeology site


**Part 2: MongoDB and Flask Application**
- `app.py` includes the following below:
    - a root route `(/)` that will query a Mongo database and pass the mars data into an HTML template to display the data
    - a route called `(/scrape)` that will import `scrape_planet.py` script and call the scrape function

- `index.html` includes the following below:
    - takes the mars data dictionary and display all of the data in the appropriate HTML elements with some Boostrap 4 and css style customization 


![](https://raw.githubusercontent.com/diannejardinez/web-scraping-challenge/master/screenshot-index.png)
