from django.shortcuts import render,get_object_or_404,redirect
from item.models import Item
from.models import Conversation
from.forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required

@login_required
def new_conversation(request,item_id):
    item=get_object_or_404(Item,id=item_id)
    #if you are the ownre yhem u are not be able to visit this page
    if item.created_by == request.user:
        return redirect('index')
    
    # now getting all the conversation related to item where u are the member:
    conversation=Conversation.objects.filter(item=item).filter(members__in=[request.user.id]) # if this id is one in member then they can proceed

    #if there is already conversation bw owner and you then:
    
    if conversation:
        pass #redirect to conversation page later
    
    
    # if form is submitted then:
    if request.method == 'POST':
        form=ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation=Conversation.objects.create(item=item)
            # conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()
            
            return redirect('item:detail',pk=item_id)
        
    else:
        form=ConversationMessageForm()
        
    return render(request,'conversation/new.html',{'form':form})        
        
        

@login_required
def inbox(request):
    conversation=Conversation.objects.filter(members__in=[request.user.id])   
        
    return render(request,'conversation/inbox.html',{'conversation':conversation})