from django.views.generic import TemplateView

from secret.models import Folder

class IndexView(TemplateView):
    model = Folder
    template_name = 'pages/index.html'

    def get_queryset(self):
        self.object_list = Folder.objects.filter(owner=self.request.user)
        return self.object_list
