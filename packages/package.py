# packages are another way to organize code
# packages are containers for multiple modules
# a package is basically a folder or directory
# There will be a directory called 'ecommerce' where all of our modules will be
# that directory will have '__init__.py'. this means that Python will treat that directory as a package
# it will also have a new module named 'shipping'
# unlike a module, we cannot import the python file directly
# there are three ways to do this:
import ecommerce.shipping # we are importing the package first with the file
ecommerce.shipping.calc_shipping() # we then call the function, you have to reference the package and the file first
# the output should be 'calc_shipping'

# here is the second way:
from ecommerce.shipping import calc_shipping # here we are calling the function directly. If needed, you can call multiple functions from the package by separating them with camma's
calc_shipping() # we don't need to worry about referencing the package or the file

# here is the third way:
from ecommerce import shipping # here we are importing the package and the file, but not the function
shipping.calc_shipping() # here we called the function

# *whichever way you choose to import the package is up to you. it does not matter which one you use
