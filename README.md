# django-test


## Instructions du test technique (non rempli dans sa totalité) :



Create a Project
* with a minimum of two apps on it and maintain the different proper working url models view and template for each app.
* Show the crud operation in each app with both Template view and API view.
* Implement Pagination in Project.
* Implement search in the project with all fields and any comparable character.
* In just detailView of item, change item name as example,

itemname-Pertimm = itemname-Pertimm.



and write a functions that takes  the above value  and it returns as 

 {value1: [i,t,e,m,n,a,m,e], value2: [P,e,r,t,i,m,m]}  

after that, 

create context as, 
context[module.Fieldname] =  while returning the data



Note here module.Fieldname is your model class field name that should be passed through context, to detailView.


* The project should have some Image field.
* The model should have a Json field with default value from a function.
* The model class should have a structure with Foreign Key, with manytoMany field,
child parent relationship Field,
