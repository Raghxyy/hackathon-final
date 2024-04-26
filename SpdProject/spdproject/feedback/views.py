from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.core.mail import send_mail
from .models import Feedback
import plotly.graph_objs as go

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

def thank_you_view(request):
    return render(request, 'feedback/thank_you.html')

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()

            # Send email notification
            subject = 'Feedback Submitted'
            message = f"Hi {feedback.name},\n\nThank you for your feedback. Your feedback content:\n\n{feedback.content}\n\nWe appreciate your input!"
            from_email = ''
            to_email = [feedback.email]
            send_mail(subject, message, from_email, to_email, fail_silently=True)

            return redirect('thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

def thank_you_view(request):
    return render(request, 'feedback/thank_you.html')

def feedback_graph(request):
    # Fetch feedback data
    feedback_data = Feedback.objects.all()

    # Extract data for visualization
    names = [feedback.name for feedback in feedback_data]
    feedback_count = len(names)

    # Create a pie chart
    fig = go.Figure(data=[go.Pie(labels=names, values=[1]*feedback_count)])
    graph_json = fig.to_json()

    return render(request, 'feedback_graph.html', {'graph_json': graph_json})

def feedback_dashboard(request):
    # Fetch feedback data
    feedback_data = Feedback.objects.all()

    # Extract data for visualization
    names = [feedback.name for feedback in feedback_data]
    emails = [feedback.email for feedback in feedback_data]
    contents = [feedback.content for feedback in feedback_data]
    created_at = [feedback.created_at for feedback in feedback_data]

    # Number of feedbacks
    feedback_count = len(names)

    # Create a pie chart for feedback count
    feedback_pie = go.Figure(data=[go.Pie(labels=['Feedback Count'], values=[feedback_count])])
    feedback_pie.update_layout(title_text="Feedback Count")
    feedback_pie_json = feedback_pie.to_json()

    # Create a bar chart for number of feedbacks per user
    feedback_per_user_bar = go.Figure(data=[go.Bar(x=names, y=[1]*feedback_count)])
    feedback_per_user_bar.update_layout(title_text="Feedbacks per User")
    feedback_per_user_bar_json = feedback_per_user_bar.to_json()

    # Create a line chart for feedback submissions over time
    feedback_over_time = go.Figure(data=[go.Scatter(x=created_at, y=[1]*feedback_count, mode='lines')])
    feedback_over_time.update_layout(title_text="Feedback Submissions Over Time")
    feedback_over_time_json = feedback_over_time.to_json()

    return render(request, 'feedback_dashboard.html', {
        'feedback_pie_json': feedback_pie_json,
        'feedback_per_user_bar_json': feedback_per_user_bar_json,
        'feedback_over_time_json': feedback_over_time_json,
        'feedback_count': feedback_count
    })
