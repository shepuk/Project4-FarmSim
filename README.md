# Sunrise Farm

Sunrise Farm is an interactive full stack app powered by Django. Grow and harvest crops, buy and sell goods.

![amiresponsive screenshot](/media/screenshots/home.png)

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
    - Sunrise Farm is designed to be accessilble to everyone, and was build with a mass-appeal casual audience in mind. Influence form hyper-casual experiences such as FarmVille was critical is designing user experience. With emphasis put into ease of use, accessibilty and clear user goals, the app is useable by anyone.

- #### User Stories
    - 'As a  typical user, 
    - 'As a fan of casual gaming, 
    - 'As an advanced user, 
    - 'As an inexperienced user, 
    - 'As a typical user,

- #### New Visitors
    - App should be clear in it's intent, and designed around user-friendliness.
    - Clear feedback for user interaction is important.
    - Easy user authentication and signup process is a must.
    - Quick and responsive feedback.

- #### Returning Visitors
    - Content should be easilly and quickly accessible.
    - User information such as current coins should be displayed clearly and quickly.


### Design
- #### Colours
    - Green naturally comes into thought when put in mind of a farm. Aside from that, High-contract would be utilised as usual to provide maximum readability for users who need it. 

![colour palette](/media/screenshots/palette.png)

- #### Typography
    - Google Fonts Martel was used for titles, headings and logos. Poppins was used for paragraph and smaller text. This serif & sans pairing offers an aesthetic look and seperates less important text form heading and section text.

![Martel font](/mediascreenshots/martel.png)
![Poppins font](/mediascreenshots/poppins.png)

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
    - Early design descisions were made using wireframes. I was able to stick to the inidial wireframe designs closely and only minor changes were made. However die to time constraints I was not able to include all pages/features which can be seen in the wireframes.
[Wireframe Screenshots](https://github.com/shepuk/Project4-farmsim/...wireframers)

- ### Flow diagram
    - A flow diagram was also created early on, to help structure the flow of the app. [See it here](https://github.com/shepuk/Project4-farmsim/...flowchart)


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






Bugs / Issues

Admin interface not loading, CRF error
Fix: https://stackoverflow.com/questions/29573163/django-admin-login-suddenly-demanding-csrf-token/70572093#70572093

Could not associate multiple inventory items with the same user more then one
Fix - was using onetoonefield, instead of foreighkey

Could not update/save model fields by using a variable as a field name in farm.views
fix - string format method was used to insert the variable into the model query

farm urls passing through two strings, were firing the first function in views every time because the first url can always avcept two strings.
Quick fix - added a third (unised) parameter to url to differantiate urls

toasts were always showing with opacity 0 
fixed by adding css to make fully opaque, then using jquery's fadeout() function to remove the message

gold icon from <a href="https://www.flaticon.com/free-icons/coin" title="coin icons">Coin icons created by Freepik - Flaticon

stick note design from https://code.tutsplus.com/tutorials/create-a-sticky-note-effect-in-5-easy-steps-with-css3-and-html5--net-13934

hero image https://www.pexels.com/photo/aerial-shot-of-green-milling-tractor-1595108/

gold text https://codepen.io/mandymichael/pen/xpLNeV

heroku ERROR: Could not build wheels for backports.zoneinfo, which is required to install pyproject.toml-based projects
https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta