from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

from feedbacks.forms import FeedbackForm
from feedbacks.models import Feedback


class FeedbackView(CreateView):
    template_name = 'feedback.html'
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return response
