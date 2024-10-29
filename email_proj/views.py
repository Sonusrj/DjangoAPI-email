from django.http import HttpResponse, HttpResponseServerError
from django.core.mail import send_mail
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

@api_view(['GET'])  # Allow only GET requests
def index(request):
    try:
        # Inject the respective values in HTML template
        html_message = loader.render_to_string(
            'email_proj/message.html',
            {
                'name': 'Sonu',
                'body': 'You Have done it',
            }
        )
        
        # Sending the email
        send_mail(
            'Congratulations!',
            'You are lucky to receive this mail.',
            'userx02002@gmail.com',  # Your email
            ['sonusaroj02010@gmail.com'],  # Recipient's email
            html_message=html_message,
            fail_silently=False,
        )

        return render(request, 'email_proj/success.html')

    except Exception as e:
        # Handle any exceptions and return an error response
        return HttpResponseServerError(f"Error sending email: {e}")
