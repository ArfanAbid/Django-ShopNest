from django.shortcuts import render,get_object_or_404,redirect
from item.models import Item
from.models import Conversation
from.forms import ConversationMessageForm



def new_conversation(request,item_id):
    item=get_object_or_404(Item,id=item_id)
    #if you are the ownre yhem u are not be able to visit this page
    if item.created_by == request.user:
        return redirect('index')
    
    # now getting all the conversation related to item where u are the member


