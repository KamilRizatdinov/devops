# Python best practices:

* Follow python style guidelines. Use linters and autoformatters. Pre-commit hooks are also powerfull in this context
* Always create a python virtual environment when developing python application
* Write clean and readable code. Don't repeat yourself, split functions, classes and methods if amount of responsibility they take becomes too heavy and might be misleading
* Mindfully choose the naming of your variables, functions, classes and methods. Make sure that your namings are clear and descriptive
* Do not reinvent things, that might turn your codebase into a mess. PyPI is full of good things
* Write proper documentation and comment, do not be afraid to leave the link to the source where you found the solution
* Use typechecking, do not put this mental work on your brain, give it a chance to solve tasks
* Use logging best practices. Imagine being a doctor whose patients always know what hurts and can clearly describe it, wow!
* Use well-known programming patterns. They definitely exist for a reason!
* Use asyncronous functions for events that take a lot of aside computations. Why you should wait for your API request to execute if you can do something else this time?
* Avoid deadlocks of your database transactions. This is probably the hard thing to do in a big project
* Try to optimize your database queries number. Do not fall into N+1 problem
