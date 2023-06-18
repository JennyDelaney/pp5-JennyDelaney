# All-Tours Website

[View the live project here.](https://pp5-all-tours.herokuapp.com/)

This website was created for vistors coming to Ireland to be able to book a tour throughout the isle of Ireland in one place.

![home_page](/media/readme-images/home_page.jpg)

## Table of content: 
 1. [Site Goals](#Site-Goals)
 1. [Design/UX](#UX)
      1. [Wireframes](#Wireframes)
	  1. [Model Schema](#Model_schema)
      1. [Project Progression](#Project-Progression)
            * [Sprint 1](#sprint-1)
            * [Sprint 2](#sprint-2)
            * [Sprint 3](#sprint-3)
            * [Sprint 4](#sprint-4)
            * [Sprint 5](#sprint-5)
			* [Sprint 6](#sprint-6)
			* [Sprint 7](#sprint-7)
			* [Sprint 8](#sprint-8)
			* [Sprint 9](#sprint-9)
			* [Sprint 10](#sprint-10)
			* [Sprint 11](#sprint-11)
			* [Sprint 12](#sprint-12)
			* [Sprint 13](#sprint-13)
      1. [New User](#New-user)
      1. [Returning User](#Returning-user)
      1. [Design](#Design)
 1. [Structure of Website](#Structure)
 1. [Technologies Used](#Technologies-Used)
 1. [Testing](#Testing)
 1. [Deployment](#Deployment)
 1. [SEO/Marketing](#SEO)
 1. [Credits & Acknowledgements](#Credits)


***

## Site Goals:

The goals for this site are as follows:
* Allow users to book a tour of their choice from anywhere within Ireland
* Allow users to book and pay for the number of tickets they require for the trip

## User Experience (UX)

-   ### User stories

To demonstrate the Agile approach that was used for this project, GitHub issues were created and a Kanban board was used to record all the user stories. The user stories were categorised using different labels, i.e Must have, Should Have and Could have. Each story was then moved from 'To Do' to 'In Progress' to 'Done' as the project progressed, with Could have stories moved to a future version category.

-   ### Project Progression:

<details>
<summary>Sprint One</summary>

- Project Set-up: set up All Tours App
</details>

<details>
<summary>Sprint Two</summary>

- Set up AllAuth

- Import allauth templates and base.html

- Add blocks to base template

This covered the following User Stories -
![Sprint Two](/media/readme-images/sprint_2.jpg)

</details>

<details>
<summary>Sprint Three</summary>

### The Home Page

- Added home app and created templates

- customized homepage and maing page header

- completed home page header and css

- added mobile header and nav bar

This covered the following User Stories -
![Sprint Three](/media/readme-images/sprint_3.jpg)
</details>

<details>
<summary>Sprint Four</summary>

### **Adding Tours:**

- added tour app, models and fixtures

- customized admin

- added tour views and templates

- started tour template

- added tour details functionality

This covered the following User Stories -
![Sprint Four](/media/readme-images/sprint_4.jpg)
</details>

<details>
<summary>Sprint Five</summary>

- Added search functionality

- Added Category filtering

- Added Sorting

- Added sorting and tour counts to tour page

- Added sorting js and back to top link

This covered the following User Stories -
![Sprint Five](/media/readme-images/sprint_5.jpg)
</details>

<details>
<summary>Sprint Six</summary>

- Added shopping bag app, urls and templates

- Added bag context

- Added add to bag functionality

- Updated context processor

- Updated shopping bag template

- Added quanity input +/- buttons

- Added quantity boxes to shopping bag page

This covered the following User Stories -
![Sprint Six](/media/readme-images/sprint_6.jpg)
</details>

<details>
<summary>Sprint Seven</summary>

- Added toasts

- Added notification CSS, shopping bag preview and additional messages
</details>

<details>
<summary>Sprint Eight</summary>

- Created checkout app and models

- Added forms, admin and signals

- Added checkout views and templates

This covered the following User Stories -
![Sprint Eight](/media/readme-images/sprint_8.jpg)
</details>

<details>
<summary>Sprint Nine</summary>

- Added stripe elements

- Added basic checkout functionality

- Added checkout success logic

- Added order summary to checkout success page

- Added loading overlay

- Added webhook handler

- Added class methods to webhook handler and webhook views

- Added checkout form data caching in payment intent

- completed webhook handler

</details>

<details>
<summary>Sprint Ten</summary>

- Updated checkout form

- Added profiles app

- Updated allauth templates, views and updated template

- Added order history and updated checkout views

- Updated webhook handler to handle profiles

- Completed confirmation emails

This covered the following User Stories -
![Sprint Ten](/media/readme-images/sprint_10.jpg)
</details>

<details>
<summary>Sprint Eleven</summary>

- Create tour form for tour admin

- Add tour view, url and template

- Finished add tour functionality

- Editing tours

- Deleting tours

This covered the following User Stories -
![Sprint Eleven](/media/readme-images/sprint_11.jpg)
</details>

<details>
<summary>Sprint Twelve</summary>

- Deployment of project to Heroku

- Set up sending of real emails

- Add contact us app

- Add Newsletter app

- Update Contact us dropdown

</details>

***

####  New User:
* As a new user, I want to be able to view and read available tours
* As a new user, I want to be able to book a tour
* As a new user, I want to be able to register easily
* As a new user, I want to be able to view my shopping bag in case I want to update it
* As a new user, I want to be able to log in to view my previous orders and maintain my customer profile

#### Returning User:
* As a returning user, I want to log in to my account
* As a returning user, I want to book a tour
* As a returning user, I want to view my previous tours

### Design/Wireframes

-   #### Colour Scheme
    -   The two main colours used are black and white to give the site a dynamic, easily read view.
-   #### Imagery
    -   The image used in this project was taken from [Pexel](https://www.pexels.com/).
-   #### Wireframes
    -   ![Wireframe](/media/readme-images/wireframe.jpg)

*   ### Structure of website

    <details>
    <summary>Home Page</summary>

    ![Home Page](/media/readme-images/home_page.jpg)
    </details>
    
    <details>
    <summary>Register Page</summary>

    ![Register Page](/media/readme-images/register_page.jpg)
    </details>
    
    <details>
    <summary>Log In Page</summary>

    ![Sign_in](/media/readme-images/sign_in_page.jpg)
    </details>
    
    <details>
    <summary>All Tours Page</summary>

    ![Tours](/media/readme-images/all_tours_page.jpg)
    </details>

    <details>
    <summary>Individual Tour Page</summary>

    ![Tour Page 2](/media/readme-images/individual_tour_page.jpg)
    </details>

    <details>
    <summary>Shopping Bag Page</summary>

    ![Shopping Bag](/media/readme-images/shopping_bag.jpg)
    </details>

	<details>
    <summary>Checkout Page</summary>

    ![Checkout](/media/readme-images/checkout_page.jpg)
    </details>

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries, Programs & Applications Used:
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.elephantsql.com/)
* [Bootstrap](https://getbootstrap.com/)

#### Google Font
* Google Font was used to import the chosen font for this project.

#### CodeAnywhere
* Codeanywhere was used for writing all the code for this project. It was also used to commit and push to GitHub.

#### GitHub
* GitHub was used to store this project.

#### Heroku
* Heroku was used to deploy the project.

#### Amazon Web Services
* Amazon Web Services was used to store the media and static files used in this project

#### Google Development Tools
* Google Dev Tools was used to edit code and check responsiveness before making the changes permanent.

## Testing:
Testing information can be viewed [here](/documents/TESTING.md)

## Deployment
Deployment information can be viewed [here](/documents/DEPLOYMENT.md)

## Deployment
Deployment information can be viewed [here](/documents/DEPLOYMENT.md)

## SEO / Marketing
The use of social media marketing is very important for bringing in customers and increasing visibility of the site. 
The approved way to generate interest is an organic approach as the marketing budget will be small initially.

Facebook marketing is often more important than any other platform, we are using it for this project.

![Facebook](/media/readme-images/facebook_desktop.jpg)

The meta keywords and description in base.html have been amended to the researched keywords. 
On significant pages like the index and product pages, the site title has the name The Policy Shop and also has keywords.

The homepage has also been designed with SEO in mind. 
Some of the keywords are also used in the text portions of the webpage, with strong tags surrounding the major keywords, to improve search results. 

For SEO purposes, we have also added a sitemap.xml and robots.txt file to the website's root directory for search engines to crawl the site. 

A sitemap is a method of classifying a website, indicating the URLs and the information contained within each section.
The URLs on your website that a search engine crawler is permitted to visit are specified in a robots.txt file.

## Credits & Acknowledgements

All code was created and manipulated by myself while following the Code Institute Course PP5 content. I customised the code to meet the requirements of my website.

I had no mentor for this project. I would like to thank my family who tested the website for me.