from django import forms
from django.utils.safestring import mark_safe
from .models import User, Auction, Category, Comment, Bid

class CreateForm(forms.ModelForm):
    title = forms.CharField(label=mark_safe("<strong>Titre de votre enchère</strong>"),
                            min_length=1,
                            max_length=100,
                            widget=forms.TextInput
                            (attrs={'class':'form-control',
				            'placeholder':'Titre'
                            }))

    image = forms.URLField(label=mark_safe("<strong>Lien vers une image</strong>"),
                            max_length=1000,
                            widget=forms.URLInput
                            (attrs={'class':'form-control',
                            'placeholder':'URL'
                            }))

    content = forms.CharField(label=mark_safe("<strong>Description de votre enchère</strong>"),
                            min_length=20,
                            max_length=1000,
                            widget=forms.Textarea
                            (attrs={'class':'form-control',
				            'placeholder':'Description'
                            }))

    starting_price = forms.DecimalField(label=mark_safe("<strong>Prix de départ (€)</strong>"),
                            min_value=0.01,
                            widget=forms.NumberInput
                            (attrs={'class':'form-control',
				            'placeholder':'Prix de départ'
                            }))

    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                            label=mark_safe("<strong>Catégorie</strong>"),
                            required=True,
                            widget= forms.Select
                            (attrs={'class':'form-control'
                            }))
                            
    class Meta:
        model = Auction
        exclude = ["author", "date", "active"]

class CommentForm(forms.ModelForm):
    content = forms.CharField(label=mark_safe("<strong>Type your comment below</strong>"),
                            min_length=1,
                            max_length=100,
                            widget=forms.TextInput
                            (attrs={'class':'form-control mb-2',
				            'placeholder':'Votre commentaire'
                            }))
                            
    class Meta:
        model = Comment
        exclude = ["auction", "author", "date"]

class BidForm(forms.ModelForm):
    amount = forms.DecimalField(label=mark_safe("<strong>Place your bid</strong>"),
                            min_value=0.01,
                            widget=forms.NumberInput
                            (attrs={'class':'form-control',
				            'placeholder':'Montant'
                            }))
                            
    class Meta:
        model = Bid
        exclude = ["auction", "author", "date"]

class SearchForm(forms.Form):
    search = forms.CharField(label="",
                            min_length=1,
                            max_length=50,
                            widget=forms.TextInput
                            (attrs={'class':'form-control mr-sm-2',
				            'placeholder':'Produit ou catégorie',
                            'type':'search',
                            'aria-label':'Search'
                            }))