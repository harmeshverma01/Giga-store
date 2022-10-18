from product.models import ProductCategory, Product, ProductImages
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from rest_framework import serializers
from cart.models import Cart


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'           
        
class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['Image']        
                                                                                         

class ProductSerializer(serializers.ModelSerializer):
    ProductImages = ProductImagesSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'  
        depth = 1       
        
class CustomerSerializer(serializers.ModelSerializer):
    #confrim_password = serializers.CharField(max_length = 255)
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'password'
        ]
        extra_Kwargs ={
            'password' : {
                'write_only' : True
            }
        }    
    
    def create(self, validatedData):
        user = User.objects.create(
            username=validatedData['username'],
            first_name=validatedData['first_name'],
            last_name=validatedData['last_name'],
            email=validatedData['email'],
        ) 
        user.set_password(validatedData['password'])
        user.save()
        return user
    
    def update(self, userObject, validatedData):
        if validatedData.get('username'):
            userObject.username = validatedData.get('username',userObject.username)
        if validatedData.get('first_name'):
            userObject.first_name = validatedData.get('first_name',userObject.first_name)
        if validatedData.get('last_name'):    
            userObject.last_name = validatedData.get('last_name',userObject.last_name)
        if validatedData.get('email'):    
            userObject.email = validatedData.get('email',userObject.email)
        if validatedData.get('password'):
            userObject.set_password(validatedData.get('password'))
        userObject.save()
        return validatedData    

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','product', 'quantity'] 
        
class PaymentSerializer(serializers.Serializer):

    payment_id = serializers.CharField(max_length=80)
    tarnsaction_id = serializers.CharField(max_length=150)
    
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'address', 'mobile']

        