from django.contrib import admin

admin.site.site_index_title= "Ho Technical University Admin Dashbord"
admin.site.site_title= "Ho Technical University Election"
admin.site.site_header= "HEY! Welcome To Ho Technical University Vote Site"

# Register your models here.
from.models import Question,choice,name,Image
# UploadImage
#in other to have the multiple choices field to the Question we will use "tabularline" to make the choices Inline and also you must specify the models which would be inline ,like this
#extra means the multiple choices field .
class ChoiceInline(admin.TabularInline):
    model= choice
    extra= 3

class imageInline(admin.TabularInline):
    model= Image
    extra= 3
    list_display = ["title", "photo"]

   

# class UploadImageInline(admin.TabularInline):
#     model= UploadImage
#     extra= 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['vote_question']}),
    ('Date information', {'fields': ['vote_date'], 'classes': ['collapse']}),]
    inlines =[ChoiceInline,imageInline]

    




# admin.site.register(Image, imageInline) 
# , UploadImageInline

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [(None, {'fields': ['vote_question']}),
#     ('Date information', {'fields': ['vote_date'], 'classes': ['collapse']}),]
#     inlines =[UploadImageInline]   


# class ChoiceInline(admin.TabularInline):
#     model = choice
#     extra = 3

# class UploadImageInline(admin.TabularInline):
#     model = UploadImage
#     extra = 3

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['vote_question']}),
#         ('Date information', {'fields': ['vote_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline, UploadImageInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(name)
# admin.site.register(UploadImage)

# admin.site.register(choice)

