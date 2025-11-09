<h1>Excercise 1</h1>
<h2>Repository Overview</h2>

DATABASE <br>
We defined a Product Entity in <b>db/models.py</b> consisting of a upc as the primary key, a product name and a product price.
We then seeded a few entries into <b>db.sqlite3</b> by running the following command in <b>main.py</b>: <br>
<t><i>Product.objects.create(upc=UPCNumber, name=ProductName, price=Price)</i> <br>

PRODUCT LOOKUP <br>
For part b, we created a lookup function in our controller (<b>main.py</b>). This lookup function uses the upc entered by the user to return the related product name and price. IF the upc could not be found in the db then, Not Found and 0.00 are returned. <br>

GUI <br>
We decided to use TKinter for the UI. We created the view file called <b>gui.py</b> and inside we have an entry box for the UPC, a submit button, a text section for the reciept and a label at the bottom for the running total. We get the upc from the user, and output the results from our lookup function in the controller.
    
<h2>Application Demonstration</h2>
