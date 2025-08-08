from django.db import models
from django.utils import timezone

# ✅ Category model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Category"
   


# ✅ Customer model
class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# ✅ Product model
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/products/', blank=True, null=True)


    #add sales field
    is_sales = models.BooleanField(default=False)
    sales=models.DecimalField(default=0,decimal_places=2,max_digits=10)

    def __str__(self):
        return self.name

# ✅ Order model
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_ordered = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"
