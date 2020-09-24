from django.forms import ModelForm, TextInput, Textarea
from django import forms

from .models import Auction, Image, Bid, Comment



class AuctionForm(ModelForm):
    
    class Meta:
        CHOICES = (
        ('no_category','No category'),
        ('fashion','Fashion'),
        ('tools','Tools'),
        ('toys','Toys'),
        ('electronics','Electronics'),
        ('home accesories','Home accessories'),
        ('books','Books'))

        model = Auction
        fields = ['title','description', 'category']
        widgets = {
            'category': forms.Select(choices=CHOICES,attrs={'class':'category'}),
            'description': Textarea(attrs={'class':'description'}),
            'title': TextInput(attrs={'class':'title'}),
            
        }
    def __init__(self, *args, **kwargs):
        super(AuctionForm,self).__init__(*args,**kwargs)
        self.fields['title'].required = True
        self.fields['description'].required = True
        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'form-control'
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if title is not None:
            return title
        else:
            raise forms.ValidationError("Title cannot be empty")
    def clean_description(self, *args, **kwargs):
        description = self.cleaned_data.get('description')
        if description is not None:
            return description
        else:
            raise forms.ValidationError("Description cannot be empty")

        

class ImageForm(ModelForm):
    
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}), required=True)
    
    class Meta:
        model = Image
        exclude = ['auction','user']
    def __init__(self, *args, **kwargs):
        super(ImageForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'image-input'

    def clean_image(self):
        image = self.cleaned_data.get['image']
        if len(image) != 0:
            return image
        else:
            raise forms.ValidationError("You have to provide at least one image.")

class BidForm(ModelForm):
    class Meta:
        model = Bid
        exclude = ['auction', 'highest_bidder']
    def __init__(self, *args, **kwargs):
        super(BidForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'bid'

    def clean_bid(self, *args, **kwargs):
        bid = self.cleaned_data.get['starting_bid']
        if bid != 0:
            return bid
        else:
            raise forms.ValidationError("You have to put minimum bid value.")

class AddBidForm(ModelForm):
    class Meta:
        model = Bid
        exclude = ['auction', 'highest_bidder']

    def __init__(self, *args, **kwargs):
        super(AddBidForm,self).__init__(*args,**kwargs)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['auction','user','time','active']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args,**kwargs)
        self.fields['comment'].required = True
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
