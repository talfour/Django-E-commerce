from django.contrib import admin
from auctions.models import User, Auction, Image, Bid, Comment
# Register your models here.

admin.site.register(User)
admin.site.register(Auction)
admin.site.register(Image)
admin.site.register(Bid)
admin.site.register(Comment)


# class PostImageAdmin(admin.StackedInline):
#     model = Image

# @admin.register(Auction)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostImageAdmin]

#     class Meta:
#         model = Auction

# @admin.register(Image)
# class PostImageAdmin(admin.ModelAdmin):
#     pass