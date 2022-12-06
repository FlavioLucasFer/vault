from django.views.generic import TemplateView

from secret.models import Folder, Team

class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['teams'] = Team.objects.filter(manager=self.request.user.id)
        data['folders'] = Folder.objects.filter(owner=self.request.user.id)
        return data

