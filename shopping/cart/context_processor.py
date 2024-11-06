from .cart import Cart
#here cart.py is the file name and Cart is the class 

def cart(request):
    #return the default data from the cart
    return {'cart':Cart(request)}