# Web Scraping 
## Guess Game with Web Scraping. With the given quotes, guess the author who said that:interrobang:

PACKAGES to install

|                         Request                          |                            BeautifulSoup                            |                     CSV                   |
|----------------------------------------------------------|-------------------------------------------------------------------- |-------------------------------------------|
|[pip install Requests](https://pypi.org/project/requests/)|[pip install BeautifulSoup](https://pypi.org/project/beautifulsoup4/)|[pip install CSV](https://pypi.org/project/python-csv/)|


**1. Scrape the quotes**

  Here the function "scrape_quotes" have two functionalities:
  
   * scrape the [quotes webpage](http://quotes.toscrape.com/scroll), scraping the quotes of all the pages.
   * Get some features of those quotes, like (author, text, bio_link) and put on a dictionary inside of a list.
   
**2. The game** :brain:

  Here the function "start_game" have one functionality:
  
   * start the questions routine game. This routine have 4 parts, if you can´t guess:
   
      1. shows the text and ask who is the author; (first attempt) :thought_balloon: You have 4 attempts, don´t worry :sunglasses: 
      2. shows the birthday and the birthplace of the author; (second attempt) :open_mouth: now you have 3 attempts, think better!  :anger: :sweat:
      3. shows the first letter of the author´s first name; (third attempt) :stop_sign: your attempts are going to end!!! :tired_face:
      4. shows the first letter of the author´s last name. (fourth and last attempt) :warning: Nooo, you have to guess now, or you will lose!!! :man_judge: 
     
  :heavy_exclamation_mark: If you guess before your attempts end, the loop will break, and you will win the game!!! :trophy: :smiling_face_with_three_hearts: \
  :heavy_exclamation_mark: If you can´t guess before your attempts end, the loop will break, and you will lose the game!!! :sob:
  
  
**3. Start the game again**

  Here the code allows you to restart the game, if you want :muscle:


      
   
    
