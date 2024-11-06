from home.models import Product
from django.contrib import messages

class Cart():
    def __init__(self, request):
        self.session = request.session
        # Get request
        self.request = request
        # Get the current session key if it exists, otherwise create an empty cart
        self.cart = self.session.get('session_key', {})
        


#add product to cart.....
    def add(self, product):
        product_id = str(product.id)
        # Check if the product is already in the cart
        if product_id in self.cart:
            messages.success(self.request, "Product is already in cart")
            return False  # Optional: can be used to indicate the product was not added
        else:
            # Add product with price to the cart
            self.cart[product_id] = {
                'name': product.name,
                'price': str(product.price),
            }
            # Mark session as modified to save changes
            self.session['session_key'] = self.cart  # Save the cart to session
            self.session.modified = True
            return True  # Indicate that the product was added successfully

	
	
	#length
    def __len__(self):
        return len(self.cart)
    
	#updating shopping cart summary ...
    def get_prods(self):
        product_ids=self.cart.keys() #get ids from cart 
        #use ids to look up product in database models...
        products=Product.objects.filter(id__in=product_ids)
        return products
        
   
	