from django.contrib import admin
from secondapp.models import (Student,Contact_Us,Category, 
register_table,add_product,cart,Order)

admin.site.site_header="My Website | Second Project"

class StudentAdmin(admin.ModelAdmin):
    # fields = ["roll_no","email","name"]
    list_display = ["name","roll_no","email","fee","gender","address","is_registered"]
    search_fields = ["roll_no","name"]
    list_filter =["name","gender"]
    list_editable = ["email",]

class Contact_UsAdmin(admin.ModelAdmin):
    fields = ["contact_number","name","subject","message"]

    list_display = ["id","name","contact_number","subject","message","added_on"]
    search_fields = ["name"]
    list_filter = ["added_on","name"]
    list_editable = ["name"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","cat_name","description","added_on"]

admin.site.register(Student,StudentAdmin)
admin.site.register(Contact_Us,Contact_UsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(register_table)
admin.site.register(add_product)
admin.site.register(cart)
admin.site.register(Order)