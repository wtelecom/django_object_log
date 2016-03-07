from django.core.exceptions import ObjectDoesNotExist
from object_log.models import LogAction, LogItem

class LogMiddleware(object):
    def process_request(self, request):


        try:
            action = LogAction.objects.get(name=request.path)
        except ObjectDoesNotExist:
            action = LogAction.objects.create(name=request.path, 
                template=request.path)
            action.save()
        except Exception:
            action = None
             
        if action:              
            # Add log entry
            entry = LogItem.objects.create(action=action, user=request.user)
            entry.save()


        
            