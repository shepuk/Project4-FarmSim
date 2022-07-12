# Sunrise Farm

Sunrise Farm is an interactive full stack app powered by Django. Grow and harvest crops, buy and sell goods.

![amiresponsive screenshot](/media/screenshots/home.png)

- [Sunrise Farm](#sunrise-farm)
    + [Visit the website](#visit-the-website)
    + [Full stack Project](#full-stack-project)
    + [Primary Objectives](#primary-objectives)
    + [Early ideas & goals](#early-ideas---goals)
    + [Screenshots](#screenshots)
    + [Responsive Design](#responsive-design)
    + [User Experience](#user-experience)
    + [Design](#design)
    + [Wireframes](#wireframes)
    + [Flow diagram](#flow-diagram)
    + [Features](#features)
    + [Security](#security)
    + [Technologies](#technologies)
    + [Testing](#testing)
    + [Bugs & Issues](#bugs---issues)
    + [Setup, Backups & Deployment](#setup--backups---deployment)
    + [Credits](#credits)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


### Visit the website

[View the live project here.](https://sunrise-farm.herokuapp.com/)

### Full stack Project

Built with the fullstack framework Django, Sunrise Farm utilises several technologies including Python, JavaScript and SQL, along with several other packages outlined in the [technologies](#technologies) section below.

### Primary Objectives

 - Design and deploy a full stack web application using Django.
 - Create a highly interactive experience with relevant feedback to users.
 - Model and manage data in a SQL database.
 - Query and manipulate data and offer CRUD functionality.
 - Meet guidelines regarding accessibility and UX design.
 - Design and maintain a relation database housing multiple related models.
 - Include online payment functionality.
 - Deploy to a cloud platform.
 - Identify and apply security features.

### Early ideas & goals

 - Design and build an interactive game with a deep set of additional features.
 - Implement database CRUD functionality into the design.
 - Design a databse in which fields are related and compared against each other. 
 - Create a varied & fun experience with longevity in mind.
 - Create a full game loop, in which users can make several key decisions.
 - The content should be justified, accessible, responsive and presented logically.

 ### Screenshots

The home page - showing the full list of available activities. I wanted to make navigation easy and obvious to the user, and allow the home page to act as a 'hub'. From here, users can navigate to any part of the website and perform actions. Icons and strong text is used to help options stand out.
![Home page screenshot](/media/screenshots/home.png)

Navigation - a sidebar was chosen for quick and easy app navigation. Some challenges were met which implementing responsive custom interaction for the sidebar but it now reacts as expected on any device.
![Home page screenshot](/media/screenshots/nav.png)

The farm page is used to allow users to plant and harvest crops. A dropdown menu is used to select a seed to plant and a store option is offered as a shortcut if the user wishes to buy more seeds. Significant date/time comparisons are make on the backend to calculate growtimes.
![Farm page screenshot](/media/screenshots/crops.png)

From the store, users can choose a quantity and buy seeds, plants and tools. Not pictured, the selling market functions similarly to this. The products model is deel and fully features, giving each product several custom attributes used throughout the website.
![Store page screenshot](/media/screenshots/store.png)

The profile app shows the currently logged in user's details.
![Profile page screenshot](/media/screenshots/profile.png)

 ### Responsive Design

All pages are designed with mobile and desktop browsing in mind. Columns stack on smaller screens and a hamburger-style menu is offered. All information and features are still available at smaller screen sizes.
[netbook view](/media/screenshots/responsive/netbook.png)
[tablet view](/media/screenshots/responsive/tablet.png)
[tablet nav view](/media/screenshots/responsive/tabletnav.png)
[mobile view](/media/screenshots/responsive/mobile.png)
[mobile nav view](/media/screenshots/responsive/mobilenav.png)

 ### User Experience
- #### Target Audience
    - Sunrise Farm is designed to be accessilble to everyone, and was built with a mass-appeal casual audience in mind.

- #### User Stories
    - 'As a  typical user, I want to be able to use and understand the site with ease, and navigate without any major issues.'
    - 'As a fan of casual gaming, I want a fun and low-stress and satisfying game loop which I can return to on a regular, and sometimes sporadic, basis' 
    - 'As an advanced user, I require quick navigation and responsive feedback. An option to upgrade with a payment option would also be interesting.'
    - 'As an inexperienced user, I need to understand the basics and easilly gather information on how to operate the site.'

- #### New Visitors
    - The app should be clear in it's intent, and designed around user-friendliness.
    - Clear feedback should be provided in response to user interaction.
    - Easy user authentication and signup process is a must.

- #### Returning Visitors
    - Content should be easilly and quickly accessible.
    - User information such as current coins should be displayed clearly and quickly.
    - Game state should be maintained and the user should be presented with what they expect to see.


### Design
- #### Colours
    - Green naturally comes into thought when put in mind of a farm. Aside from that, High-contract would be utilised as usual to provide maximum readability for users who need it. 

![colour palette](/media/screenshots/palette.png)

- #### Typography
    - Google Fonts Martel was used for titles, headings and logos. Poppins was used for paragraph and smaller text. This serif & sans pairing offers an aesthetic look and seperates less important text form heading and section text.

![Martel font](/media/screenshots/martel.png)
![Poppins font](/media/screenshots/poppins.png)

- #### Imagery
    - 16x16 retro-style sprites were used throughout the design to provide an old-school gaming feel. These types of sprites are readilly available for royalty-free use also. These were scaled up for modern screens and retained their pixel designs with CSS. Without this, images appear blurry and stretched.

![sprite](/media/corn_seed.png)![sprite](/media/corn.png)![sprite](/media/tomato_seed.png)![sprite](/media/tomato.png)![sprite](/media/axe.png)![sprite](/media/watercan.png)

- #### Accessibility
    - All images have a descriptive `alt` attribute.
    - Contrast is high throughout the website and all text is clearly readable.
    - All forms utilise a `label` tag.
    - Headings and paragraphs are used appropriately.
    - Semantic markup is used throughout the website.
    - Tables are used in place of divs where appropriate.
    - Clear flash messages are shown at the top of the screen and offer feedback for interaction.

- #### Database Design
    - I began designing my databases by identifying the categories which would need their own model. After scoping out the project size and deciding on a final set of features, I implemented the following models; 
        1. **Profile** would contain expanded user information. Allauth (built in to Django) already provided login details and password etc, and with theProfile model I could implement charater stats, coins, premium membership and more.
        2. **Farm** would contain all relevant information to a user's current active plants in the farm. Each individual crop is tracked and is paired with a product from the store model. Each crop's plant time and harvest time are also stored - this allows me to track when the crops are due for harvest, along with a 'growtime' attribute belonging to a foreign product model.
        3. **Inventory** keeps track of a user's currently owned items. This is updated during several user interactions in the farm, store or selling market. Each inventory instance is paired with the user model as well.
        4. **Products** houses all of the store items, and is also responsible for storing information on items such as buy price, sell price, grow time and which crop a seed may produce. Several other models rely on this products model for informartion on game state.
        5. **Categories** is used to place fields in the products model into particular categories. This is useful when displaying which items can be planted for example (you can't plant an axe item!). 


- ### Wireframes
    - Early design descisions were made using wireframes. I was able to stick to the inidial wireframe designs closely and only minor changes were made.
![Wireframe image](https://github.com/shepuk/Project4-FarmSim/blob/main/media/wireframes/wireframe.png)

- ### Flow diagram
    - A flow diagram was also created early on, to help structure the flow of the app. 
![Flowchart image](https://github.com/shepuk/Project4-FarmSim/blob/main/media/wireframes/flowchart.png)

### Features
- #### Current features
    - Deep SQL database interaction used for updating user informartion, tracking datetime data and displaying complex data models on screen. 
    - Stripe payment system used to enable premium features on a user account.
    - Allauth user security features for a secure login and verification experience.
    - Tracking of multiple planted crops, powered by Python datetime, Django models and JavaScript.
    - Commerce areas, buying and selling, and user wallet/inventory tracking.
    - Django message system for clear user feedback in the form of toast messaging.
    - Complex model table links and data comparisons.

- #### Features to implement
- Unfortunately due to time constraints and over-planning features, there are still several key features to implement into the final product;
    - To complete and deeped the game loop, a 'quests' section was to be implemented. This would provide another use for in-game currency and inventory items, rather that just buying and selling. For example, townfolk would provide requests for a certain amount of tomatoes - another use for tomatoes other than just selling them for profit.
    - An additional category of 'flowers' was planned, to seperate crops from flower plants. Currently the few flower seeds that are available simply go into the same farmland as the crops.
    - A 'museum' was planned as a way to showcase user acomplishment - number of crops harvested, total gold aquired etc.
    - 'Forraging' was a feature I woul dhave liked to add - to allow the user to collect reasources such as wood and stone, to build additional farm buildings. A chicken coop to look after chickens, for example.
    - Some premium features did not make it into the app before deadline. For example, an additional 8 slots for planting crops would have been made available.
    - I wanted to implement a user chat room - not a crucial feature, but would have provided some additional user interactivity.


### Security
-  Allauth was used for user authentication and provided secure password hashing for new signups or logging in.
- Environmental variables are included in a .gitingore file to prevent any sensitive data being publicly available.


### Technologies
- [Django](https://www.djangoproject.com/) Framework was used to build the project
- [AllAuth](https://github.com/pennersr/django-allauth)
- [Python](https://www.python.org/) was the primary backend language used.
- [Heroku Postgres](https://www.heroku.com/postgres) is a Heroku-hosted database which the project was ported to for hosting.
- [JavaScript](https://www.javascript.com/) was used for some app logic.
- [jQuery](https://jquery.com/) was used for DOM manipulation.
- [Bootstrap CSS](https://getbootstrap.com/) CSS awas used throughout the app for it's attractive design and easy implementation.
- [HTML](https://en.wikipedia.org/wiki/HTML) formed the structure of the site and also included significant Django templating.
- [Font Awesome](https://fontawesome.com/) provided some icons throughout the site.
- [Google Fonts](https://fonts.google.com/) provided the use of the Averia Libre font.
- [Git](https://git-scm.com/) was used via the terminal for version control.
- [Github](https://github.com/) was used to host and store the project files.
- [Heroku](https://dashboard.heroku.com/login) is used to host the app.
- [Gitpod](https://gitpod.io/workspaces) was my primary IDE during project development.
- [Figma](https://www.figma.com/) was used during the design phase for wireframes.
- [Diagrams.net](https://app.diagrams.net/) was used for the flow chart.
- A more thorough list of technologies used, including plugins, can be found in the requirements.txt file 

### Testing
- #### Primary Objectives

 1. Design and deploy a full stack web application using Django.
    - I have successfuly designed and built a full-stack web application using the Django framework. It is full stack in the sense that it is the functional entirety of an application, comprising both the front end and the back end.
 2. Create a highly interactive experience with relevant feedback to users.
    - The app offers plenty of interactive pages with effective toast messaging providing feedback. 
 3. Model and manage data in a SQL database.
    - The SQL database housing all app information is modeled and designed in a defensive way, properly dealing with errors and handling data relationships efficiently and intelligently.
 4. Query and manipulate data and offer CRUD functionality.
    - The database is queried and manipulated on a regular bases as the user browses and interacts, offering full crud functionality.
 5. Meet guidelines regarding accessibility and UX design.
    - Standard guidelines around accessibility and UX design have been met - with relevant symantec markup and descriptive tags. Colours, text and buttons are used effectively accross the site for maximum ease of use.
 6. Design and maintain a relational database housing multiple related models.
    - The database contains many related fields and handles data manipulation efficiently. Multiple models have been set up. 
 7. Include online payment functionality.
    - Stripe was used to implement a payment service, in which users can buy a premium membership and receive bonuses across many parts of the app experience.
 8. Deploy to a cloud platform.
    - Final build was deployed to Heroku cloud platform, including a hosted postgres database.
 9.  Identify and apply security features.
    - Outlined in [security](#security) section.


- #### Early ideas & goals
 1. Design and build an interactive game with a deep set of additional features.
    - I have built a highly interactive farming simulator-type game with several features and significant database operations. There are numerous features for users to partake in. As outlined above, however, there cwas a planned further set of features which I was not able to implement in time.
 2. Implement database CRUD functionality into the design.
     - The database which I have implemented into the the back end of the app is integral to the user experience, and utilises full CRUD functionality.
 3. Design a databse in which fields are related and compared against each other. 
     - Model fields rely heavily on related data, for example the product model houses many important fields which are used to supply information on how to deal with user interaction and alter inventory and user models.
 4. Create a varied & fun experience with longevity in mind.
     - The final product does not quite meet my initial expectations with regards to longevity. This is mainly because the game loop is not fully complete and users are not presented with the full set of features to use their in-game assets. With that being said, I think the final product is still enjoyable and varied.
 5. Create a full game loop, in which users can make several key decisions.
     - See above point. The game loop is not fully fleshed out, and users have limited choice when it comes to spending their in-game coins or selling products. To complete the game loop, there would be some risk/reward choices and goals to achieve such as 'should I sell or complete a task with these crops I have grown', and the ability for users to play towards certain goals.
 6. The content should be justified, accessible, responsive and presented logically.
     - In terms of accessible and responsive design, the app is very user friendly and easy to use. Content is presented logically, and uses symantec markup tags like `<article>` for example. 



- #### Target Audience
1. Sunrise Farm is designed to be accessilble to everyone, and was built with a mass-appeal casual audience in mind. Influence form hyper-casual experiences such as FarmVille was critical in designing user experience. With emphasis put into ease of use, accessibilty and clear user goals, the app is useable by anyone.
    -  Influence form hyper-casual experiences such as FarmVille was critical in designing user experience. With emphasis put into ease of use, accessibilty and clear user goals, the app is useable by anyone. The app caters to a wide audience well. 

- #### User Stories
1. 'As a  typical user, I want to be able to use and understand the site with ease, and navigate without any major issues.'
    - Care was taken into designing the UI for the site, and around designing a smooth and understandable UX. A responsive sidebar is used with large, obvious buttons which are clearly labeled. Headings make content obvious and the page count is kept down to a minimum to avoide excessive browsing. Everything is accessible in at least two clicks, meaning users can get where they need to be in a matter of seconds.
2. 'As a fan of casual gaming, I want a fun and low-stress and satisfying game loop which I can return to on a regular, and sometimes sporadic, basis' 
    - The app offers a casual and low-impact gaming experience. As memtioned above,  the game loop could certainly be more fleshed out and satisfying, but in its current state the game still offers a stress-free and rewarding set of features. I made sure to not make any actions take too long (such as waiting for crops to harvest) as this would slow down actions and become less interesting. User data is persistent so that casual users can return whenever and pick up where they left off.
3. 'As an advanced user, I require quick navigation and responsive feedback. An option to upgrade with a payment option would also be interesting.'
    - A tripe payment system was implemented to satisfy this user story. Navigation and quick, informative toasts are used to provide quick-clickers with instant feedback. A local database also helps with speed.
4. 'As an inexperienced user, I need to understand the basics and easilly gather information on how to operate the site.'
    - A comprehensive help guide is offered alongside a site designed around easy user interaction. Visually, users can see obviously what the goals of the site are and what they should be doing.

- #### New Visitors
1. The app should be clear in it's intent, and designed around user-friendliness.
    - New visitors are presented with clearly labeled options and interactions which provide relevant feedback if they are doing something which is outside of the rules of the logic. 
2. Clear feedback should be provided in response to user interaction.
    - Feedback is provided accross the whole site and give users instant feed back as to actions performed that are either correct or incorrect. Quick guidance is provided in the toast messagig to let users know if they need to try something else. 
3. Easy user authentication and signup process is a must.
    - Thanks to AllAuth, user authentication was implemented easilly and users can expect a quick and easy login/logout/register process.

- #### Returning Visitors
1. Content should be easilly and quickly accessible.
    - A responsive sidebar is used with large, obvious buttons which are clearly labeled. Headings make content obvious and the page count is kept down to a minimum to avoide excessive browsing. Everything is accessible in at least two clicks, meaning users can get where they need to be in a matter of seconds.
2. User information such as current coins should be displayed clearly and quickly.
    - Coins and inventory are extremely easy to find and the current coins amount is persistent showed in the nav area for logged in users.
3.  Game state should be maintained and the user should be presented with what they expect to see.
    - The database is used to store critical game information and was designed that users, once logged in, will see the exact same information as when they logged out. Eg- Datetime is used for the farm/crops section so that even if the game is left for a while or logged out, the game logic will still calculate the time between the original dates/times and provide the correct data.


- #### Manual Testing
    - Multiple browsers and devices were used to test the application.
    - The deployed website was also tested againt the development version to ensure everything worked as expected.
    - BrowserStack was used for their large variety of testing functionalty. I was able to test the app on over 50 devices including different OS, tablets and mobiles.
    - Modern browsers such as Chrome, Firefox and Edge display and load content as expected. Older browsers such as Internet Explorer are incompatible with large portions of the website, and are not reccomended. 
    - Mobile browsers handle styling and responsive design very well. Identical functionality to desktop/laptop screens.
    - Friends and family were utilised to test links, spelling, design and responsiveness.

- #### Testing the code
 - Validators were used for the deployed code.
    - [PEP8 Online](http://pep8online.com/) was used to make sure Python code was written to guidelines and falls within PEP8 compliancy. [See the PEP8 results here]()

### Bugs & Issues
- #### Resolved bug examples
1. Django admin interface was not loading, and producing a CRF error.
    - Fix: Adding the following to middleware in settings resolved this issue: `django.middleware.csrf.CsrfViewMiddleware` [Link to fix](https://stackoverflow.com/questions/29573163/django-admin-login-suddenly-demanding-csrf-token/70572093#70572093)

2. During development I ran into an issue when trying to associate multiple inventory items with the same user more then once.
    - Fix - The fix here was using onetoonefield, instead of foreighkey

3. Could not update/save model fields by using a variable as a field name in farm.views
    - Fix - the python string format method was used to insert the variable into the model query.

4. Farm urls passing through two strings, were firing the first function in views every time because the first url can always avcept two strings.
    - Quick fix - added a third (unised) parameter to url to differantiate urls.

5. Toasts were always showing with opacity 0 and were invisible to the user.
    - Fixed by adding css to make fully opaque, then using jquery's fadeout() function to remove the message.

6. heroku ERROR: Could not build wheels for backports.zoneinfo, which is required to install pyproject.toml-based projects
    - Fix found on StackOverflow: [Link](https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta)

### Setup, Backups & Deployment
[Gitpod](https://www.gitpod.io/) was used as my primary IDE.
A template was provided by Code Institute which I cloned for my project repository.
Opening the repository in Gitpod is made simple thanks to a [Chrome Extension](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki).

- Django commands used:
1. Build Django app with `django-admin startproject farmsim`
2. Add new apps to project with `django-admin startapp appName`
3. Run development server with `python3 manage.py runserver`
4. Trial run of database changes with `python3 manage.py makemigrations --dry-run`
5. Database migrations with `python3 manage.py makemigrations`
6. Database migrations with `python3 manage.py migrate`
7. Fixture (JSON) loading with `python3 manage.py loaddata products`

Git / Github were used for file versioning and hosting.
`$ git add -A` was used initially to add my files and folders to the staging area, followed by git `$ commit -m "commit message"` and `$ git push` to add everything to my Github repository. These three commands allow me to commit changes and upload new code to Github. Git commits were used often, for any changes, new features or bug fixes.

The Github repository was linked to Heroku for hosting and teasting early in development. Using the Heroku CLI, I was able to upload code to the Heroku hosting service with the following commands;
`$ heroku login` (use Heroku login credentials here)
`$ git add .`
`$ git commit -am "Heroku commit message"`
`$ git push heroku main`

### Credits

#### Documentation & Online Help
- [Python Documentation](https://www.python.org/doc/)
- [Django Documentation](https://docs.djangoproject.com/en/4.0/)
- [Mozilla MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/column-count)
- [W3 Schools](https://www.w3schools.com/)

#### Media
- [Hero image](https://www.pexels.com/photo/aerial-shot-of-green-milling-tractor-1595108/)
- [Gold text](https://codepen.io/mandymichael/pen/xpLNeV)
- [Gold icon](https://www.flaticon.com/free-icons/coin)

#### Content
All content was written by me.

#### Acknowledgements
Code Institute & Newcastle College.