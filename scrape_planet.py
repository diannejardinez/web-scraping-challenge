from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd


def init_browser():
    # Setting up path for Browser splinter
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", executable_path, headless=False)


def scrape_info():
    ### NASA Mars News ###

    # Calling function for Browser splinter
    browser = init_browser()

    # Visting url througher splinter browser
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)

    # Using Beatiful soup to parse the html in the designated url
    html = browser.html
    soup = bs(html, "html5")

    # Get the date, title, and content text in the latest news
    news_date = soup.find('div', class_='list_date').text
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    ############################################
    ### JPL Mars Space Images - Featured Image ###

    # Calling function for Browser splinter
    browser = init_browser()

    # Visting url througher splinter browser
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    time.sleep(1)

    # Using Beatiful soup to parse the html in the designated url
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the image url for the JPL Deatures space image
    featured_image_tag = soup.find('article', class_='carousel_item')['style']
    featured_image_url = featured_image_tag.split("url")[1]
    featured_image_url = featured_image_url.split("'")[1]
    featured_image_url = ('https://www.jpl.nasa.gov' + str(featured_image_url))

    ############################################
    ### Mars Weather ###
    # Calling function for Browser splinter
    browser = init_browser()

    # Visting url througher splinter browser
    url = 'https://twitter.com/MarsWxReport?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
    browser.visit(url)

    time.sleep(1)

    # Using Beatiful soup to parse the html in the designated url
    html = browser.html
    soup = bs(html, "html5")

    #Getting latest weather tweet
    mars_weather_tags = soup.find_all('div', class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0')
    for mars_weather in mars_weather_tags:
        if 'InSight sol' in mars_weather.text:
            mars_weather.text
            break
    mars_weather = (mars_weather.text)  

    ############################################
    ### Mars Facts ###

    # Calling function for Browser splinter
    browser = init_browser()

    # Using the read_html function in Pandas to automatically scrape tabular data from designated url
    url = 'http://space-facts.com/mars/'
    mars_facts_table = pd.read_html(url)

    # Slicing dataframes to use normal indexing
    mars_facts_df = mars_facts_table[0]
    mars_facts_df.columns = ['Measurement', 'Unit']

    # Using to_html method to generate HTML tables from mars_facts_df 
    mars_facts_html_table = mars_facts_df.to_html(index=False)

    ############################################
    ### Mars Hemispheres ###

    ## Cerberus Hemisphere Enhanced ##
    # Calling function for Browser splinter
    browser = init_browser()
    # Visting url througher splinter browser
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    time.sleep(1)
    # Using Beatiful soup to parse the html in the designated url
    html = browser.html
    soup = bs(html, "html5")
    # Getting image url
    cerberus = soup.find('img', class_='wide-image')['src']
    cerberus_url = ('https://astrogeology.usgs.gov/' + str(cerberus)) 
    # Getting Hemisphere Name 
    cerberus_title = soup.find('h2', class_='title').text

    ## Schiaparelli Hemisphere Enhanced ##
    # Calling function for Browser splinter
    browser = init_browser()
    # Visting url througher splinter browser
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)
    time.sleep(1)
    # Using Beatiful soup to parse the html in the designated url
    html = browser.html
    soup = bs(html, "html5")
    # Getting image url
    schiaparelli = soup.find('img', class_='wide-image')['src']
    schiaparelli_url = ('https://astrogeology.usgs.gov/' + str(cerberus)) 
    # Getting Hemisphere Name
    schiaparelli_title = soup.find('h2', class_='title').text

    ## Syrtis Major Hemisphere Enhanced ##
    # Calling function for Browser splinter
    browser = init_browser()
    # Visting url througher splinter browser
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)
    time.sleep(1)
    # Using Beatiful soup to parse the html in the designated url
    html = browser.html
    soup = bs(html, "html5")
    # Getting image url
    syrtis_major = soup.find('img', class_='wide-image')['src']
    syrtis_major_url = ('https://astrogeology.usgs.gov/' + str(cerberus)) 
    # Getting Hemisphere Name 
    syrtis_major_title = soup.find('h2', class_='title').text

    ## Valles Marineris Hemisphere Enhanced ##
    # Calling function for Browser splinter
    browser = init_browser()
    # Visting url througher splinter browser
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    time.sleep(1)
    # Using Beatiful soup to parse the html in the designated url
    html = browser.html
    soup = bs(html, "html5")
    # Getting image url
    valles_marineris = soup.find('img', class_='wide-image')['src']
    valles_marineris_url = ('https://astrogeology.usgs.gov/' + str(cerberus)) 
    # Getting Hemisphere Name 
    valles_marineris_title = soup.find('h2', class_='title').text

    # Creating dictionary for each hemisphere title and image url
    cerberus_dict ={
        'title': cerberus_title,
        'img_url': cerberus_url
    }
    schiaparelli_dict ={
        'title': schiaparelli_title,
        'img_url': schiaparelli_url
    }
    syrtis_major_dict ={
        'title': syrtis_major_title,
        'img_url': syrtis_major_url
    }
    valles_marineris_dict ={
        'title': valles_marineris_title,
        'img_url': valles_marineris_url
    }

    # Creating a list to store all of the hemisphere dictionaries
    hemisphere_image_urls= []
    hemisphere_image_urls.append(cerberus_dict)
    hemisphere_image_urls.append(schiaparelli_dict)
    hemisphere_image_urls.append(syrtis_major_dict)
    hemisphere_image_urls.append(valles_marineris_dict)

    ############################################
    ### Store data in a dictionary ###
    planet_data = {
        ### NASA Mars News ###
        "news_date": news_date,
        "news_title": news_title,
        "news_p": news_p,
        ### Featured Image ###
        "featured_image_url": featured_image_url,

        ### Mars Weather ###
        "mars_weather": mars_weather,

        ### Mars Facts ###
        "mars_facts_html_table": mars_facts_html_table,  

        ## Mars Hemispheres ##
        "hemisphere_image_urls": hemisphere_image_urls
        }


    # Close the browser after scraping
    browser.quit()

    # Return results
    return planet_data

