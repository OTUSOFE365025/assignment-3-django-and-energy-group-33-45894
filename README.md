<h1>Excercise 1</h1>
<h2>Repository Overview</h2>
This repository contains a simple Django-based product lookup system with a Tkinter front-end. You can run it with <i>python gui.py</i> <br><br>

DATABASE <br>
We defined a Product Entity in <b>db/models.py</b> consisting of a upc as the primary key, a product name and a product price.
We then seeded a few entries into <b>db.sqlite3</b> by running the following command in <b>main.py</b>: <br>
<t><i>Product.objects.create(upc=UPCNumber, name=ProductName, price=Price)</i> <br>

PRODUCT LOOKUP <br>
For part b, we created a lookup function in our controller (<b>main.py</b>). We relied on the database imports and setup in (<b>main.py</b>). Our lookup function uses the upc entered by the user to return the related product name and price. IF the upc could not be found in the db then, Not Found and 0.00 are returned. <br>

GUI <br>
We decided to use TKinter for the UI. We created the view file called <b>gui.py</b> and inside we have an entry box for the UPC, a submit button, a text section for the reciept and a label at the bottom for the running total. We get the upc from the user, and output the results from our lookup function in the controller.
    
<h2>Application Demonstration</h2>
<ol>
    <li>Start the program</li>
    <img width="124" height="25" alt="image" src="https://github.com/user-attachments/assets/c9e79859-35da-4f53-bcc1-50a5bac60c69" /><br>
    <li>Enter a UPC</li>
    <img width="498" height="319" alt="image" src="https://github.com/user-attachments/assets/766c7c3a-7815-465b-a91c-a967f472d5c9" /><br>
    <li>Click Scan</li>
    <img width="500" height="324" alt="image" src="https://github.com/user-attachments/assets/d6c02621-ccfd-41ad-a2aa-078408b30d91" /><br>
    <li>Repeat</li>
    <img width="502" height="322" alt="image" src="https://github.com/user-attachments/assets/8b45dbc5-0564-4c62-b1ad-d4fb87fe7c9a" /><br>
    <li>Handling for invalid upc</li>
    <img width="501" height="319" alt="image" src="https://github.com/user-attachments/assets/89cc473e-2e77-4b1d-9949-8f33c533200e" />
</ol>
