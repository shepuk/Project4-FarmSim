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
